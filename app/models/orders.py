from app.models.users import User, users
from app.models.meals import Meal, get_meal_by_id


orders = [
        {
      "id": 101,
      "meals": [
    {
      "id": 21,
      "desc": "Beans with rice",
      "price": 20000},
    {
      "id": 23,
      "desc": "Minced meat with pasta",
      "price": 14000 }
    ]
    },
    {
      "id": 104,
      "meals": [
    {
      "id": 21,
      "desc": "Beans with rice",
      "price": 20000}
    ]
    }
]

def get_order_by_id(order_id):
    for order in orders:
        if order['id'] == order_id: 
            return order

class Order:
    count = 0
    def __init__(self, user, meals):
        self.id = Order.count + 1
        self.meals = []
        self.user = user

    def deleteOrder(self):
        orders.remove(self)

    def addOrder(self):
        orders.append(self)

    def add_meal_to_order(self, meal_id):
        selected_meal = get_meal_by_id(meal_id)
        self.meals.append(selected_meal)

    def to_dict(self):
        return {
            'id': self.id,
            'user': self.user.to_dict(),
            'meals': [meal.to_dict() for meal in self.meals]
        }




