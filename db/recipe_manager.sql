DROP TABLE IF EXISTS recipe_ingredient;
DROP TABLE IF EXISTS recipes;
DROP TABLE IF EXISTS ingredients;


CREATE TABLE recipes(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    cooking_time INT,
    description VARCHAR(255),
    instructions TEXT,
    diet VARCHAR(255),
    image VARCHAR(255)
);



CREATE TABLE ingredients(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    amount INT
);


CREATE TABLE recipe_ingredient(
    id SERIAL PRIMARY KEY,
    recipe_id INT REFERENCES recipes(id) ON DELETE CASCADE,
    ingredient_id INT REFERENCES ingredients(id) ON DELETE CASCADE

);


INSERT INTO recipes(name,cooking_time,description,instructions,diet,image) VALUES ('macaroni', 20, 'gooey cheese', 'cook pasta then make sauce bake for 20 muinst', 'vegetarian', 'macaroni image here');
insert INTO ingredients (name, amount) VALUES ('cheese', 100);
INSERT INTO ingredients(name, amount) VALUES ('pasta', 200);
INSERT INTO recipe_ingredient(recipe_id, ingredient_id) VALUES (1,2);
