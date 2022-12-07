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
@recipes_blueprint.route("/")
def recipes():
    recipes = recipe_repository.select_all()
    return render_template("/index.html", recipes=recipes)

@recipes_blueprint.route("/recipes")
def recipes_filter():
    recipes = recipe_repository.select_all()
    ingredients = ingredient_repository.select_all()
    return render_template("recipes/index.html", recipes=recipes, ingredients=ingredients)


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
    return render_template('/recipes/show.html', single_recipe=single_recipe, ingredients=ingredient_instances)


# EDIT RECIPE
# GET '/recipes/<id>/edit'
@recipes_blueprint.route('/recipes/<int:id>/edit')
def edit_recipes(id):
    recipe = recipe_repository.select(id)
    ingredients = ingredient_repository.select_all()
    recipe_ingredient = [recipe_ingredient.ingredient_id for recipe_ingredient in recipe_ingredient_repository.select_all_by_recipe_id(id)]
    return render_template('/recipes/edit.html', single_recipe=recipe, ingredients=ingredients, recipe_ingredient=recipe_ingredient)



# UPDATE RECIPES
# POST '/recipes/<id>' (would normally be PUT)
@recipes_blueprint.route("/recipes/<int:id>", methods=["POST"])
def update_recipe(id):
    form_data = request.form
    recipe_name = form_data['name']
    recipe_description = form_data['description']
    recipe_cooking_time = form_data['cooking_time']
    recipe_instructions = form_data['instructions']
    recipe_image = form_data['image']
    recipe_diet = form_data['diet']

    # get from form data ingredients that are picked (use getlist())

    # get the get from recipe_ingredient_repository before editing (to see what ingredients were already ticked)

    # generate list of ingredients that are no longer ticked in the form data but were ticked in the repository query 
    # and delete from recipe_ingredients table

    # generate a list of ingredients that are now ticked and weren't before and add these to the recipes table

    # see that everything is still the same if not changed 
    




    updated_recipe = Recipe(recipe_name, recipe_cooking_time, recipe_description, recipe_instructions, recipe_diet, recipe_image, id)
    recipe_repository.update(updated_recipe)    
    return redirect(f"/recipes/{updated_recipe.id}")


# DELETE RECIPES
# DELETE '/recipes/<id>/delete'

@recipes_blueprint.route("/recipes/<id>/delete", methods=['POST'])
def delete_recipe(id):
    recipe_repository.delete(id)
    return redirect('/recipes')

@recipes_blueprint.route("/recipes/filtered", methods=['POST'])
def filter_recipes():
    ingredients = ingredient_repository.select_all()
    form_data = request.form
    filtered_recipe_list = set()
    recipe_ingredients = recipe_ingredient_repository.select_all()
    recipes = recipe_repository.select_all()
    recipe_lookup = {recipe.id: recipe for recipe in recipes}
    selected_filter_diet = form_data.getlist('diet')
    selected_filter_ingredients = [int(i) for i in form_data.getlist('ingredient')]
    for recipe in recipes:

        if recipe.diet in form_data.getlist('diet'):
            filtered_recipe_list.add(recipe)

    for recipe_ingredient in recipe_ingredients:
        if recipe_ingredient.ingredient_id in selected_filter_ingredients:
            filtered_recipe_list.add(recipe_lookup[recipe_ingredient.recipe_id])

    return render_template("/recipes/index.html", recipes = list(filtered_recipe_list), ingredients=ingredients, selected_filter_diet=selected_filter_diet, selected_filter_ingredients=selected_filter_ingredients )

