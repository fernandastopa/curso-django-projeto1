from django.contrib.auth.models import User
from django.test import TestCase
from recipes.models import Category, Recipe


class RecipeTestBase(TestCase):
    def setUp(self):
        # self.make_recipe(), só vai ser chamado nos testes que precisam
        # não precisou criar category e author nos testes,
        # pois eles já estão sendo criados dentro
        # de make_recipe, utilizando unpack e valores padrão
        return super().setUp()

    def make_category(self, name='Category'):
        return Category.objects.create(name=name)

    def make_author(
        self,
        first_name='user',
        last_name='name',
        username='username',
        password='123456',
        email='username@email.com'
    ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
        )

    def make_recipe(
        self,
        category_data=None,  # para poder transformar em {} e fazer unpack
        author_data=None,    # e o unpack transformar nos valores padrão
        title='Title test',
        description='Description test',
        slug='slug-test',
        preparation_time=1,
        preparation_time_unit='minutes',
        servings=1,
        servings_unit='people',
        preparation_steps='Preparation steps test',
        preparation_steps_is_html=False,
        is_published=True,
    ):
        if category_data is None:
            category_data = {}

        if author_data is None:
            author_data = {}

        return Recipe.objects.create(
            category=self.make_category(**category_data),  # unpack de nada
            # Resumo: None, {} e category_data, é pra simular
            # argumentos não passadosa pra category, para que o python utilize
            # o valor padrão, nesse caso, category='Category'
            author=self.make_author(**author_data),
            # Author também usará valores padrão
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
            is_published=is_published,
        )
