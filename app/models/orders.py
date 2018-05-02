orders = [
        {
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
    }
]

def get_order_by_id(order_id):
    for order in orders:
        if order['id'] == order_id: 
            return order

class Order:
    count = 0
    def __init__(self, meals):
        Order.count += 1
        self.id = Order.count
        self.meals = []

    def deleteOrder(self):
        orders.remove(self)

    def addOrder(self):
        orders.append(self)

    def to_dict(self):
        return {
            'id': self.id,
            'meals': [meal.to_dict() for meal in self.meals]
        }




