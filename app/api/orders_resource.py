from flask_restplus import Resource, reqparse
from flask import jsonify
from app.models.orders import Order, orders, get_order_by_id

parser = reqparse.RequestParser()
parser.add_argument('meals', type=list, required=True)

class OrderResource(Resource):
    def get(self, order_id):
        order = Order.get_order_by_id(order_id)
        return jsonify({'order': order})
         

    def put(self, order_id):
        data = parser.parse_args()
        order = Order.get_order_by_id(order_id)
        order['meals'] = data['meals']
        return jsonify({'order': order})
    
    def delete(self, order_id):
        order = Order.get_order_by_id(order_id)
        order.deleteOrder()
        return jsonify({'orders': orders})


class OrdersResource(Resource):
    def get(self):
        return jsonify({
            'orders':  orders})

    def post(self):
        data = parser.parse_args()

        order = Order(
        meals=data['meals'])

        order.addOrder()
        return jsonify({'order': order}), 200



