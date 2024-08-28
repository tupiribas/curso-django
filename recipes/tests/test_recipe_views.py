from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views
from recipes.models import Category, Recipe, User


class RecipeViewsTest(TestCase):
    def test_recipe_home_views_function_is_correct(self):
        view_home = resolve(path=reverse(viewname='recipes:home'))
        view_home_imported = views.home
        self.assertIs(view_home.func, view_home_imported)

    def test_recipe_home_view_returns_status_code_200_OK(self):
        response = self.client.get(path=reverse(viewname='recipes:home'))
        status_code = 200
        msg_status = 'OK'
        self.assertEqual(response.status_code, status_code)
        self.assertEqual(response.reason_phrase, msg_status)

    def test_recipe_home_view_loads_correct_tamplate(self):
        response = self.client.get(path=reverse(viewname='recipes:home'))
        path_tamplate = 'recipes/pages/home.html'
        self.assertTemplateUsed(response, path_tamplate)

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(path=reverse(viewname='recipes:home'))
        part_html = '<h1 class="center m-y">No recipes found here 🥲</h1>'
        self.assertIn(
            part_html,
            response.content.decode('utf-8')
        )

    def test_recipe_home_template_loads_recipes(self):
        category = Category.objects.create(name='Category')
        author = User.objects.create_user(
            first_name='user',
            last_name='name',
            username='username',
            password='123456',
            email='user@gmail.com',
        )
        recipe = Recipe.objects.create(
            category=category,
            author=author,
            title='receita',
            description='teste descricao',
            slug='teste-receita',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porção',
            preparation_steps='Recipes tesinf en brasilian',
            preparation_steps_is_html=False,
            is_published=True,
        )
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        self.assertIn('Receita', content)

    def test_recipe_category_views_function_is_correct(self):
        view_category = resolve(
            path=reverse(
                viewname='recipes:category', kwargs={'category_id': 1000}
            )
        )
        view_category_imported = views.category
        self.assertIs(view_category.func, view_category_imported)

    def test_recipe_category_view_returns_status_404_if_no_recipes_found(self):
        response = self.client.get(path=reverse(
            viewname='recipes:category', kwargs={'category_id': 1000}
            )
        )
        status_code = 404
        self.assertEqual(response.status_code, status_code)

    def test_recipe_details_views_function_is_correct(self):
        view_details = resolve(path=reverse(
            viewname='recipes:recipe', kwargs={'id': 1}
            )
        )
        view_details_imported = views.recipe
        self.assertIs(view_details.func, view_details_imported)

    def test_recipe_details_view_return_status_404_if_no_recipes_found(self):
        response = self.client.get(path=reverse(
            viewname='recipes:recipe', kwargs={'id': 1000}
        ))
        status_code = 404
        self.assertEqual(response.status_code, status_code)
