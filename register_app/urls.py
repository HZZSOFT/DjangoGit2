from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^posts', views.posts)
]
#    path('index/', views.index),
#    path('posts/', views.posts),

