from django.contrib import admin
from .models import Post, PostView, User
# Register your models here.
admin.site.register(Post)
admin.site.register(PostView)
admin.site.register(User)