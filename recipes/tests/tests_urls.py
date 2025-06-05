from django.test import TestCase
from django.urls import reverse

# para exibir prints, -rP


class TestRecipeURLs(TestCase):
    def test_recipe_home_url_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')  # não requer path pois home é "/"

    def test_recipe_category_url_is_correct(self):
        # a chave terá o mesmo nome que o campo no path
        url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/recipes/category/1/')

    def test_recipe_detail_url_is_correct(self):
        # recipes:recipe > nome do app e name da url
        url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(url, '/recipes/1/')  # path de fato
