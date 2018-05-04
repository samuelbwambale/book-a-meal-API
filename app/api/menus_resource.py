from datetime import datetime
from flask import jsonify
from flask_restplus import Resource, reqparse
from app.models.menu import Menu, menus, get_menu_by_id
from app.models.meals import Meal

parser = reqparse.RequestParser()
parser.add_argument('forToday', type= bool, required=True, location="json")
parser.add_argument('meals', type=list, required=True, location="json")


class MenuResource(Resource):
    def post(self):
        data = parser.parse_args()        
        new_menu = Menu(
        forToday = data['forToday'],
        meals = data['meals']) 
        menus.append(new_menu)
        return ({'menu': new_menu.to_dict() })


    def get(self):
        data = parser.parse_args()
        my_menu = Menu.get_menu_by_id(data['id'])
        if not my_menu:
            return {'message': 'Menu does not exist'. format(data['id'])}
        
        if data['forToday'] == True:
            return jsonify({'my_menu': my_menu}), 200
        else:
            return {'message': 'Not todays menu'}

class MenusResource(Resource):
    def get(self):
        return jsonify({
                'menus': menus})
