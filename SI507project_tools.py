import os
import csv
import random
from flask import Flask, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Creating Database for the Recipes using SI507_Project2 code
# Application configurations >> taken from main_app_SOLUTION.py

app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./Qrecipes.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy

###Setting up the Models###

class Recipe_Authors(db.Model):
	__tablename__="recipe_authors"
	author_id = db.Column(db.Integer, primary_key=True)
	author_name = db.Column(db.String(65))

class Ingredients(db.Model):	
	__tablename__="ingredients"
	ingredients_id = db.Column(db.Integer, primary_key=True)
	ingredients_name = db.Column(db.String(65))

class Recipe(db.Model):
	__tablename__="recipes"
	recipe_id = db.Column(db.Integer, primary_key=True)
	recipes_name = db.Column(db.String(65))
	directions = db.Column(db.String(65))
	recipe_photo = db.Column(db.String(65))
	review_count = db.Column(db.Integer)
	total_time = db.Column(db.String(65))
	prep_time = db.Column(db.String(65))
	cook_time = db.Column(db.String(65))
	author_id = db.Column(db.Integer, db.ForeignKey('recipe_authors.author_id'))

class Recipe_Ingredients(db.Model):	
	__tablename__="recipe_ingredients"
	mapping_id = db.Column(db.Integer, primary_key=True)
	recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'))
	ingredients_id = db.Column(db.Integer, db.ForeignKey('ingredients.ingredients_id'))

##### Helper functions #####
### For database additions
### Relying on global session variable above existing

def get_or_create_director(director_name):
	director = Director.query.filter_by(name=director_name).first()
	if director: 
		return director
	else:
		director = Director(name=director_name)
		session.add(director)
		session.commit()
		return director

## Populating Database for all Tables

def get_csv():
	recipesdata = open("recipes_cleaned.csv", "r")
	csv_recipesdata = csv.reader(recipesdata, delimiter=';')
	next(csv_recipesdata, None)
	return csv_recipesdata

def populate_db(csv_recipesdata, session):
	for rows in csv_recipesdata: 

		# Populate Ingredients Table
		ingredients = rows[8].split(',') ### check this. 
		ingredientMap = []
		for i in ingredients: 
			ingredient = Ingredients.query.filter_by(ingredients_name=i).first()
			if not ingredient:
				ingredient = Ingredients(ingredients_name = i)
			ingredientMap.append(ingredient)
		
		# Populate authors table
		author = rows[4]
		author_id = Recipe_Authors.query.filter_by(author_name=i).first()
		if not author_id:
			author_id = Recipe_Authors(author_name=author)
	
		recipe_id = Recipe(recipe_id = rows[0], 
							recipes_name = rows[1], 
							directions = rows[10], 
							recipe_photo = rows[2], 
							review_count = rows[3], 
							total_time = rows[7], 
							prep_time = rows[5], 
							cook_time = rows[6], 
							author_id = author_id.author_id)
	
		for i in ingredientMap:
			Recipe_Ingredients(recipe_id = recipe_id.recipe_id, ingredients_id = i.ingredients_id)
		
		session.commit()
###Setting up the Controllers (route functions)###



# Flask Routes (3 Flask Routes for the project requirements)

# Homepage with Table of Contents Route #1

# Listing the Database created for the recipes retained from csv - Route


if __name__ == '__main__':
	db.create_all()
	recipesdata = get_csv()
	populate_db(recipesdata, session)
	app.run()


