# recipes/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/new/', views.recipe_create, name='recipe_create'),
    path('recipe/<int:pk>/edit/', views.recipe_edit, name='recipe_edit'),
    path('recipe/<int:pk>/delete/', views.recipe_delete, name='recipe_delete'),
    path('recipe/<int:pk>/like/', views.like_recipe, name='like_recipe'),
    path('popular/', views.popular_recipes, name='popular_recipes'),
    path('api/recipes/', views.RecipeListAPI.as_view(), name='recipe_list_api'),

    path('search/', views.search_recipes, name='search_recipes'),
    path('user/<str:username>/', views.user_recipes, name='user_recipes'),
]
