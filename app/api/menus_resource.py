from datetime import datetime
from flask import jsonify
from flask_restplus import Resource, reqparse
from app.models.menu import Menu, menus, get_menu_by_id, get_menu_for_today
from app.models.meals import Meal


parser = reqparse.RequestParser()
parser.add_argument('id', type= int, required=True)
parser.add_argument('forToday', type= bool, required=True)
parser.add_argument('meals', type=list, required=True)


class MenuResource(Resource):
    def post(self):
        data = parser.parse_args()

        menu ={"id" : data["id"], "forToday": data["forToday"], "meals":  data['meals']}
        menus.append(menu)
        message = "{} has been added".format(menu)
        return {'message': message }, 201

    def get(self):
        menu = get_menu_for_today()
        if not menu:
            return {'message': 'No menu for today exists'}
        else:
            return {'Todays menu': menu}, 200

class MenusResource(Resource):
    def get(self):
        return {'menus': menus}
