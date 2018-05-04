import unittest
import json
from app import app
from app.models.menu import Menu, menus, get_menu_by_id
from app.models.meals import Meal, meals, get_meal_by_id


class MenusApiTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()    


    def test_get_meal_by_id(self):
        mymeal = get_meal_by_id(22)
        self.assertEqual(mymeal['price'], 12000)


    def test_post_a_menu(self):
        menu = {
                "id": 111,
                'forToday': True,
                "meals": [
                        {"id": 21,
                        "desc": "Beans with rice",
                        "price": 20000},
                        {"id": 26,
                        "desc": "Beans with matooke",
                        "price": 10000} ]
                }

        """ Test setting up a menu """
        response = self.app.post("/api/v1/menu",
        data=json.dumps(menu), content_type='application/json')
        self.assertEqual(response.status_code, 200)
    
    def test_get_menu_of_the_day(self):
        available = False
        for menu in menus:
            if menu['forToday'] == True: 
                available = True
                break
        self.assertTrue(available,True)


    def test_getAllMenus(self):
        response = self.app.get('/api/v1/menus', content_type = 'application/json')
        self.assertEqual(response.status_code, 200)

