# recipes/admin.py

from django.contrib import admin
from .models import Recipe, Comment

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('created_at', 'author')
    search_fields = ('title', 'description', 'ingredients')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'recipe', 'created_at')
    list_filter = ('created_at', 'author')
    search_fields = ('text',)