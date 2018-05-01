users = [
        {
      "username": "maurizzio",
      "password": "pwdmmm",
      "isAdmin": True
    },
    {
     "username": "kongolo",
      "password": "pwdkkk",
      "isAdmin": False
    },
    {
     "username": "brians",
      "password": "pwdbbb",
      "isAdmin": False
    }
]

def get_user_by_username(user_name):
    # for user in users:
    #     if user['username'] == user_name: 
    #         return user    
    user = [user for user in users if user['username'] == user_name]
    return user

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
        

