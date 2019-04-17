import csv
import random

## Using SI507_HW4.py for assistance on cleaning cached data

recipesdata = open("Data/clean_recipes.csv", "r")
csv_recipesdata = csv.reader(recipesdata, delimiter=';') ## The delimiter is included because the data is separated with semicolons for the table
next(csv_recipesdata, None) ## This deletes the row with the column titles

# Creating a different version of the recipes data to fit the goals and milestones of my project

cleaned_recipes = open("recipes_cleaned.csv", "w")
cleaned_recipes.write("Recipe ID;Recipe Name;Recipe Photo;Total Reviews;Author;Prep Time;Cook Time;Total Time;Ingredients;Total Ingredients;Description\n")
write_object = csv.writer(cleaned_recipes, delimiter=';')

# Rearranging the data from Data/clean_recipes.csv - there should be an empty column for "Total Ingredients"

for rows in csv_recipesdata:
#  	print(rows[9])
	blankvalue = ""
	newrows = [rows[9],rows[0],rows[2],rows[1],rows[3],rows[4],rows[5],rows[6],rows[7],"",rows[8]]
	
	# Selecting the "Total Time" and omitting recipes with a "Total Time" of more than 45 minutes
	if "h" in newrows[7] or "d" in newrows[7] or "X" in newrows[7]:
		continue
	minstrip = newrows[7].replace("m","")
	if int(minstrip) >= 45: 
		continue
	# Changing the "1k" into a numerator in order for the database to be the same
	newrows[3] = newrows[3].replace("k","000")
	
	# Selecting the Ingredients column and writing a function that counts each word and printed out to the "Total Ingredients" as integers
	
	newrows[9] = str(len(newrows[8].split(",")))
# 	print(newrows[9])
	
	write_object.writerow(newrows)

cleaned_recipes.close()
