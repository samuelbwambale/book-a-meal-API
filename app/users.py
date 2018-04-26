users = []
count = 0

class Users:
    def __init__(self, userId, email, password):
        count += 1
        self.id = count
        self.email = email
        self.password = password

    def addUser(self):
        users.append(self)

    def updateUser(self, email, password):
        self.email = email
        self.password = password

    def deleteUser(self):
        users.remove(self)
        

