from django.db import models


# Create your models here.
class Permission(models.Model):
    description = models.CharField(max_length=500)
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
    publish_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    comment_date = models.DateTimeField

    def __str__(self):
        return self.content
