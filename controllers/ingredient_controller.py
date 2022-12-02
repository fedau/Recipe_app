from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.ingredients import Ingredient

import repositories.ingredient_repository as ingredient_repository
ingredients_blueprint = Blueprint("ingredients", __name__)


@ingredients_blueprint.route("/ingredients")
def ingredients():
    ingredients = ingredient_repository.select_all()
    return render_template("ingredients/index.html", ingredients=ingredients)