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


recipe1 = Recipe('Yoghurt', 10, 'Straight from the fridge', 'Pick your favorite yoghurt and add toppings', 'vegetarian', 'https://images.unsplash.com/photo-1530259152377-3a014e1092e0?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2069&q=80')
recipe_repository.save(recipe1)
recipe3 = Recipe('Yoghurt', 10, 'Straight from the fridge', 'Pick your favorite yoghurt and add toppings', 'vegetarian', 'https://images.unsplash.com/photo-1530259152377-3a014e1092e0?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2069&q=80')
recipe_repository.save(recipe3)
recipe4 = Recipe('Yoghurt', 10, 'Straight from the fridge', 'Pick your favorite yoghurt and add toppings', 'vegetarian', 'https://images.unsplash.com/photo-1530259152377-3a014e1092e0?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2069&q=80')
recipe_repository.save(recipe4)
recipe5 = Recipe('Yoghurt', 10, 'Straight from the fridge', 'Pick your favorite yoghurt and add toppings', 'vegetarian', 'https://images.unsplash.com/photo-1530259152377-3a014e1092e0?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2069&q=80')
recipe_repository.save(recipe5)
recipe2 = Recipe('Noodles', 15, "Instant love", "Boil water Open up the package", 'meat', 'https://images.unsplash.com/photo-1553621043-f607bfbf6640?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1626&q=80')
recipe_repository.save(recipe2)
recipe6 = Recipe('Noodles', 15, "Instant love", "Boil water Open up the package", 'meat', 'https://images.unsplash.com/photo-1553621043-f607bfbf6640?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1626&q=80')
recipe_repository.save(recipe6)
recipe7 = Recipe('Noodles', 15, "Instant love", "Boil water Open up the package", 'meat', 'https://images.unsplash.com/photo-1553621043-f607bfbf6640?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1626&q=80')
recipe_repository.save(recipe7)
recipe8 = Recipe('Noodles', 15, "Instant love", "Boil water Open up the package", 'meat', 'https://images.unsplash.com/photo-1553621043-f607bfbf6640?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1626&q=80')
recipe_repository.save(recipe8)
recipe9 = Recipe('Noodles', 15, "Instant love", "Boil water Open up the package", 'meat', 'https://images.unsplash.com/photo-1553621043-f607bfbf6640?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1626&q=80')
recipe_repository.save(recipe9)
recipe10 = Recipe('Noodles', 15, "Instant love", "Boil water Open up the package", 'meat', 'https://images.unsplash.com/photo-1553621043-f607bfbf6640?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1626&q=80')
recipe_repository.save(recipe10)
recipe11 = Recipe('Noodles', 15, "Instant love", "Boil water Open up the package", 'meat', 'https://images.unsplash.com/photo-1553621043-f607bfbf6640?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1626&q=80')
recipe_repository.save(recipe11)
recipe12 = Recipe('Noodles', 15, "Instant love", "Boil water Open up the package", 'meat', 'https://images.unsplash.com/photo-1553621043-f607bfbf6640?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1626&q=80')
recipe_repository.save(recipe12)
recipe13 = Recipe('Noodles', 15, "Instant love", "Boil water Open up the package", 'meat', 'https://images.unsplash.com/photo-1553621043-f607bfbf6640?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1626&q=80')
recipe_repository.save(recipe13)
recipe14 = Recipe('Noodles', 15, "Instant love", "Boil water Open up the package", 'meat', 'https://images.unsplash.com/photo-1553621043-f607bfbf6640?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1626&q=80')
recipe_repository.save(recipe14)
recipe_ingredient1 = Recipe_ingredient(recipe1, ingredient1)
recipe_ingredient_repository.save(recipe_ingredient1)

recipe_ingredient2 = Recipe_ingredient(recipe2, ingredient2)
recipe_ingredient_repository.save(recipe_ingredient2)







pdb.set_trace()
