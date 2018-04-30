from flask_restplus import Api
from flask import Blueprint

apiv1 = Blueprint('api',__name__)
api = Api(apiv1)


from .meals_resource import MealsResource
from .meals_resource import MealResource
from .menus_resource import MenuResource
api.add_resource(MealsResource,'/meals')
api.add_resource(MealResource,'/meals/<int:meal_id>')
api.add_resource(MenuResource,'/menu')

from .users_resource import UsersResource
from .users_resource import UserRegister
from .users_resource import UserLogin
api.add_resource(MealsResource,'/users')
api.add_resource(MealsResource,'/auth/signup')
