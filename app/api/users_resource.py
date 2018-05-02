from flask_restplus import Resource, reqparse
from flask import jsonify
from app.models.users import User, users, get_user_by_username

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True,
                    help='Username is required')
parser.add_argument('password', type=str, required=True,
                    help='Password is required')
parser.add_argument('isAdmin', type=bool, required=True,
                    help='Status is required')


class UsersResource(Resource):
    def get(self):
        return jsonify({
                'users': users})


class UserRegister(Resource):
    def post(self):
        data = parser.parse_args()

        user = User(
        username=data['username'],
        password=data['password'],
        isAdmin=data['isAdmin'])

        user = get_user_by_username(param['username'])
        if user:
            return {'message': 'User {} already exists'. format(param['username'])}
        else:
            user.addUser()
            return {'user': user.to_dict()}, 201
       


class UserLogin(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True,
                    help='Username is required')
        parser.add_argument('password', type=str, required=True,
                    help='Password is required')
        param = parser.parse_args()
        user = get_user_by_username(param['username'])
        #user = [u for u in users if param['username'] == u['username']]

        if not user:
            return {'message': 'User {} does not exist'. format(param['username'])}
      
        if user['password'] == param['password']:
            return {'message': 'Logged in as {}'. format(user['username'])}
        else:
            return {'message': 'Wrong credentials'}





















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


