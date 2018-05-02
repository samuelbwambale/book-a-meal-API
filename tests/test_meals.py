import unittest
import json
from app import app
from app.models.meals import Meal, get_meal_by_id

meals = []

class MealsApiTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_addMeal(self):
        meal = {
            "id": 21,
            "desc": "Beans with rice",
            "price": 20000 
        }

        """ Test adding new meal on API """
        response = self.app.post("/api/v1/meals",\
        data=json.dumps(meal), content_type='application/json')
        self.assertEqual(response.status_code, 201)



    def test_deleteMeal(self):
        meal = Meal(desc="Matooke and Rice", price = 20000)
        meal.addMeal()
        for meal in meals:
            if meal['price'] == 20000: 
                return meal 
        res = meal.deleteMeal
        self.assertTrue(res,True)

    def test_addMeal_with_wrong_values(self):
        """ add price as string instead of int """

        meal = Meal(desc="Matooke and Rice", price="kkk")
        result = meal.addMeal()
        self.assertTrue(result,False)

    def test_updateMeal(self):
        meal = {
            "id": 21,
            "desc": "Beans with rice",
            "price": 100000 
        }
        response = self.app.put("/api/v1/meals/21",\
        data=json.dumps(meal), content_type='application/json')
        self.assertEqual(response.status_code, 201)





    


    

