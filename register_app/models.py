from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Permission(models.Model):
    description = models.CharField(max_length=500, help_text="Description of this privillage")
    is_Admin = models.BooleanField()

    def __str__(self):
        return self.description


class User(models.Model):
    permission = models.ForeignKey(Permission, on_delete=models.SET_NULL, null=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    mobile = models.CharField(max_length=11)
    address = models.CharField(max_length=500)
    email = models.EmailField()

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.title])


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    content = models.TextField()
    comment_date = models.DateTimeField(default=timezone.now())
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('comment_date',)

    def __str__(self):
        return 'comment by {} on {}'.format(self.name, self.post)
