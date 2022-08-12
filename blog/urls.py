from django.urls import path
from .views import *
app_name = 'blog'

urlpatterns=[
    path('', index, name='index'),
    path('post/', post_list, name='post_list'),
    path('search/', search, name='search_results'),
    path('post/<id>/', post_detail, name='post_detail'),
    path('post/<id>/update/', post_update, name='post_update'),
    path('post/<id>/delete/', post_delete, name='post_delete'),
    path('create/', post_create, name='post_create'),
    path('create-blog-category/', createCat, name='createCat'),
    path('search/', search, name='search'),
    path('search/<str:cat>', categorysearch, name='catsearch'),

]