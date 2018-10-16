from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^posts/new', views.new_post, name='new_post'),
    url(r'^posts/', views.posts, name='posts')
]
#    path('index/', views.index),
#    path('posts/', views.posts),

