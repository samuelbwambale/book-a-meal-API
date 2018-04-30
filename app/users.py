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
        

