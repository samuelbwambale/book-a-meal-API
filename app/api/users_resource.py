from flask_restplus import Resource, reqparse
from flask import jsonify
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
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
        # return {
        #     'users': [user for user in users]
        # }, 200
        return jsonify({
                'users': users})


class UserRegister(Resource):
    def post(self):
        data = parser.parse_args()
        user = get_user_by_username(data['username'])

        if user:
            return {'message': 'User {} already exists'.format(data['username'])}

<<<<<<< HEAD
        user = get_user_by_username(param['username'])
        if user:
            return {'message': 'User {} already exists'. format(param['username'])}
        else:
            user.addUser()
            return {'user': user.to_dict()}, 201
=======
        user = User(
        username = data['username'],
        password = User.generate_hash(data['password']),
        isAdmin = data['isAdmin'])

        try:
            user.addUser()
            access_token = create_access_token(identity = data['username'])
            refresh_token = create_refresh_token(identity = data['username'])
            return { 
                'user': user.to_dict(),
                'message': 'User {} was created'.format(data['username']),
                'access_token': access_token,
                'refresh_token': refresh_token
                }, 201
        except Exception as err:
            return {'message': '{}'.format(err)}, 500
>>>>>>> 694b6eda4948ee5fa436ec5fc256fad2c5e615b8
       


class UserLogin(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True,
                    help='Username is required')
        parser.add_argument('password', type=str, required=True,
                    help='Password is required')
        param = parser.parse_args()
        user = get_user_by_username(param['username'])
<<<<<<< HEAD
        #user = [u for u in users if param['username'] == u['username']]

        if not user:
            return {'message': 'User {} does not exist'. format(param['username'])}
      
        if user['password'] == param['password']:
            return {'message': 'Logged in as {}'. format(user['username'])}
=======
        #import pdb; pdb.set_trace()
        if not user:
            return {'message': 'User {} does not exist'. format(param['username'])}
        if User.verify_hash(param['password'], user['password']):
            access_token = create_access_token(identity = param['username'])
            refresh_token = create_refresh_token(identity = param['username'])
            return {
                'message': 'Logged in as {}'.format(user['username']),
                'access_token': access_token,
                'refresh_token': refresh_token
                }
>>>>>>> 694b6eda4948ee5fa436ec5fc256fad2c5e615b8
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


