from django.test import TestCase

from recipes.models import Category, User, Recipe


class RecipeTestBase(TestCase):
    def setUp(self) -> None:
        category = Category.objects.create(name='Category')
        author = User.objects.create_user(
            first_name='user',
            last_name='name',
            username='username',
            password='123456',
            email='user@gmail.com',
        )
        recipe = Recipe.objects.create( # noqa F841
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
        return super().setUp()
