from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction, IntegrityError
from django.db.models import Q

from itertools import chain
from operator import attrgetter

from .models import Categorie, TypeContenu, Article, Contenu
from .forms import CatForm, TypeForm, ArticleForm, ContenuForm

def index(request):
    articles = Article.objects.filter(publie=True).order_by('-created_at')[:3]
    categories = Categorie.objects.all()
    
    #  les 3 derniers articles publiés.
    context = {
            'articles': articles,
            'categories': categories
            }
    return render(request, 'blog/index.html', context)

def listing(request):
    # tous les articles publiés.
    articles = Article.objects.filter(publie=True).order_by('-created_at')
    categories = Categorie.objects.all()
    titre_page = "Tous les articles"
#    # pagination.
#    articles_par_page = 9 # nombre d'articles par page
#    paginator = Paginator(articles_list, articles_par_page)
#    page = request.GET.get('page')
#    try:
#        articles = paginator.page(page)
#    except PageNotAnInteger:
#        articles = paginator.page(1)
#    except EmptyPage:
#        articles = paginator.page(paginator.num_pages)
#    context = {
#        'articles': articles,
#        'paginate': True,
#        'categories': categories,
#        'titre_page': titre_page
#   }
    context = {
        'articles': articles,
        'categories': categories,
        'categorie_select': None,
        'titre_page': titre_page

    }
    
    return render(request, 'blog/listing.html', context)

def listing_cat(request, cat):
    # articles publiés de la categorie cat.
    categorie_select = Categorie.objects.get(nom=cat)
    articles = Article.objects.filter(publie=True, categorie=categorie_select).order_by('-created_at')
    categories = Categorie.objects.all()
    titre_page = f'Articles de la catégorie {categorie_select.nom}'
    context = {
        'articles': articles,
        'categories': categories,
        'categorie_select': categorie_select.nom,
        'titre_page': titre_page
    }
    return render(request, 'blog/listing.html', context)

def listing_search(request):
    # articles publiés recherchés
    query = request.GET.get('query')
    if not query:
        articles = Article.objects.filter(publie=True).order_by('-created_at')
    else:
        articles = Article.objects.filter(Q(publie=True) & 
                (Q(titre__icontains=query) | Q(resume__icontains=query))
                ).order_by('-created_at')

    n_articles = len(articles)    
    if n_articles == 0:
        titre_page = 'Désolé, aucun résultat pour la recherche "{}".'.format(query)
    elif n_articles ==1:
        titre_page = 'Résultat pour la recherche "{}" : {} article.'.format(query, n_articles)
    else:
        titre_page = 'Résultat pour la recherche "{}" : {} articles.'.format(query, n_articles)

    categories = Categorie.objects.all()
    context = {
        'articles': articles,
        'categories': categories,
        'categorie_select': None,
        'titre_page': titre_page
    }
    return render(request, 'blog/listing.html', context)


def lire_article(request, article_id):

#    # sélection de l'article à afficher :
#    # si l'article existe mais n'est pas publié (publie = False),
#    # on ne peut pas le lire car on génère une erreur 404

    article = get_object_or_404(Article, id=article_id, publie=True)

    # liste des contenus de l'article, en excluant les contenus de type 'image' dont le champ image est vide 
    # pour éviter l'erreur d'exécution du html : ValueError: The 'image' attribute has no file associated with it
    list_contenus = Contenu.objects.filter(article=article).exclude(typecontenu__nom='image', image='')
 
    # tri des contenus dans l'ordre d'affichage souhaité, donné par le champ position :
    contenus = sorted(
            chain(list_contenus),
            key=attrgetter('position')
            )

    # extrait du contenu "sous-titre" pour la construction du sommaire :
    # suppose qu'on ait défini un typecontenu "sous-titre", dont on veut afficher le texte.
    soustitres = [contenu for contenu in contenus 
            if contenu.typecontenu.nom == "sous-titre"]
    # les sous-titres ne seront affichés que si l'article a un contenu de type "sommaire".
    # cette condition est traitée dans le template lire_article.html

    # liste des catégories d'article pour la barre de navigation du blog:
    categories = Categorie.objects.all()

    context = {
            'article': article,
            'contenus': contenus,
            'soustitres': soustitres,
            'categories': categories
            }

    return render(request, 'blog/lire_article.html', context)       




def creation_models(request):
    return render(request, 'blog/creation_models.html', locals())
    
def creation_cat(request):
    form = CatForm(request.POST or None)
    if form.is_valid():
        categorie = form.save()
        categorie.save()
        envoi_cat = True
        return render(request, 'blog/creation_models.html', locals())
    return render(request, 'blog/creation_cat.html', locals())

def creation_type(request):
    form = TypeForm(request.POST or None)
    if form.is_valid():
        typecontenu = form.save()
        typecontenu.save()
        envoi_typ = True
        return render(request, 'blog/creation_models.html', locals())
    return render(request, 'blog/creation_type.html', locals())


def creation_article(request):
    form = ArticleForm(request.POST or None, request.FILES)
    if form.is_valid():
        article = form.save()
        article.save()
        envoi_art = True
        return render(request, 'blog/creation_models.html', locals())
    return render(request, 'blog/creation_article.html', locals())

def creation_contenu(request):
    form = ContenuForm(request.POST or None, request.FILES)
    if form.is_valid():
        contenu = form.save()
        contenu.save()
        envoi_con = True
        return render(request, 'blog/creation_models.html', locals())
    return render(request, 'blog/creation_contenu.html', locals())


def apropos(request):
    return render(request, 'blog/apropos.html')
