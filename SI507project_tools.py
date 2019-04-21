import os
import csv
import random
import json
from flask import Flask, render_template, session, redirect, url_for, request
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
				session.add(ingredient)
				session.commit()
				
			ingredientMap.append(ingredient)
		
		# Populate authors table
		author = rows[4]
		author_id = Recipe_Authors.query.filter_by(author_name=author).first()
		if not author_id:
			author_id = Recipe_Authors(author_name=author)
			session.add(author_id)
			session.commit()
	
		recipe_id = Recipe(recipes_name = rows[1].strip(), 
							directions = rows[10], 
							recipe_photo = rows[2], 
							review_count = rows[3], 
							total_time = rows[7], 
							prep_time = rows[5], 
							cook_time = rows[6], 
							author_id = author_id.author_id)
		session.add(recipe_id)
		session.commit()
	
		for i in ingredientMap:
			recipe = Recipe_Ingredients(recipe_id = recipe_id.recipe_id, ingredients_id = i.ingredients_id)
			session.add(recipe)
			session.commit()
		
## Main Source from SI507_project3.py
# Creating a function which searches through the database for duplicates and adds new recipe into the database
		
def addRecipeToDB(name, author, duration, directions, ingredients):
	response = {}
	message = ""
	if Recipe.query.filter_by(recipes_name=name).first():
		message = "This recipe already exists, please return to the main app."
	else:
		ingredients = ingredients.split(',') ### check this. 
		ingredientMap = []
		for i in ingredients: 
			ingredient = Ingredients.query.filter_by(ingredients_name=i).first()
			if not ingredient:
				ingredient = Ingredients(ingredients_name = i)
				session.add(ingredient)
				session.commit()
				
			ingredientMap.append(ingredient)
		
		# Populate authors table
		author_id = Recipe_Authors.query.filter_by(author_name=author).first()
		if not author_id:
			author_id = Recipe_Authors(author_name=author)
			session.add(author_id)
			session.commit()
	
		recipe_id = Recipe(recipes_name = name, 
							directions = directions,
							total_time = duration,
							author_id = author_id.author_id)
		session.add(recipe_id)
		session.commit()
		
		for i in ingredientMap:
			recipe = Recipe_Ingredients(recipe_id = recipe_id.recipe_id, ingredients_id = i.ingredients_id)
			session.add(recipe)
			session.commit()
		message = "Thank you! For Sharing A New Recipe."
		
	response["message"] = message
	
	return response

### Flask Routes (3 Flask Routes for the project requirements)

# Homepage with Table of Contents Route #1
@app.route('/')
def qrecipeshome(): 
    return render_template("index.html", title="QRecipes") 
    
# Listing the Database created for the recipes retained from csv - Route
@app.route('/qrecipes/search/<search_term>')
def recipesearch(search_term):
	response = {}
	response["recipes"] = []
	
	## Searching through the database and printing the information onto the page
	
	recipes = session.execute("SELECT * FROM recipes WHERE recipes_name LIKE '%{}%'".format(search_term))
	for recipe in recipes:
		authors = session.execute("SELECT * FROM recipe_authors WHERE author_id=={}".format(recipe.author_id))
		format_authors = []
		for author in authors: 
			format_authors.append(author.author_name)
		ingredients = session.execute("SELECT * FROM ingredients, recipe_ingredients WHERE recipe_ingredients.ingredients_id==ingredients.ingredients_id and recipe_ingredients.recipe_id=={}".format(recipe.recipe_id))
		format_ingredients = []
		for ingredient in ingredients: 
			format_ingredients.append(ingredient.ingredients_name)
			
		recipe_obj = {
			"title": recipe.recipes_name.replace("'",""),
			"recipenumber": recipe.author_id,
			"cooktime": recipe.total_time,
			"author": ', '.join(format_authors),
			"ingredients": ', '.join(format_ingredients),
			"directions": recipe.directions.replace("'","")
		} 
		response["recipes"].append(recipe_obj)
	return render_template("recipe_response.html", title="QRecipes: Results", recipes=response["recipes"], search_term=search_term)

# Form for user to submit new recipes into the database
@app.route('/qrecipes/addrecipe/')
def addrecipe():
	return render_template("addrecipe.html", title="QRecipes: Sharing") 

@app.route('/qrecipes/addreciperow', methods=["POST"])
def addreciperow():
	name = request.form["name"]
	author = request.form["author"]
	duration = request.form["duration"]
	directions = request.form["directions"]
	ingredients = request.form["ingredients"]
	response = addRecipeToDB(name, author, duration, directions, ingredients)
	return json.dumps(response)

# Created an additional function which tells the computer to go through the files allowing it not to be recreated over and over again
# when I am trying to design the flask.
if __name__ == '__main__':

	exists = os.path.isfile('Qrecipes.db')
	if not exists:
		db.create_all()
		recipesdata = get_csv()
		populate_db(recipesdata, session)
		
	app.run()


