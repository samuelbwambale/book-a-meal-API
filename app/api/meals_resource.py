from flask_restplus import Resource, reqparse
from flask import jsonify
from app.models.meals import Meal, meals, get_meal_by_id



class MealsResource(Resource):
    
    def get(self):
        return {
                'meals': meals}

    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int,
                            required=True, help='Id is required')
        parser.add_argument('price', type=int,
                            required=True, help='Price is required')
        parser.add_argument('desc', type=str,
                            required=True, help='Description is required')
        params = parser.parse_args()
        id = params['id']
        price=params['price']
        desc=params['desc']
        meal ={"price":price, "desc":desc, "id": id}
        meals.append(meal)
        message = "{} has been added".format(meal)
        return {'message': message }, 201


class MealResource(Resource):
    def put(self, meal_id):
        parser = reqparse.RequestParser()
        parser.add_argument('price', type=int, required=True)
        parser.add_argument('desc', type=str, required=True)
        params = parser.parse_args()
        meal = get_meal_by_id(meal_id)
        if not meal:
            return {
                'error': 'Bad request, no meal with such id exists'
            }, 400
        meal["id"] = meal_id,
        meal["price"] = params['price']
        meal["desc"] = params['desc']
        return {'message': meal },200


    def delete(self, meal_id):
        meal = get_meal_by_id(meal_id)
        if not meal:
            return {
                'error': 'Bad request, no meal with such id exists'
            }, 400
        meals.remove(meal)
        return {'message': "Meal deleted" },200


