from django.urls import path, re_path
from .import views


app_name = 'blog'

urlpatterns =[
    re_path(r'^$', views.listing, name='listing'),
    re_path(r'^(?P<article_id>[0-9]+)/$', views.lire_article, name='lire_article'),
    re_path(r'^cat/(?P<cat>[\w-]+)/$', views.listing_cat, name='listing_cat'),
#   la ligne du dessus peut être plus simplement remplacée par celle ci-dessous:
#   path('cat/<cat>/', views.listing_cat, name='listing_cat'),
    re_path(r'^search/$', views.listing_search, name='listing_search'),
    re_path(r'^creation_models_he5f5L6spg6eo4dZ64/$', views.creation_models, name='creation_models'),
    re_path(r'^creation_cat_he5f5L6spg6eo4dZ64/$', views.creation_cat, name='creation_cat'),
    re_path(r'^creation_type_he5f5L6spg6eo4dZ64/$', views.creation_type, name='creation_type'),
    re_path(r'^creation_article_he5f5L6spg6eo4dZ64/$', views.creation_article, name='creation_article'),
    re_path(r'^creation_contenu_he5f5L6spg6eo4dZ64/$', views.creation_contenu, name='creation_contenu'),
    re_path(r'^apropos/$', views.apropos, name='apropos'),
    ]



