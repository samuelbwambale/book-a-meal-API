import unittest
from app import app
from app.meals import meals, Meal




class ApiTestCase(unittest.TestCase):
    def test_addMeal(self):
        meal = Meal(desc="Matooke and Rice", price = 20000)
        result = meal.addMeal()
        self.assertTrue(result,True)
        
    def test_deleteMeal(self):
        # for meal in meals:
        #    if meal['id'] == meal_id:
        #         self.assertEqual(meal.deleteMeal(), True)
        pass
        

    

