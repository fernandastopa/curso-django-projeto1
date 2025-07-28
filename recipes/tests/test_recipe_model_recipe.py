from .test_recipe_base import RecipeTestBase
from django.core.exceptions import ValidationError
from parameterized import parameterized


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def test_recipe_title_raises_error_when_title_is_grater_than_65(self):
        self.recipe.title = "A" * 70

        with self.assertRaises(ValidationError):
            # Vai levantar uma exceção quando fizer o full_clean()
            self.recipe.full_clean()  # Aqui ocorre a validação

    @parameterized.expand([
            ('title', 65),
            ('description', 165),
            ('preparation_time_unit', 65),
            ('servings_unit', 65),
        ])
    def test_recipe_max_length_fields(self, field, max_length):
        setattr(self.recipe, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()
