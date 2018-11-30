from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import (
    PostForm,
    CommentForm,
    SignUpForm,
    EditProfileForm
)
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash


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
            post = form.save(request)
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
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required()
def profile(request):
    args = {'user': request.user}
    return render(request, 'panel/profile.html', args)


@login_required()
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/panel/profile/')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'panel/edit_profile.html', args)

@login_required()
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/panel/profile/')
        else:
            return redirect('/panel/profile/password/')
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'panel/change_password.html', args)