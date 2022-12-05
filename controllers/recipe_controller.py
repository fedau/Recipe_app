from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.recipes import Recipe
from models.ingredients import Ingredient
from models.recipe_ingredient import Recipe_ingredient
import repositories.recipe_repository as recipe_repository
import repositories.ingredient_repository as ingredient_repository
import repositories.recipe_ingredient as recipe_ingredient_repository

import pdb

recipes_blueprint = Blueprint("recipes", __name__)

# INDEX
# GET /RECIPES
@recipes_blueprint.route("/recipes")
def recipes():
    recipes = recipe_repository.select_all()
    return render_template("recipes/index.html", recipes=recipes)


# NEW RECIPE
# GET '/recipes/new'
@recipes_blueprint.route("/recipes/new")
def new_recipe():
    recipes = recipe_repository.select_all()
    ingredients = ingredient_repository.select_all()
    return render_template("recipes/new_recipe.html", recipes=recipes, ingredients=ingredients)

# CREATE NEW RECIPE
# POST '/recipes'

@recipes_blueprint.route("/recipes", methods=["POST"])
def save_recipe():
    form_data = request.form
    recipe_name = form_data['name']
    recipe_description = form_data['description']
    recipe_cooking_time = form_data['cooking_time']
    recipe_instructions = form_data['instructions']
    recipe_image = form_data['image']
    recipe_diet = form_data['diet']
    new_recipe = Recipe(recipe_name, recipe_cooking_time, recipe_description, recipe_instructions, recipe_diet, recipe_image)
    recipe_repository.save(new_recipe)
    all_ingredients = ingredient_repository.select_all()
    ingredient_picks = {}
    counter = 0
    for ingredient in all_ingredients:
        ingredient_picks[ingredient.name] = ingredient.id
        counter += 1
    # ingredient_pick_names = list(ingredient_picks.values())
    all_form_data_keys = form_data.keys()
    for  key in all_form_data_keys:
        if key in ingredient_picks:
            for item in all_ingredients:
                if item.name == key:
                    ingredient_id = item.id
                    new_recipe_ingredient = Recipe_ingredient(new_recipe.id, ingredient_id)
                    recipe_ingredient_repository.save(new_recipe_ingredient)

    # pdb.set_trace()
    
    return redirect("/recipes")

# SHOW 1 RECIPE
# # GET '/recipes/<id>
@recipes_blueprint.route('/recipes/<int:id>')
def show(id):
    single_recipe = recipe_repository.select(id)
    # ingredients = recipe_repository.ingredients(single_recipe)
    recipe_ingredients = recipe_ingredient_repository.select_all_by_recipe_id(id)
    ingredient_instances = []
    for item in recipe_ingredients:
        new_ingredient = ingredient_repository.select(item.ingredient_id)
        ingredient_instances.append(new_ingredient)
    # recipe = recipe_repository.select_all()
    return render_template('recipes/show.html', single_recipe=single_recipe, ingredients=ingredient_instances)


# EDIT RECIPE
# GET '/recipes/<id>/edit'



# UPDATE RECIPES
# POST '/recipes/<id>' (would normally be PUT)


# DELETE RECIPES
# DELETE '/recipes/<id>/delete'