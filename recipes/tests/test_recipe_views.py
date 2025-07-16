from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase


class RecipeViewsTest(RecipeTestBase):

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
        ...

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:category', kwargs={'category_id': 1})
        )
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_status_code_404(self):
        response = self.client.get(
            reverse('recipes:category',
                    kwargs={'category_id': 9999})
        )
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:recipe', kwargs={'id': 1})
        )
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_returns_status_code_404(self):
        response = self.client.get(
            reverse('recipes:recipe',
                    kwargs={'id': 9999})
        )
        self.assertEqual(response.status_code, 404)
