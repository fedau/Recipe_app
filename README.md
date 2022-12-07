This project is made for the CodeClan course week5 of python, Flask and  SQL.
This project makes a recipe website. It has a database where you can store recipes and ingredients. 
On the server side you will then be able to view the recipes edit and delte them. There is also a filter function alowing you to sort the page by diet and or ingredients you are looking for. You can add a recipe and add an ingredient if it is not in the list.  

# Recipe_app
python project for code clan
Built With

    HTML
    CSS
    Python
    Flask
    Postgresql

Getting Started
Prerequisites

To run this app, you must install:

    psychopg

    pip3 install psycopg2

    Flask

    pip3 install Flask

    Postgresql

Installation

    Clone the repository

    git clone https://github.com/fedau/Recipe_app

    Navigate to the folder using terminal
    
    Createdb recipe_manager

    psql -d recipe_manager -f db/recipe_manager.sql

    Seed the database with pre-set data by running the console.py file

    python3 console.py

    Run Flask

    flask run

    Open in browser (Google Chrome is recommended): http://127.0.0.1:5000
    To stop the server enter ctrl + c in your Terminal
