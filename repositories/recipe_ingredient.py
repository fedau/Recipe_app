from db.run_sql import run_sql
from models.recipe_ingredient import Recipe_ingredient


import repositories.ingredient_repository as ingredient_repository
import repositories.recipe_repository as recipe_repository

def save(recipe_ingredient):
    sql = "INSERT INTO recipe_ingredient (recipe_id, ingredient_id) VALUES (%s, %s) RETURNING id"
    values = [recipe_ingredient.recipe_id, recipe_ingredient.ingredient_id]
    results = run_sql(sql, values)
    recipe_ingredient.id = results[0]['id']
    return recipe_ingredient

# WHAT AM I DOINNGGGGGG

def select(id):
    recipe_ingredient = None
    sql = "SELECT * FROM recipe_ingredients WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        recipe_ingredient = Recipe_ingredient(result['recipe_id'], result['ingredient_id'], result['id'] )
    return recipe_ingredient



def select_all():
    recipes_ingredients = []
    sql = "SELECT * FROM recipe_ingredient"
    results = run_sql(sql)
    for row in results:
        recipe = recipe_repository.select(row['recipe_id'])
        ingredient = ingredient_repository.select(row['ingredient_id'])
        recipe_ingredient = Recipe_ingredient(recipe.id, ingredient.id, row['id'])
        recipes_ingredients.append(recipe_ingredient)
    return recipes_ingredients

def select_all_by_recipe_id(id):
    recipes_ingredients = []
    sql = "SELECT * FROM recipe_ingredient WHERE recipe_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        recipe = recipe_repository.select(row['recipe_id'])
        ingredient = ingredient_repository.select(row['ingredient_id'])
        recipe_ingredient = Recipe_ingredient(recipe.id, ingredient.id, row['id'])
        recipes_ingredients.append(recipe_ingredient)
    return recipes_ingredients


def delete_all():
    sql ="DELETE FROM recipe_ingredient"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM recipe_ingredient WHERE id = %s"
    values = [id]
    run_sql(sql, values)
