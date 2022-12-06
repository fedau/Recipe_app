from flask import Flask, render_template
from controllers.ingredient_controller import ingredients_blueprint
from controllers.recipe_controller import recipes_blueprint
# from controllers.recipe_ingredient_controller import recipes_ingredient_blueprint

app = Flask(__name__)

app.register_blueprint(ingredients_blueprint)
app.register_blueprint(recipes_blueprint)
# app.register_blueprint(recipes_ingredient_blueprint)

@app.route('/')
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)