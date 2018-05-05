
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



def get_user_by_username(user_name):
    for user in users:
        if user['username'] == user_name: 
            return user
    
        

