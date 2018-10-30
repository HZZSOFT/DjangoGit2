from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CommentList
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(), name="login"),
    path('panel/logout/', views.logout_view, name="logout"),
    url(r'^$', views.index, name='index'),
    path('posts/<slug:slug>/', views.post_detail, name='post_detail'),
    path('panel/posts/new/', views.new_post, name='new_post'),
    path('panel/posts/', views.posts, name='posts'),
    path('panel/panel/', views.panel, name='panel'),
    path('panel/comments/', login_required(CommentList.as_view()), name="comment_list")
]
#    path('index/', views.index),
#    path('posts/', views.posts),

