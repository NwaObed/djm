from cgitb import text
from turtle import title
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = get_user_model()
    author = models.ForeignKey(user, on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    published_date = models.DateTimeField()