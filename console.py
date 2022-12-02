import pdb

from models.ingredients import Ingredient
from models.recipe_ingredient import Recipe_ingredient
from models.recipes import Recipe

import repositories.ingredient_repository as ingredient_repository
import repositories.recipe_ingredient as recipe_ingredient_repository
import repositories.recipe_repository as recipe_repository

recipe_ingredient_repository.delete_all()
recipe_repository.delete_all()
ingredient_repository.delete_all()

ingredient1 = Ingredient('Yoghurt', 100)
ingredient_repository.save(ingredient1)

ingredient2 = Ingredient('Noodles', 50)
ingredient_repository.save(ingredient2)

recipe1 = Recipe('Yoghurt', 10, 'Straight from the fridge', 'Pick your favorite yoghurt and add toppings', 'vegetarian', 'image')
recipe_repository.save(recipe1)

recipe2 = Recipe('Noodles', 15, "Instant love", "Boil water Open up the package", 'meat', 'image')
recipe_repository.save(recipe2)

recipe_ingredient1 = Recipe_ingredient(recipe1, ingredient1)
recipe_ingredient_repository.save(recipe_ingredient1)

recipe_ingredient2 = Recipe_ingredient(recipe2, ingredient2)
recipe_ingredient_repository.save(recipe_ingredient2)







pdb.set_trace()
