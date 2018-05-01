from datetime import datetime
from flask import jsonify
from flask_restplus import Resource, reqparse
from app.models.menu import Menu, menus, get_menu_by_id

parser = reqparse.RequestParser()
parser.add_argument('forToday', type= bool, required=True)
# parser.add_argument('date', type=lambda x: datetime.strptime(x,'%Y-%m-%dT%H:%M:%S'), help='Wrong date format')
parser.add_argument('meals', type=list, required=True)

menus = [
    {'id': 222,
     'forToday': False,
     'meals': [{
         "price": "something soemthing",
         "id": 8,
         "description": 1001
     },
         {
         "price": "something soemthing",
         "id": 9,
         "description": 1002
     },
         {
         "price": "something soemthing",
         "id": 15,
         "description": 1003
     }]},

    {'id': 111,
     'forToday': True,
     'meals': [{
             "price": "something soemthing",
             "id": 3,
         "description": 1001
     },
         {
         "price": "something soemthing",
         "id": 18,
         "description": 1002
     },
         {
         "price": "something soemthing",
         "id": 20,
         "description": 1003
     }]}
]


class MenuResource(Resource):
    def post(self):
        data = parser.parse_args()
        
        new_menu = Menu(
        forToday = data['forToday'],
        meals = data['meals']) 
        new_menu.addMenu()
        return jsonify({
            'menu': menu }), 200

    def get(self):
        data = parser.parse_args()
        my_menu = Menu.get_menu_by_id(data['id'])

        if not my_menu:
            return {'message': 'Menu {} does not exist'. format(data['username'])}
        
        if data['forToday'] == True:
            return jsonify({'my_menu': my_menu}), 200
        else:
            return {'message': 'Not todays menu'}

class MenusResource(Resource):
    def get(self):
        return jsonify({
                'menus': menus})
