from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm, CommentForm
from django.shortcuts import redirect
from django.contrib.auth import logout


# Create your views here.
def index(request):
    all_post = Post.objects.all()
    return render(request, 'index.html', {'posts': all_post})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect(post)
    else:
        comment_form = CommentForm()

    return render(request, 'post_detail.html', {'post': post,
                                                'comments': comments,
                                                'comment_form': comment_form})


def logout_view(request):
    logout(request)
    return render(request, 'panel/logout.html')


def login():
    return


@login_required
def posts(request):
    all_post = Post.objects.all()
    return render(request, 'panel/posts.html', {'posts': all_post})


@login_required
def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('posts')
    else:
        form = PostForm()
    return render(request, 'panel/new_post.html', {'form': form})


@login_required()
def panel(request):
    return render(request, 'panel/panel.html', {})
