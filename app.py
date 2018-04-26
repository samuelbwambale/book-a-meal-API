# app.py

from flask import Flask, jsonify, abort, make_response, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)

    meals = [
        {
            'id': 1,
            'desc': u'Beef and Rice',
            'price': 12000
        },
        {
            'id': 2,
            'desc': u'Fried chicken and spaghetti',
            'price': 18000
        },
        {
            'id': 3,
            'desc': u'Pizza magherita',
            'price': 20000
        },
        {
            'id': 5,
            'desc': u'Steak and pasta',
            'price': 8000
        }
    ]


menu = {

    'id': 1,
    'desc': u'Beef and Rice',
            'meals': [
                {'id': 5, 'desc': u'Steak and pasta', 'price': 8000},
                {
                    'id': 3,
                    'desc': u'Pizza magherita',
                    'price': 20000
                }]
}


orders = [
    {
        'id': 111,
        'cost': 28000
    },
    {
        'id': 112,
        'cost': 12000
    },
    {
        'id': 113,
        'cost': 30000
    }
]


@app.route('/buonpranzo/api/v1/')
def index():
    return "Welcome to Buon Pranzo"

# Register a user

# Login a user

# Get all the meal options - GET


@app.route('/buonpranzo/api/v1/meals/', methods=['GET'])
def get_meals():
    return jsonify({'meals': meals})

# Add a meal option - POST


@app.route('/buonpranzo/api/v1/meals/', methods=['POST'])
def add_meal():
    if not request.json or not 'id' or not 'desc' or not 'price' in request.json:
        abort(400)
    meal = {
        'id': meals[-1]['id'] + 1,
        'desc': request.json['desc'],
        'price': request.json.get('price')
    }
    meals.append(meal)
    return jsonify({'meals': meals}), 201

# Update the information of a meal option - PUT


@app.route('/buonpranzo/api/v1/meals/<int:meal_id>', methods=['PUT'])
def update_meal(meal_id):
    meal = [meal for meal in meals if meal['id'] == meal_id]
    if len(meal) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'desc' in request.json and type(request.json['desc']) is not unicode:
        abort(400)
    if 'price' in request.json and type(request.json['price']) is not str:
        abort(400)
    meal[0]['desc'] = request.json.get('desc', meal[0]['desc'])
    meal[0]['price'] = request.json.get('price', meal[0]['price'])
    return jsonify({'meals': meal[0]})

# Remove a meal option - DELETE


@app.route('/buonpranzo/api/v1/meals/<int:meal_id>', methods=['DELETE'])
def delete_meal(meal_id):
    meal = [meal for meal in meals if meals['id'] == meal_id]
    if len(meal) == 0:
        abort(404)
    meals.remove(meal[0])
    return jsonify({'result': True})

# Setup the menu for the day - POST


@app.route('/buonpranzo/api/v1/menu/', methods=['POST'])
def setup_menu():
    if not request.json or not 'id' or not 'name' or not 'meals' in request.json:
        abort(400)
    menu = {
        'id': menu[-1]['id'] + 1,
        'name': request.json['desc'],
        'meals': request.json.get('meals')
    }
    menu.append(menu)
    return jsonify({'menu': menu}), 201

# Get the menu for the day - GET


# Select the meal option from the menu - POST


# Modify an order - PUT

# Get all the orders - GET


if __name__ == '__main__':
    app.run(debug=True)
