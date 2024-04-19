from django.db import models
from django.contrib.auth.models import User
from blog.models import Post

class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posts = models.ManyToManyField(Post)
