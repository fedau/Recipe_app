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

ingredient3 = Ingredient('Soupbase', 50)
ingredient_repository.save(ingredient3)

ingredient4 = Ingredient('Fruitmix', 80)
ingredient_repository.save(ingredient4)

ingredient5 = Ingredient('Vegetables mix', 140)
ingredient_repository.save(ingredient5)



recipe1 = Recipe('Yoghurt', 10, 'Straight from the fridge', 'Pick your favorite yoghurt and add toppings', 'dessert', 'https://images.unsplash.com/photo-1530259152377-3a014e1092e0?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2069&q=80')
recipe_repository.save(recipe1)

recipe2 = Recipe('Noodles', 15, "Instant love", "Boil water Open up the package", 'meat', 'https://images.unsplash.com/photo-1553621043-f607bfbf6640?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1626&q=80')
recipe_repository.save(recipe2)


recipe_ingredient1 = Recipe_ingredient(recipe1.id, ingredient1.id)
recipe_ingredient_repository.save(recipe_ingredient1)
recipe_ingredient3 = Recipe_ingredient(recipe1.id, ingredient4.id)
recipe_ingredient_repository.save(recipe_ingredient3)

recipe_ingredient2 = Recipe_ingredient(recipe2.id, ingredient2.id)
recipe_ingredient_repository.save(recipe_ingredient2)

recipe_ingredient4 = Recipe_ingredient(recipe2.id, ingredient3.id)
recipe_ingredient_repository.save(recipe_ingredient4)

recipe_ingredient4 = Recipe_ingredient(recipe2.id, ingredient5.id)
recipe_ingredient_repository.save(recipe_ingredient4)





# pdb.set_trace()
