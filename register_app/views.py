from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect


# Create your views here.
def index(request):
    return render(request, 'index.html', {'customers': customers})


def posts(request):
    all_post = Post.objects.all()
    return render(request, 'posts.html', {'posts': all_post})


def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('views.posts')
    else:
        form = PostForm()
    return render(request, 'new_post.html', {'form': form})


class Customer:
    def __init__(self, name, family, mobile, avg):
        self.name = name
        self.family = family
        self.mobile = mobile
        self.avg = avg


customers = [
    Customer('milad', 'hatami', '09384677005', 16.25),
    Customer('ali', 'rezaei', '09169555555', 19.50),
    Customer('hadi', 'razi', '09121231122', 15)
]
