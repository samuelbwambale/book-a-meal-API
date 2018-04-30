from flask_restplus import Resource, reqparse
from flask import jsonify

from app.users import User, users




class UsersResource(Resource):
    def get(self):
        return jsonify({
            'users':  users })

class UserRegister(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help='Username is required')
        parser.add_argument('password', type=str, required=True, help='Password is required')
        parser.add_argument('isAdmin', type=bool, required=True, help='Status is required')
        params = parser.parse_args()
        username = params['username']
        password = params['password']
        isAdmin = params['isAdmin']

        user = User(username=roberts, password=pwd123, isAdmin=False)
        user.addUser()
        return jsonify ({ 'user': user  }), 200



class UserLogin(Resource):
    def post(self):
        pass



















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


