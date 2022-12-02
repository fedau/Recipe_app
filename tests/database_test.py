import unittest

from models.ingredients import Ingredient
from models.recipes import Recipe

class TestDataBase(unittest.TestCase):

    def setUp(self):
        self.ingredient = Ingredient('Cheese', 20)
        self.recipe = Recipe('Toast', 5, 'Crunchy', 'Toast bread smear spread', 'vegetarian', 'image')



    def test_ingredient_name(self):
        self.assertEqual('Cheese', self.ingredient.name)
    
    def test_ingredietn_amount(self):
        self.assertEqual(20, self.ingredient.amount)
        

    def test_recipe_name_cooking_time(self):
        self.assertEqual('Toast', self.recipe.name)
        self.assertEqual(5, self.recipe.cooking_time)