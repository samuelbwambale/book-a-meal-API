from flask_restplus import Resource, reqparse
from flask import jsonify
from app.models.orders import Order, orders, get_order_by_id
from app.models.meals import Meal, meals, get_meal_by_id
from app.models.users import User

parser = reqparse.RequestParser()
parser.add_argument('user', type=dict, required=True)
parser.add_argument('meals', type=list, required=True)
parser.add_argument('id', type=int, required=True)



class OrderResource(Resource):
    def get(self, order_id):
        order = get_order_by_id(order_id)
        return {'order': order
                }

    def put(self, order_id):
        order = get_order_by_id(order_id)
        if not order:
            return {
                'error': 'Bad request, no order with such id exists'
            }, 400
        data = parser.parse_args()
        order['user'] = data['user']
        order['meals'] = data['meals']
        return {'order': order}, 200
    
    def delete(self, order_id):
        order = get_order_by_id(order_id)
        if not order:
            return {
                'error': 'Bad request, this order does not exists'
            }, 400
        order.remove(order)
        return {'Message': "Order deleted"}, 200


class OrdersResource(Resource):
    def get(self):
        return {
            'orders':  orders
            }

    def post(self):
        params = parser.parse_args()
        user = params['user']
        Id = params['id']   
        meals = params['meals']        
        order ={"user":user, "id":Id, "meals":meals}
        orders.append(order)
        message = "{} has been added".format(order)
        return {'message': message }, 201

