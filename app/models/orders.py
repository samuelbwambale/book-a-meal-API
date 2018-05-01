orders = []

def get_order_by_id(order_id):
    for order in orders:
        if order['id'] == order_id: 
            return order

class Order:
    count = 0
    def __init__(self, meals):
        Order.count += 1
        self.id = Order.count
        self.meals = []

    def deleteOrder(self):
        orders.remove(self)

    def addOrder(self):
        orders.append(self)




