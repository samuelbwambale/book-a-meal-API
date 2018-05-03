from flask_restplus import Resource, reqparse
from app.meals import Meal, meals

for i in range(1, 10):
    price = 1000 + i
    n = Meal(price, 'something soemthing')
    meals.append(n)


class MealsResource(Resource):
    def get(self):
        return {
            'meals':  [{'id': meal.id, 'price': meal.price, 'desc': meal.desc} for meal in meals]
        }

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('price', type=float,
                            required=True, help='Price is required')
        parser.add_argument('desc', type=str,
                            required=True, help='Description is required')
        params = parser.parse_args()
        price = params['price']
        desc = params['desc']

        meal = Meal(price=price, desc=desc)
        meal.addMeal()

        return {
            'meals':  [{'id': meal.id, 'price': meal.price, 'desc': meal.desc} for meal in meals]
        }, 200


class MealResource(Resource):
    
    def put(self, meal_id):
        parser = reqparse.RequestParser()
        parser.add_argument('price', type=float, required=True)
        parser.add_argument('desc', type=str, required=True)
        params = parser.parse_args()
        price = params['price']
        desc = params['desc']
        for meal in meals:
            if meal['id'] == meal_id:
                meal['desc'] = desc
                meal['price'] = price
                return {'meals': {'id': meal.id, 'price': meal.price, 'desc': meal.desc}}

    def delete(self, meal_id):
        for meal in meals:
            if meal['id'] == meal_id:
                meal.deleteMeal()
                return {
                    'meals':  [{'id': meal.id, 'price': meal.price, 'desc': meal.desc} for meal in meals]
                }, 200


