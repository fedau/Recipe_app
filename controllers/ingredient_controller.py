from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.ingredients import Ingredient

import repositories.ingredient_repository as ingredient_repository
ingredients_blueprint = Blueprint("ingredients", __name__)


@ingredients_blueprint.route("/ingredients")
def ingredients():
    ingredients = ingredient_repository.select_all()
    return render_template("ingredients/index.html", ingredients=ingredients)

# CREATE NEW RECIPE
# POST '/ingredients'

@ingredients_blueprint.route("/ingredients", methods=["POST"])
def save_ingredient():
    form_data = request.form
    ingredient_name = form_data['name']
    ingredient_amount = form_data['amount']
    new_ingredient = Ingredient(ingredient_name, ingredient_amount)
    ingredient_repository.save(new_ingredient)
    return redirect("/ingredients")
    





# SHOW 1 RECIPE????
# GET '/ingredients/<id>??????


# EDIT RECIPE????
# GET '/ingredients/<id>/edit'?????


# UPDATE ingredients???
# POST '/ingredients/<id>' (would normally be PUT)


# DELETE ingredients???
# DELETE '/ingredients/<id>/delete'