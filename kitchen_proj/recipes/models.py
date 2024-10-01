# recipes/models.py

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count
from taggit.managers import TaggableManager


class PopularRecipeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(like_count=Count('likes')).order_by('-like_count')


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = TaggableManager()
    likes = models.ManyToManyField(User, related_name='liked_recipes', blank=True)

    objects = models.Manager()
    popular = PopularRecipeManager()

    def __str__(self):
        return self.title


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.recipe}'
