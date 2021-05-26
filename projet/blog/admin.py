from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType

from .models import Categorie, TypeContenu, Article, Contenu #, Paragraphe, Image, Citation, SousTitre, Liste

# _______________________________________________________________
# classe mixin pour récupérer facilement les adresse url des instances
# et pour les afficher dans l'interface d'administration

class AdminURLMixin(object):
    def get_admin_url(self, obj):
        content_type = ContentType.objects.get_for_model(obj.__class__)
        return reverse("admin:blog_%s_change" % (
            content_type.model),
            args=(obj.id,))



# _______________________________________________________________
# classes des modèles à afficher en table dans les classes liées:
# Articles dans Catégorie,
# Paragraphe, Image, Citation dans Article

class ArticleInline(admin.TabularInline, AdminURLMixin):
    # affiche sous une catégorie les articles qui lui sont liés
    model = Article
    # champs éditables à afficher
    fieldsets = [
            (None, {'fields': ['titre', 'auteur', 'publie', 'date_public', 'article_link']})
            ]
    # champs non modifiables à afficher
    readonly_fields = ['created_at', 'article_link']
    ordering = ('-created_at',)
    extra = 0
    
    # méthode pour pouvoir afficher le lien html des articles :
    def article_link(self, article):
        url = self.get_admin_url(article)
        return mark_safe("<a href='{}'>{}</a>".format(url, article.id))

    article_link.short_description = "lien"

class ContenuInline(admin.TabularInline, AdminURLMixin):
    # affiche sous un article les contenus qui lui sont liés
    model = Contenu
    # champs éditables à afficher
    fieldsets = [
            (None, {'fields': ['article', ('typecontenu', 'position', 'titre'), 'texte', 'image', 'contenu_link']})
            ]
    # champs non modifiables à afficher
    readonly_fields = ['contenu_link']
    ordering = ('position',)
    extra = 1
    
    # méthode pour pouvoir afficher le lien html des paragraphes :
    def contenu_link(self, contenu):
        url = self.get_admin_url(contenu)
        return mark_safe("<a href='{}'>{}</a>".format(url, contenu.id))

    contenu_link.short_description = "lien"


    
# _______________________________________________________________
# classes pour afficher chaque modèle dans l'interface d'administration

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    
    # affichage des catégories
    
    # affichage de la table des articles de la catégorie
    inlines = [ArticleInline,]


@admin.register(TypeContenu)
class TypeContenuAdmin(admin.ModelAdmin):
    
    # affichage des types de contenu
    
    # affichage de la table des contenu de chaque type de contenu
    inlines = [ContenuInline,]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # affichage des articles

    # définition d'une barre de recherche et de filtre sur les champs
    search_fields = ['titre', 'resume']
    list_filter = ['categorie', 'created_at', 'publie']

    # champs à afficher
    fieldsets = [
            (None, {'fields': [('titre', 'auteur', 'categorie', 'publie'), ('created_at', 'date_public', 'date_maj'), 'miniature', 'resume', ]})
            ]
 
    # déclarer les champs non modifiables pour pouvoir les afficher:
    readonly_fields = ['created_at']
    
    # affichage de la  table des contenus des articles:
    inlines = [ContenuInline,]


@admin.register(Contenu)
class ContenuAdmin(admin.ModelAdmin):
    # affichage des contenus

    # définition d'une barre de recherche et de filtre sur les champs
    search_fields = ['titre', 'texte']
    list_filter = ['typecontenu', 'article', 'position']

    # champs à afficher
    fieldsets = [
            (None, {'fields': [('article', 'typecontenu', 'position'), 'titre', 'texte', 'image',]})
            ]
  


