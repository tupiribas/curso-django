from django.shortcuts import render
from utils.recipes.factory import make_recipe
from recipes.models import Recipe, Category


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
        'title_page': 'Home',
    })


def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id, is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
        'title_page': f'{recipes.first().category.name} - Category',
    })


def recipe(request, id):
    recipe = Recipe.objects.filter(id=id)
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipes': recipe,
        'is_detail_page': True,
        'title_page': 'Details',
    })
