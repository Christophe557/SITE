from django.db import models

# Create your models here.


class Article(models.Model):

    # données générales sur l'article
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=20, blank=True)
    created_at = models.DateField(auto_now_add=True, verbose_name='date de création')
    date_public = models.DateField(verbose_name='date de publication', blank=True)
    date_maj = models.DateField(verbose_name='date de mise à jour', blank=True)
    publie = models.BooleanField(default=False)
    slug = models.SlugField(max_length=50, blank=True)
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)
    
    # pour affichage dans le sommaire
    miniature = models.ImageField(upload_to="blog/miniatures/")
    resume = models.TextField(max_length=200)

    # contenu détaillé de l'article
    # dans class Contenu.



    class Meta:
        verbose_name = "article"
        ordering = ['created_at']


    def __str__(self):
        return self.titre


class TypeContenu(models.Model):

    # les types de contenu : paragraphe, image, sous-titre, ...
    nom = models.CharField(max_length=20)

    class Meta:
        verbose_name = "type"

    def __str__(self):
        return self.nom



class Contenu(models.Model):
    

    #  le type de contenu : paragraphe, image, sous-titre, ...
    typecontenu = models.ForeignKey('TypeContenu', on_delete=models.CASCADE)
    # article auquel apprtient ce contenu :
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    
    # le contenu :
    
    # titre non affichable (ex: parag. 1), et sert de alt pour une image
    titre = models.CharField(max_length=20)
    # contenu titre, paragraphe affichable, sert de légende pour une image
    texte = models.TextField(max_length=1000, blank=True)
    # contenu image
    image = models.ImageField(upload_to="blog/images/", blank=True)

    # position du contenu dans l'article :
    position = models.IntegerField()

    class meta:
        verbose_name = "contenu"
    
    # définition d'une ancre à inclure dans le fichier html
    # par exemple : <a href='{% url contenu.ancre %}'>Lien</a>
    # pour pouvoir accéder directement au contenu <p id='{{contenu.id}}'> blabla </p>
    # utilisé pour créer des liens-ancres dans le sommaire.
    @property
    def ancre(self):
        return '#'+str(self.id)


    def __str__(self):
        return self.article.titre[:10]+ "_" + str(self.position) + "_" + self.titre



class Categorie(models.Model):

    nom = models.CharField(max_length=100)

    class Meta:
        verbose_name = "categorie"

    def __str__(self):
        return self.nom


class Contact(models.Model):
    pass


class Commentaire(models.Model):
    pass 
