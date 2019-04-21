import sqlite3
import unittest

### Will change the strings later this week >>> Source Credit: SI507_HW05_TestCase

class SI507FinalProjectTesting(unittest.TestCase):

	def setUp(self):
		self.conn = sqlite3.connect("./Qrecipes.db") # Connecting to database that should exist in autograder
		self.cur = self.conn.cursor()

	def test_for_recipes_table(self):
		self.cur.execute("select recipes_name, directions, recipe_photo, review_count, total_time, prep_time, cook_time, author_id from recipes where recipes_name='Mocha Chocolate Chip Banana Muffins Recipe'")
		data = self.cur.fetchone()
		self.assertEqual(data,('Mocha Chocolate Chip Banana Muffins Recipe', 'Preheat oven to 350 degrees F (175 degrees C).**Blend butter or margarine, sugar, egg, banana, dissolved coffee, and vanilla in food processor for 2 minutes. Add flour, salt, baking powder, and soda, and blend just until flour disappears. Add chocolate chips and mix in with wooden spoon. Spoon mixture into 15 to 18 paper-lined muffin cups.**Bake for 25 minutes.  Cool on wire racks.**', 'https://images.media-allrecipes.com/userphotos/560x315/1334257.jpg', 579, '35 m', '10 m', '25 m', 1), "Testing data that results from selecting recipes_name Mocha Chocolate Chip Banana Muffins Recipe")

	def test_for_ingredients_table(self):
		self.cur.execute("select ingredients_id, ingredients_name from ingredients where ingredients_name='margarine'")
		data = self.cur.fetchone()
		self.assertEqual(data,(1, 'margarine'), "Testing data from ingredients_name margarine")
		
	def test_for_recipeauthors_table(self):
		self.cur.execute("select author_id, author_name from recipe_authors where author_name='Jan Bittner'")
		data = self.cur.fetchone()
		self.assertEqual(data,(2, 'Jan Bittner'), "Testing data from recipe_authors Jan Bittner")
	
	def test_for_addrecipes_table(self):
		addrecipe = ('SI507FinalProject', 'Submission', '25 m')
		self.cur.execute("insert into recipes(recipes_name, directions, total_time) values (?, ?, ?)", addrecipe)
		self.conn.commit()

		self.cur.execute("select recipes_name, directions, total_time from recipes where recipes_name='SI507FinalProject'")
		data = self.cur.fetchone()
		self.assertEqual(data, addrecipe, "Testing another select statement after a sample insertion")

	def test_for_recipes_table(self):
		res = self.cur.execute("select * from recipes")
		data = res.fetchall()
		self.assertTrue(data, 'Testing that you get a result from making a query to the recipes table')

	def tearDown(self):
		self.conn.commit()
		self.conn.close()


if __name__ == '__main__':
	unittest.main(verbosity=2)