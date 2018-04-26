orders = []
count = 0

class Orders:
    def __init__(self, id, meals, userId):
        count += 1
        self.id = count
        self.meals = []
        self.userId = userId


    def deleteOrder(self):
        orders.remove(self)

    def addOrder(self):
        orders.append(self)

    def updateOrder(self, meals)
        self.meals = meals


