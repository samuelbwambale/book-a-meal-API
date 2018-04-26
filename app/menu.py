count = 0
menus = []


class Menu:
    def __init__(self, date,meals):
        count += 1
        self.date = date
        self.meals = []
    
    def addMenu(self):
        menus.append(self)

    def updateMenu(self, date, meals)
        self.date = date
        self.meals = meals

    def deleteMenu(self):
        menus.remove(self)
        return "Success"
        		
