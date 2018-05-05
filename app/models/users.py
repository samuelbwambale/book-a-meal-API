from passlib.hash import pbkdf2_sha256 as sha256

users = []

class User:
    def __init__(self, username, password, isAdmin):
        self.username = username
        self.password = password
        self.isAdmin = isAdmin

    def addUser(self):
        users.append(self)

    def updateUser(self, username, password, isAdmin):
        self.username = username
        self.password = password
        self.isAdmin = isAdmin

    def deleteUser(self):
        users.remove(self)

    def to_dict(self):
        return {
           'username': self.username,
           'password': self.password,
           'isAdmin': self.isAdmin
       }

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)


def get_user_by_username(user_name):
    for user in users:
        if user['username'] == user_name: 
            return user
    
        

