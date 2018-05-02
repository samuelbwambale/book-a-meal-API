import unittest
import json
from app import app
from app.models.menu import Menu, get_menu_by_id


menus = [
    {'id': 222,
     'forToday': False,
     'meals': [{
         "price": "something soemthing",
         "id": 8,
         "description": 1001
     },
         {
         "price": "something soemthing",
         "id": 9,
         "description": 1002
     },
         {
         "price": "something soemthing",
         "id": 15,
         "description": 1003
     }]},

    {'id': 111,
     'forToday': True,
     'meals': [{
             "price": "something soemthing",
             "id": 3,
         "description": 1001
     },
         {
         "price": "something soemthing",
         "id": 18,
         "description": 1002
     },
         {
         "price": "something soemthing",
         "id": 20,
         "description": 1003
     }]}
]

class MenusApiTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    
    def test_setMenu(self):
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
        response = self.app.post("/api/v1/menu",\
        data=json.dumps(menu), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_getAllMenus(self):
        response = self.app.get('/api/v1/menus', content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
