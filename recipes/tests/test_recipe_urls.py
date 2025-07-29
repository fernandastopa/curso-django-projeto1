from django.test import TestCase
from django.urls import reverse

# para exibir prints, -rP, configurado no pytest.ini


class RecipeURLsTest(TestCase):
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

    def test_recipe_search_url_is_correct(self):
        url = reverse('recipes:search')
        self.assertEqual(url, '/recipes/search/')

# Ciclo TDD: RED > GREEN > REFACTOR
# 1º: Testar o teste antes mesmo de implementar o código (red)
# 2º  Implementar o código e rodar o teste (green)
# 3º  Refatorar o que precisa
