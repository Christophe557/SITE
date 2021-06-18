from django.test import RequestFactory
from django.urls import reverse
from blog.models import Article, Categorie, TypeContenu
from blog import views
from mixer.backend.django import mixer
import pytest

from django.http import Http404


@pytest.mark.django_db
class TestViews:

    def test_lire_article_publie(self):
        """
        la vue renvoie un status_code 200 quand on veut
        lire un article existant et dont le champ publie = True
        """
        article = mixer.blend('blog.Article', id=1, publie=True)
        path = reverse('blog:lire_article', kwargs={'article_id': 1})
        request = RequestFactory().get(path)
        response = views.lire_article(request, article_id=1)
        assert response.status_code == 200

    def test_lire_article_non_publie(self):
        """
        si on tente de lire un article existant mais qui n'est pas publié
        (champ publie = False) la vue renvoie une erreur 404
        """
        article = mixer.blend('blog.Article', id=1, publie=False)
        path = reverse('blog:lire_article', kwargs={'article_id': 1})
        request = RequestFactory().get(path)
        status = 0
        try:
            response = views.lire_article(request, article_id=1)
        except Http404:
            status = 404
        assert status == 404

