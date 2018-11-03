from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Permission(models.Model):
    description = models.CharField(max_length=200, help_text="Description of this privillage")
    is_Admin = models.BooleanField()

    def __str__(self):
        return self.description


class User(models.Model):
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=20)
    mobile = models.CharField(max_length=11, null=True)
    address = models.CharField(max_length=500, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, default=timezone.now())
    content = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    content = models.TextField()
    comment_date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)
    id = models.AutoField(primary_key=True)

    class Meta:
        ordering = ('comment_date',)

    def __str__(self):
        return self.content
