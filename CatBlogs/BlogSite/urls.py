from . import views
from django.urls import path
from .views import index, create_article, article_detail, catBreeds, blogs

urlpatterns = [
    path('', index, name='index'),
    path('create_article/', create_article, name='create_article'),
    path('article/<int:article_id>/', article_detail, name='article_detail'),
    path('like/<int:article_id>/', views.like_article, name='like_article'),
    path('comment/<int:article_id>/', views.add_comment, name='add_comment'),
    path('cat_breeds', catBreeds, name='cats'),
    path('cat_blogs', blogs, name='blogs'),
    path('cats/<int:cat_id>/', views.cat_detail, name='cat_detail'),
]

