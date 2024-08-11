from django.shortcuts import get_list_or_404, render
# from utils.recipes.factory import make_recipe # Dados de Teste
from recipes.models import Recipe


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
        'title_page': 'Home',
    })


def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True
        ).order_by('-id'))

    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
        'title_page': f'{recipes[0].category.name} - Category',
    })


def recipe(request, id):
    recipe = Recipe.objects.filter(
        pk=id, is_published=True).order_by('-id').first()
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
        'title_page': f'{recipe.title}',
    })
