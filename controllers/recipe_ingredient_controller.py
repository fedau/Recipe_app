# CREATE NEW RECIPE
# POST '/recipes'

# SHOW 1 RECIPE
# GET '/recipes/<id>


# EDIT RECIPE
# GET '/recipes/<id>/edit'


# UPDATE RECIPES
# POST '/recipes/<id>' (would normally be PUT)
@recipes_blueprint.route("/recipes", methods=["POST"])
def save_recipe():
    form_data = request.form
    recipe_name = form_data['name']
    recipe_description = form_data['description']
    recipe_cooking_time = form_data['cooking_time']
    recipe_instructions = form_data['instructions']
    # ingredients_id =?????
    recipe_image = form_data['image']

    new_recipe = Recipe(recipe_name, recipe_description,recipe_cooking_time, recipe_instructions, recipe_image)
    recipe_repository.save(new_recipe)
    return redirect("/recipes")
    


# DELETE RECIPES
# DELETE '/recipes/<id>/delete'