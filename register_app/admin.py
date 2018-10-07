from django.contrib import admin
from .models import User
from .models import Permission
from .models import Post
from .models import Comment
# Register your models here.
admin.site.register(User)
admin.site.register(Permission)
admin.site.register(Post)
admin.site.register(Comment)
