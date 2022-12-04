from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.recipes import Recipe
import repositories.recipe_repository as recipe_repository

recipes_blueprint = Blueprint("recipes", __name__)

@recipes_blueprint.route("/recipes")
def recipes():
    recipes = recipe_repository.select_all()
    return render_template("recipes/index.html", recipes=recipes)

@recipes_blueprint.route("/recipes/new")
def new_recipe():
    recipes = recipe_repository.select_all()
    return render_template("recipes/new_recipe.html", recipes=recipes)