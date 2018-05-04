from flask_restplus import Resource, reqparse
from flask import jsonify
from app.models.orders import Order, orders, get_order_by_id
from app.models.meals import Meal, meals, get_meal_by_id
from app.models.users import User

parser = reqparse.RequestParser()
parser.add_argument('user', type=dict, required=True)
parser.add_argument('meals', type=list, required=True)



class OrderResource(Resource):
    def get(self, order_id):
        order = get_order_by_id(order_id)
        return {
            'order': order
            }

    def put(self, order_id):
        order = get_order_by_id(order_id)
        if not order:
            return {
                'error': 'Bad request, no meal with such id exists'
            }, 400
        data = parser.parse_args()
        order = get_order_by_id(order_id)
        order['user'] = data['user']
        order['meals'] = data['meals']
        return jsonify({'order': order})
    
    def delete(self, order_id):
        order = get_order_by_id(order_id)
        order.deleteOrder()
        return jsonify({'orders': orders})


class OrdersResource(Resource):
    def get(self):
        return jsonify({
            'orders':  orders
            })

    def post(self):
        data = parser.parse_args()
        order = Order(data['user'],data['meals'])
        order.addOrder()
        return {'order':{
            'id': order.id,
            'user': order.user,
            'meals': [meal.to_dict() for meal in order.meals]
        } }, 201

