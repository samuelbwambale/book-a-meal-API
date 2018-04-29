menus = []


class Menu:
    def __init__(self, date, meals):
        self.id = random.randint(1,6)
        self.date = date
        self.meals = []
    
    def addMenu(self):
        menus.append(self)

    def updateMenu(self, date, meals):
        self.date = date
        self.meals = meals

    def deleteMenu(self):
        menus.remove(self)
        return "Success"
        		
