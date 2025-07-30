from django.urls import reverse, resolve
from recipes import views
# from unittest import skip

from .test_recipe_base import RecipeTestBase


# @skip('Vou pular a classe inteira de testes')
class RecipeHomeViewsTest(RecipeTestBase):

    # setUp()
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)
    # tearDown()

    # setUp()
    def test_recipe_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)
    # tearDown()

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h1>[404] Oops... There is nothing here :(</h1>',
            response.content.decode('utf-8')
        )

        # Testando self.fail()
        # self.fail('Testando se vou ser exibido como AssertionError')

    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe(category_data={
            'name': 'Café da manhã'
        })  # exemplo pra category_data e author_data
# caso passe parametros, tem que ser no tipo dict
        response = self.client.get(reverse('recipes:home'))
        response_context_recipes = response.context['recipes']
        content = response.content.decode('utf-8')
        # decode para que ele se torne uma string

        self.assertEqual(len(response_context_recipes), 1)
        self.assertIn('Café da manhã', content)
        self.assertIn('Title test', content)
        self.assertIn('Description test', content)
        self.assertIn('1 minutes', content)
        # dá pra conferir no debug console, com "-> content"
        # ...

    def test_recipe_home_template_doesnt_load_unpublished_recipes(self):
        self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')

        self.assertIn(
            '<h1>[404] Oops... There is nothing here :(</h1>',
            content
        )
