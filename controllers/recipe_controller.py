from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.recipes import Recipe
import repositories.recipe_repository as recipe_repository

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
    return render_template("recipes/new_recipe.html", recipes=recipes)

# CREATE NEW RECIPE
# POST '/recipes'

# SHOW 1 RECIPE
# GET '/recipes/<id>


# EDIT RECIPE
# GET '/recipes/<id>/edit'


# UPDATE RECIPES
# POST '/recipes/<id>' (would normally be PUT)


# DELETE RECIPES
# DELETE '/recipes/<id>/delete'