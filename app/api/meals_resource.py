from flask_restplus import Resource, reqparse
from flask import jsonify
from app.meals import Meal, meals




class MealsResource(Resource):
    def get(self):
        #import pdb; pdb.set_trace()
        # return {
        #     'meals': [meal for meal in meals]
        # }, 200
        return jsonify({
                'meals': meals})

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('price', type=int,
                            required=True, help='Price is required')
        parser.add_argument('desc', type=str,
                            required=True, help='Description is required')
        params = parser.parse_args()
        #print (str(params['price']) +" " + params['desc'] )
        meal = Meal(price=params['price'], desc=params['desc'])
        if meal:
            return {'message': 'Meal has been added' }, 201


class MealResource(Resource):
    def put(self, meal_id):
        parser = reqparse.RequestParser()
        parser.add_argument('price', type=int, required=True)
        parser.add_argument('desc', type=str, required=True)
        params = parser.parse_args()
        price = params['price']
        desc = params['desc']
        for meal in meals:
            if meal['id'] == meal_id:
                meal['desc'] = desc
                meal['price'] = price
                return {'meal': meal.to_dict()}

    def delete(self, meal_id):
        for meal in meals:
            if meal['id'] == meal_id:
                meal.deleteMeal()
                return {'meals': [meal for meal in meals]}


