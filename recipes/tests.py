from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views


class RecipeURLsTest(TestCase):
    def test_recipe_home_url_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')

    def test_recipe_category_url_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/recipe/category/1/')

    def test_recipe_details_url_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(url, '/recipe/1/')


class RecipeViewsTest(TestCase):
    def test_recipe_home_views_function_is_correct(self):
        view_home = resolve(reverse('recipes:home'))
        view_home_imported = views.home
        self.assertIs(view_home.func, view_home_imported)

    def test_recipe_category_views_function_is_correct(self):
        view_category = resolve(
            reverse('recipes:category', kwargs={'category_id': 1})
        )
        view_category_imported = views.category
        self.assertIs(view_category.func, view_category_imported)

    def test_recipe_details_views_function_is_correct(self):
        view_details = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        view_details_imported = views.recipe
        self.assertIs(view_details.func, view_details_imported)
