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
        return {
                'users': users}


class UserRegister(Resource):
    def post(self):
        data = parser.parse_args()
        user = get_user_by_username(data['username'])

        if user:
            return {'message': 'User {} already exists'.format(data['username'])}
        username = data['username']
        password = data['password']
        isAdmin = data['isAdmin']
        user ={"username":username, "password":password, "isAdmin": isAdmin}
        try:
            users.append(user)
            return { 
                'username': (data['username'])
                }, 201
        except Exception as err:
            return {'message': '{}'.format(err)}, 500
       


class UserLogin(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True,
                    help='Username is required')
        parser.add_argument('password', type=str, required=True,
                    help='Password is required')
        param = parser.parse_args()
        user = get_user_by_username(param['username'])
        if not user:
            return {'message': 'User {} does not exist'. format(param['username'])}
        if (param['password'] == user['password']):
            return {
                'message': 'Logged in as {}'.format(user['username']),
                }
        else:
            return {'message': 'Wrong credentials'}
        
