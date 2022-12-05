from db.run_sql import run_sql
from models.ingredients import Ingredient
from models.recipes import Recipe


def save(ingredient):
    sql = "INSERT INTO ingredients (name, amount) VALUES (%s, %s) RETURNING id"
    values = [ ingredient.name, ingredient.amount]
    results = run_sql(sql, values)
    ingredient.id = results[0]['id']
    return ingredient

def select_all():
    ingredients = []
    sql = " SELECT * FROM ingredients"
    results = run_sql(sql)
    for row in results:
        ingredient = Ingredient(row['name'], row['amount'], row['id'])
        ingredients.append(ingredient)
    return ingredients



def select(id):
    ingredient = None
    sql = "SELECT * FROM ingredients WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        ingredient = Ingredient(result['name'], result['amount'], result['id'] )
    return ingredient

def delete_all():
    sql = "DELETE FROM ingredients"
    run_sql(sql)


def recipes(ingredient):
    recipes = []
    sql = """SELECT recipes.* FROM recipes INNER JOIN recipe_ingredient ON recipe_ingredient.recipe_id = recipes.id WHERE ingredient_id = %s"""
    values = [ingredient.id]
    results = run_sql(sql, values)
    for row in results:
        recipe = Recipe(row['name'], row['cooking_time'], row['description'], row['instructions'], row['diet'], row['image'], row['id'])
        recipes.append(recipe)
    return recipes


