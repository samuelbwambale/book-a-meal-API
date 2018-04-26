from flask_restplus import Api
from flask import Blueprint

apiv1 = Blueprint('api',__name__)
api = Api(apiv1)


from .meals_resource import MealsResource
from .meals_resource import MealResource

api.add_resource(MealsResource,'/meals')
api.add_resource(MealResource,'/meals/<int:meal_id>')
api.add_resource(MenuResource,'/menu')