import unittest
import json
from app import app
from app.models.orders import Order, orders, get_order_by_id
from app.models.meals import Meal, meals
from app.models.users import User


class OrdersApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()


    def test_addOrder(self):
        order = {
                "id": 104,
                "user": {"username": "kongolo", "password": "pwdkkk", "isAdmin": False},
                "meals": [
                        {"id": 21,
                        "desc": "Beans with rice",
                        "price": 20000},
                        {"id": 26,
                        "desc": "Beans with matooke",
                        "price": 10000}]
                }
        response = self.app.post("/api/v1/orders",
        data=json.dumps(order), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_order_by_id(self):
        order = {
                "id": 104,
                "user": {"username": "kongolo", "password": "pwdkkk", "isAdmin": False},
                "meals": [
                        {"id": 21,
                        "desc": "Beans with rice",
                        "price": 20000},
                        {"id": 26,
                        "desc": "Beans with matooke",
                        "price": 10000}]
                }
        orders.append(order)
        my_order = get_order_by_id(104)
        res = False
        for order in orders:
            if order['id'] == 104: 
                return True
        self.assertEqual(res, True)


 


    
