from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


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


class CommentList(TemplateView):
    template_name = 'panel/comment_list.html'

    comments = Comment.objects.all()

    def get_context_data(self, **kwargs):
        context = ({
            'comments': self.comments,
        })
        return context


@login_required()
def approve_comment(request):
    current_id = request.GET.get('id')
    try:
        comment = Comment.objects.get(id=current_id)
        comment.active = True
        comment.save()
    except Comment.DoesNotExist:
        return HttpResponse("<div style='height: 200px;width:200px;margin: 0 auto;padding: 50px;'>"
                            "<h3>Comment not found</h3><div>")
    return render(request, "panel/approve_comment.html", {'comment': comment})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()

        args = {'form': form}
        return render(request, 'registration/signup.html', args)
