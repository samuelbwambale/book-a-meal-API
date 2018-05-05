import unittest
import json
from app import app
from app.models.meals import Meal, meals, get_meal_by_id

class MealsApiTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_addMeal(self):
        meal = {
            "id": 21,
            "desc": "Beans with rice",
            "price": 20000 
        }
        response = self.app.post("/api/v1/meals",\
        data=json.dumps(meal), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_deleteMeal(self):
        meal ={"price": 23456, "desc":"Mulokony and cassava", "id": 25}
        meals.append(meal)
        for meal in meals:
            if meal['price'] == 23456: 
                return meal 
        res = meals.remove(meal)
        self.assertTrue(res,True)

    def test_addMeal_with_wrong_values(self):
        meal = {"price": 23456, "desc":"Mulokony and cassava", "id": "kkk"}
        response = self.app.post("/api/v1/meals",\
        data=json.dumps(meal), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_get_meal_by_id(self):
        mymeal ={"price": 24000, "desc":"Mulokony and cassava", "id": 240}
        meals.append(mymeal)
        mymeal2 = get_meal_by_id(240)
        self.assertEqual(mymeal2['price'], 24000)

