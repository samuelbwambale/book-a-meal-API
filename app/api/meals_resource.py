from flask_restplus import Resource,reqparse
from app.meals import Meal, meals
from app.menu import Menu , menus

for i in range(1,10):
    price = 1000 + i
    n = Meal(price,'something soemthing')
    meals.append(n)

class MealsResource(Resource):
    def get(self):
        return {
            'meals':  [{'id': meal.id, 'price': meal.price, 'description': meal.desc} for meal in meals]
        }

    def post(self):
        parser= reqparse.RequestParser()
        parser.add_argument('price',type=float,required=True,help='Price is required')
        parser.add_argument('description',type=str,required=True,help='Description is required')
        params = parser.parse_args()
        price = params['price']
        desc = params['description']

        meal = Meal(price=price,desc=desc)
        meal.addMeal()

        return {
            'meals':  [{'id': meal.id, 'price': meal.price, 'description': meal.desc} for meal in meals]
        }, 200

class MealResource(Resource):
    def put(self,meal_id):
        parser= reqparse.RequestParser()
        parser.add_argument('price',type=float,required=True)
        parser.add_argument('description',type=str,required=True)
        params = parser.parse_args()
        price = params['price']
        desc = params['description']
        for meal in meals:
           if meal['id'] == meal_id:
               meal['desc'] = desc
               meal['price'] = price
               return {'meals': {'id': meal.id, 'price': meal.price, 'description': meal.desc}}

    def delete(self, meal_id):
        for meal in meals:
           if meal['id'] == meal_id:
               meal.deleteMeal()
               return {
            'meals':  [{'id': meal.id, 'price': meal.price, 'description': meal.desc} for meal in meals]
        }, 200

menus = [
    {'id': 222, 
    'date': "2018-04-24 10:30:55.423844", 
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
    'date': "2018-04-26 10:40:11.423844", 
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

class MenuResource(Resource):
    def post(self)
        parser= reqparse.RequestParser()
        parser.add_argument('date',type=date,required=True)
        parser.add_argument('meals',type=list,required=True)
        params = parser.parse_args()
        date = params['date']
        meals = params['meals']
        menu = Menu(date=date.today(), meals = [{
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
            "id": 1, 
            "description": 1003
        }] )
        menu.addMenu()
        return {
             'menus':  [{'id': menu.id, 'date': menu.date, 'meals': menu.meals} for menu in menus]
        }, 200


    


