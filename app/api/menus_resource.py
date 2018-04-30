from flask_restplus import Resource, reqparse
from app.menu import Menu, menus

menus = [
    {'id': 222,
     'date': "2018-04-24 10:30:55.423844",
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
     'date': "2018-04-26 10:40:11.423844",
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
        parser = reqparse.RequestParser()
        parser.add_argument('date', type=date, required=True)
        parser.add_argument('meals', type=list, required=True)
        params = parser.parse_args()
        date = params['date']
        meals = params['meals']
        menu = Menu(date=date.today(), meals=[{
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
            "id": 1,
            "description": 1003
        }])
        menu.addMenu()
        return {
            'menus':  [{'id': menu.id, 'date': menu.date, 'meals': menu.meals} for menu in menus]
        }, 200

    def get(self):
        return {
                'menus':  [{'id': menu.id, 'date': menu.date, 'meals': menu.meals} for menu in menus]
            }
