# recipes/views.py

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics

from blog.models import Post
from .forms import RecipeForm, CommentForm
from .models import Recipe
from .serializers import RecipeSerializer


class RecipeListAPI(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


def recipe_list(request):
    recipes = Recipe.objects.all().order_by('-created_at')

    # Фильтрация по заголовку
    title_query = request.GET.get('title')
    if title_query:
        recipes = recipes.filter(title__icontains=title_query)

    # Фильтрация по ингредиентам
    ingredients_query = request.GET.get('ingredients')
    if ingredients_query:
        recipes = recipes.filter(ingredients__icontains=ingredients_query)

    # Фильтрация по автору
    author_query = request.GET.get('author')
    if author_query:
        recipes = recipes.filter(author__username__icontains=author_query)

    paginator = Paginator(recipes, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'recipes/recipe_list.html', {'page_obj': page_obj})


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    ingredients = recipe.ingredients.split('\n')
    instructions = recipe.instructions.split('\n')

    comments = recipe.comments.all().order_by('-created_at')

    # Пагинация комментариев
    paginator = Paginator(comments, 10)  # 10 комментариев на страницу
    page_number = request.GET.get('page')
    comments_page = paginator.get_page(page_number)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.recipe = recipe
            new_comment.author = request.user
            new_comment.save()
            return redirect('recipe_detail', pk=pk)
    else:
        comment_form = CommentForm()

    return render(request, 'recipes/recipe_detail.html', {
        'recipe': recipe,
        'ingredients': ingredients,
        'instructions': instructions,
        'comments': comments_page,
        'comment_form': comment_form
    })


def user_recipes(request, username):
    user = get_object_or_404(User, username=username)
    recipes = Recipe.objects.filter(author=user).order_by('-created_at')

    paginator = Paginator(recipes, 10)  # 10 рецептов на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'author': user
    }
    return render(request, 'recipes/user_recipes.html', context)


@login_required
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            form.save_m2m()  # Это сохранит теги
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form})


@login_required
def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.user != recipe.author:
        return redirect('recipe_detail', pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.save()
            form.save_m2m()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/recipe_form.html', {'form': form})


@login_required
def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.user != recipe.author:
        return redirect('recipe_detail', pk=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe_list')
    return render(request, 'recipes/recipe_confirm_delete.html', {'recipe': recipe})


@login_required
def like_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.user in recipe.likes.all():
        recipe.likes.remove(request.user)
    else:
        recipe.likes.add(request.user)
    return redirect('recipe_detail', pk=pk)


def popular_recipes(request):
    recipes = Recipe.popular.all()[:10]  # Получаем 10 самых популярных рецептов
    return render(request, 'recipes/popular_recipes.html', {'recipes': recipes})


def search_recipes(request):
    query = request.GET.get('q')
    if query:
        recipes = Recipe.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(ingredients__icontains=query) |
            Q(instructions__icontains=query)
        ).distinct()
    else:
        recipes = Recipe.objects.all()

    paginator = Paginator(recipes, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'recipes/search_results.html', {'page_obj': page_obj, 'query': query})


def home(request):
    latest_recipes = Recipe.objects.order_by('-created_at')[:5]
    latest_posts = Post.objects.order_by('-created_at')[:5]
    context = {
        'latest_recipes': latest_recipes,
        'latest_posts': latest_posts,
    }
    return render(request, 'home.html', context)
