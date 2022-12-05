from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.recipes import Recipe
import repositories.recipe_repository as recipe_repository
import repositories.ingredient_repository as ingredient_repository
import repositories.recipe_ingredient as recipe_ingredient_repository
import pdb

recipes_ingredient_blueprint = Blueprint('recipe_ingredient', __name__)
# CREATE NEW RECIPE
# POST '/recipes'

# SHOW 1 RECIPE
# GET '/recipes/<id>

# WHAT AM I DOINNGGGGGG

@recipes_ingredient_blueprint.route('/recipes/<id>' , methods=['GET'])
def show_page():
    recipe = recipe_repository.select_all()
    ingredients = ingredient_repository.select_all()
    # recipe_ingredient = recipe_ingredient_repository.select_all()
    return render_template('recipes/show.html', recipe=recipe, ingredients=ingredients)

# EDIT RECIPE
# GET '/recipes/<id>/edit'


# UPDATE RECIPES
# POST '/recipes/<id>' (would normally be PUT)

# DELETE RECIPES
# DELETE '/recipes/<id>/delete'