from pyexpat import model
from statistics import mode
from turtle import title
from unicodedata import category
from django.db import models
from django.forms import SlugField

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Post(models.Model):
    category = models.ForeignKey(Category, related_name='post', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    intro = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

class Meta:
    ordering = ('-created_at', )

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)  
    email = models.EmailField(max_length=255)  
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

