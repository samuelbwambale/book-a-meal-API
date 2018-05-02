import unittest
import json
from app import app
from app.models.orders import Order, get_order_by_id

orders = [{
      "id": 101,
      "meals": [
    {
      "id": 21,
      "desc": "Beans with rice",
      "price": 20000    },
    {
      "id": 23,
      "desc": "Minced meat with pasta",
      "price": 14000    }
    ]
    },
    {
      "id": 104,
      "meals": [
    {
      "id": 21,
      "desc": "Beans with rice",
      "price": 20000    }
    ]
    }]

class OrdersApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_addOrder(self):
        order = {
                "id": 104,
                "meals": [
                        {"id": 21,
                        "desc": "Beans with rice",
                        "price": 20000},
                        {"id": 26,
                        "desc": "Beans with matooke",
                        "price": 10000} ]
                }

        """ Test adding new meal on API """
        response = self.app.post("/api/v1/orders",\
        data=json.dumps(order), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_deleteOrder(self):
        ord = get_order_by_id(101)
        res = ord.deleteOrder()
        self.assertTrue(res,True)

        

    
