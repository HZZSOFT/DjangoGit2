from django.db import models


# Create your models here.
class Permission(models.Model):
    user_type = models.BooleanField()
    description = models.CharField(max_length=500)


class Users(models.Model):
    permission = models.ForeignKey(Permission, on_delete=models.SET_NULL)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    mobile = models.CharField(max_length=11)
    address = models.CharField(max_length=500)
    email = models.EmailField()


class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    publish_date = models.DateTimeField()
    author = models.ForeignKey(Users, on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey(Users, on_delete=models.SET_NULL)
    post = models.ForeignKey(Posts, on_delete=models.SET_NULL)
    content = models.TextField()
    comment_date = models.DateTimeField
