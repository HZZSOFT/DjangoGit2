from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.shortcuts import redirect
from django.contrib.auth import logout


# Create your views here.
def index(request):
    all_post = Post.objects.all()
    return render(request, 'index.html', {'posts': all_post})


def post_detail(request, post):
    post1 = get_object_or_404(Post, title=post)
    return render(request, 'post_detail.html', {'post': post1})


def logout_view(request):
    logout(request)
    return render(request, 'logout.html')


def login():
    return


@login_required
def posts(request):
    all_post = Post.objects.all()
    return render(request, 'posts.html', {'posts': all_post})


@login_required
def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('posts')
    else:
        form = PostForm()
    return render(request, 'new_post.html', {'form': form})