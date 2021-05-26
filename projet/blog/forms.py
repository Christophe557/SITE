
from django.forms import Form, ModelForm, TextInput
from .models import Categorie, TypeContenu, Article, Contenu 


class CatForm(ModelForm):
    class Meta:
        model = Categorie
        fields = ["nom"]

class TypeForm(ModelForm):
    class Meta:
        model = TypeContenu
        fields = ["nom"]

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = [
                "titre", 
                "auteur", 
                "publie", 
                "categorie", 
                "miniature", 
                "resume"
                ]

class ContenuForm(ModelForm):
    class Meta:
        model = Contenu
        fields = [
                "typecontenu", 
                "article", 
                "position",
                "titre", 
                "texte", 
                "image"
                ]





