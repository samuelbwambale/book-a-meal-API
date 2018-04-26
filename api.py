
from flask import Flask, jsonify, abort, make_response, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


meals = {
    'meal1': {'name': 'Beans with rice'},
    'meal2': {'name': 'Pizza'},
    'meal3': {'name': 'Chicken and chips'},
}



def abort_if_meal_doesnt_exist(meal_id):
    if meal_id not in meals:
        abort(404, message="Meal {} doesn't exist".format(meal_id))

parser = reqparse.RequestParser()
parser.add_argument('name')


# Meal
# shows a single todo item and lets you delete a todo item
class Meal(Resource):
    def get(self, meal_id):
        abort_if_meal_doesnt_exist(meal_id)
        return meals[meal_id]

    def delete(self, meal_id):
        abort_if_meal_doesnt_exist(meal_id)
        del meals[meal_id]
        return '', 204

    def put(self, meal_id):
        args = parser.parse_args()
        meal = {'name': args['name']}
        meals[meal_id] = meal
        return meal, 201



# shows a list of all meals and add meal to meals
class Meals(Resource):
    def get(self):
        return meals

    def post(self):
        args = parser.parse_args()
        meal_id = int(max(meals.keys()).lstrip('meal')) + 1
        meal_id = 'meal%i' % meal_id
        meals[meal_id] = {'name': args['name']}
        return meals[meal_id], 201

## Actually setup the Api resource routing here
api.add_resource(Meals, '/meals')
api.add_resource(Meal, '/meals/<meal_id>')



if __name__ == '__main__':
    app.run(debug=True)