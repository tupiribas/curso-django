from django.urls import resolve, reverse

from recipes import views
# from unittest import skip
from recipes.tests.test_recipe_base import RecipeTestBase


class RecipeViewsTest(RecipeTestBase):
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

    # @skip('WIP')
    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(path=reverse(viewname='recipes:home'))
        part_html = '<h1 class="center m-y">No recipes found here 🥲</h1>'
        self.assertIn(
            part_html,
            response.content.decode('utf-8')
        )

    def test_recipe_home_template_loads_recipes(self):
        # Need a recipe for this test
        self.make_recipe()

        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        response_context_recipe = response.context['recipes']

        # Check if one recipe exist
        self.assertIn('Recipes', content)
        self.assertEqual(len(response_context_recipe), 1)

    def test_recipe_home_template_dont_load_recipes_not_published(self):
        """Test recipe is_pulished False and not show"""
        part_html = '<h1 class="center m-y">No recipes found here 🥲</h1>'
        # Need a recipe for this test
        self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')

        # Check if one recipe exist
        self.assertIn('Recipes', content)
        self.assertIn(part_html, content)

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

    def test_recipe_category_template_dont_load_recipes_not_published(self):
        """Test recipe is_pulished False and not show"""
        # Need a recipe for this test
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(path=reverse(
            viewname='recipes:category',
            kwargs={'category_id': recipe.category.id}
            )
        )

        status_code = 404
        self.assertEqual(response.status_code, status_code)

    def test_recipe_category_template_loads_recipes(self):
        needed_title = 'This Is A Category Test'
        # Need a recipe for this test
        self.make_recipe(title=needed_title)

        response = self.client.get(reverse('recipes:category',
                                           kwargs={'category_id': 1}))
        content = response.content.decode('utf-8')

        # Check if one recipe exist
        self.assertIn(needed_title, content)

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

    def test_recipe_details_template_loads_the_correct_recipe(self):
        needed_title = 'This is a details page - It Load one recipe'
        # Need a recipe for this test
        self.make_recipe(title=needed_title)

        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        content = response.content.decode('utf-8')

        # Check if one recipe exist
        self.assertIn(needed_title, content)

    def test_recipe_detail_template_dont_load_recipe_not_published(self):
        """Test recipe is_pulished False and not show"""
        # Need a recipe for this test
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(path=reverse(
            viewname='recipes:recipe',
            kwargs={'id': recipe.id}
            )
        )

        status_code = 404
        self.assertEqual(response.status_code, status_code)
