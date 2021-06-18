from django.urls import reverse, resolve


class TestUrls:

    def test_index(self):
        path = reverse('index')
        assert resolve(path).view_name == 'index'


    def test_listing(self):
        path = reverse('blog:listing')
        assert resolve(path).view_name == 'blog:listing'

    def test_lire_article(self):
        path = reverse('blog:lire_article', kwargs={'article_id': 1})
        assert resolve(path).view_name == 'blog:lire_article'

    def test_listing_cat(self):
        path = reverse('blog:listing_cat', kwargs={'cat': 'cat'})
        assert resolve(path).view_name == 'blog:listing_cat'

    def test_listing_search(self):
        path = reverse('blog:listing_search')
        assert resolve(path).view_name == 'blog:listing_search'

    def test_apropos(self):
        path = reverse('blog:apropos')
        assert resolve(path).view_name == 'blog:apropos'




