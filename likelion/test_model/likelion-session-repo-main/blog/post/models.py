from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.


class Post(models.Model):
    content = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
