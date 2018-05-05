import unittest
import json
from app import app
from app.models.users import User, get_user_by_username

users = []

class UsersApiTestCase(unittest.TestCase):


    def setUp(self):
        self.app = app.test_client()

    def test_register(self):
        user = {
            "username": "xaviers",
            "password": "pwdxxx", 
            "isAdmin": True
        }
        response = self.app.post("/api/v1/auth/signup",\
            data=json.dumps(user), content_type='application/json')
        
        self.assertEqual(response.status_code, 201)
        inputs = json.loads(response.get_data())
        

    def test_login(self):
        user = {
            "username": "brians",
            "password": "pwdbbb",
            "isAdmin": False
        }
        response = self.app.post("/api/v1/auth/login",\
            data=json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code, 200)


    def test_login_missing_input_values(self):
        usr = {
            "username": "xaviers",
            "password": "pwdxxx"
        }
        response = self.app.post("/api/v1/auth/signup",\
            data=json.dumps(usr), content_type='application/json')
        self.assertEqual(response.status_code, 400)



    def test_getAllUsers(self):
        response = self.app.get('/api/v1/users', content_type = 'application/json')
        self.assertEqual(response.status_code, 200)

    
