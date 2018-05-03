from flask_restplus import Api
from flask import Blueprint

apiv1 = Blueprint('api',__name__)
api = Api(apiv1)


from .meals_resource import MealsResource
from .meals_resource import MealResource
#GET all meals or POST a meal option
api.add_resource(MealsResource,'/meals')
#PUT or DELETE a meal option
api.add_resource(MealResource,'/meals/<int:meal_id>')

from .menus_resource import MenuResource
from .menus_resource import MenusResource
#POST (setup) or GET menu of the day
api.add_resource(MenuResource,'/menu')
#GET all menus
api.add_resource(MenusResource,'/menus')


from .users_resource import UsersResource
from .users_resource import UserRegister
from .users_resource import UserLogin
#GET all users
api.add_resource(UsersResource,'/users')
#POST to register a user
api.add_resource(UserRegister,'/auth/signup')
#POST to login a user
api.add_resource(UserLogin,'/auth/login')

from .orders_resource import OrdersResource
from .orders_resource import OrderResource
#POST an order or GET all orders
api.add_resource(OrdersResource,'/orders')
#PUT (modify) and order or delete it
api.add_resource(OrderResource,'/orders/orderId')




