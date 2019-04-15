# SI507W19 Final Project

Angela Chih

[Link to this repository](https://github.com/ahcdesign/SI507W19FinalProject)

---

## Project Description

My project "QRecipes" will collect recipes and gather the information and select all the 
recipes with the shortest duration and at least a vegetable is included in the recipe. 
As a graduate student I would like the option to either meal prep or have a night in to 
de-stress but not take too long to cook as I still have a lot of work to do. The main page 
of the Flask route will be the Table of Contents leading to two other Flask routes of meal 
prepping and quick de-stressor meals. The project will allow users to look for recipes 
they can use for themselves to either meal prep or quick de-stressor.  

## How to run

1. First, you should ... (e.g. install all requirements with `pip install -r requirements.txt`)
2. Second, you should ... (e.g. run `python programname.py runserver` or whatever else is appropriate)
3. Anything else

## How to use

1. A useful instruction goes here
2. A useful second step here
3. (Optional): Markdown syntax to include an screenshot/image: ![alt text](image.jpg)

## Routes in this application
- `/home` -> this is the home page containing a Table of Contents for the 
- `/MealPrep` -> This route will show a list of healthy recipes that can be prepped for a 
week, simple and fast to cook. It will also have a return button for accessibility to 
return to the homepage. 
- `/QuickMeal` -> This route will show a list of quick recipes with more ingredients but 
the duration will still be the same as the meal prep. 
- `/home/<username>` -> The homepage will also take the input of a name and show a greeting

## How to run tests
1. First... (e.g. access a certain directory if necessary)
2. Second (e.g. any other setup necessary)
3. etc (e.g. run the specific test file)
NOTE: Need not have 3 steps, but should have as many as are appropriate!

## In this repository:
- Directory Name
  - File in directory
  - File in directory
- File name
- File name

---
## Code Requirements for Grading
Please check the requirements you have accomplished in your code as demonstrated.
- [x] This is a completed requirement.
- [ ] This is an incomplete requirement.

Below is a list of the requirements listed in the rubric for you to copy and paste.  See rubric on Canvas for more details.

### General
- [ ] Project is submitted as a Github repository
- [ ] Project includes a working Flask application that runs locally on a computer
- [ ] Project includes at least 1 test suite file with reasonable tests in it.
- [ ] Includes a `requirements.txt` file containing all required modules to run program
- [ ] Includes a clear and readable README.md that follows this template
- [ ] Includes a sample .sqlite/.db file
- [ ] Includes a diagram of your database schema
- [ ] Includes EVERY file needed in order to run the project
- [ ] Includes screenshots and/or clear descriptions of what your project should look like when it is working

### Flask Application
- [ ] Includes at least 3 different routes
- [ ] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
- [ ] Interactions with a database that has at least 2 tables
- [ ] At least 1 relationship between 2 tables in database
- [ ] Information stored in the database is viewed or interacted with in some way

### Additional Components (at least 6 required)
- [ ] Use of a new module
- [ ] Use of a second new module
- [ ] Object definitions using inheritance (indicate if this counts for 2 or 3 of the six requirements in a parenthetical)
- [ ] A many-to-many relationship in your database structure
- [ ] At least one form in your Flask application
- [ ] Templating in your Flask application
- [ ] Inclusion of JavaScript files in the application
- [ ] Links in the views of Flask application page/s
- [ ] Relevant use of `itertools` and/or `collections`
- [ ] Sourcing of data using web scraping
- [ ] Sourcing of data using web REST API requests
- [ ] Sourcing of data using user input and/or a downloaded .csv or .json dataset
- [ ] Caching of data you continually retrieve from the internet in some way

### Submission
- [ ] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
- [ ] I included a summary of my project and how I thought it went **in my Canvas submission**!
