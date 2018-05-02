from flask import Flask
from config import config
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(config['development'])
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app)

from .api import apiv1
app.register_blueprint(apiv1, url_prefix='/api/v1')


