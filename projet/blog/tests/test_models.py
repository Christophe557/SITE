from blog.models import Article, Categorie, Contenu,  TypeContenu
from mixer.backend.django import mixer
import pytest



@pytest.mark.django_db
class TestModels:

    def test_contenu_has_ancre(self):
        #contenu = mixer.blend('blog.Contenu', id=999)
        contenu = mixer.blend(Contenu, id=999)
        assert contenu.ancre == '#999'


        

