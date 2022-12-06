from db.run_sql import run_sql

from models.recipes import Recipe
from models.ingredients import Ingredient


def save(recipe):
    sql ="INSERT INTO recipes (name, cooking_time, description, instructions, diet, image) VALUES (%s,%s,%s,%s,%s,%s) RETURNING id"
    values = [recipe.name, recipe.cooking_time, recipe.description, recipe.instructions, recipe.diet, recipe.image]
    results = run_sql(sql, values)
    recipe.id = results[0]['id']
    return recipe


def select_all():
    recipes = []
    sql = "SELECT * FROM recipes"
    results = run_sql(sql)

    for row in results:
        recipe = Recipe(row['name'], row['cooking_time'], row['description'], row['instructions'], row['diet'], row['image'], row['id'])
        recipes.append(recipe)
    return recipes


def select(id):
    recipe = None
    sql = "SELECT * FROM recipes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        recipe = Recipe(result['name'], result['cooking_time'], result['description'], result['instructions'], result['diet'], result['image'], result['id'] )
    return recipe

def delete_all():
    sql ="DELETE FROM recipes"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM recipes WHERE id = %s"
    values = [id]
    run_sql(sql, values)




def ingredients(recipe):
    ingredients = []
    sql = """SELECT ingredients.* FROM ingredients INNER JOIN recipe_ingredient ON recipe_ingredient.ingredient_id=ingredient.id WHERE recipe_id = %s"""
    values= [recipe.id]
    results = run_sql(sql, values)
  
    for row in results:
        ingredient=Ingredient(row['name'], row['amount'], row['id'])
        ingredients.append(ingredient)
    return ingredients

def update(recipe):
    sql = "UPDATE recipes SET (name, cooking_time, description, instructions, diet, image) = (%s,%s,%s,%s,%s,%s) WHERE id = %s"
    values = [recipe.name, recipe.cooking_time, recipe.description, recipe.instructions, recipe.diet, recipe.image, recipe.id]
    run_sql(sql, values)


