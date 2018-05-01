from datetime import datetime
menus = []

def get_menu_by_id(menu_id):
    for menu in menus:
        if menu['menu_id'] == menu_id: 
            return menu

class Menu:
    count = 0
    def __init__(self, forToday, meals):
        Menu.count = Menu.count + 1
        self.id = Menu.count
        self.forToday = forToday
        self.meals = []
    
    def addMenu(self):
        menus.append(self)

    def updateMenu(self, forToday, meals):
        self.forToday = forToday
        self.meals = meals

    def deleteMenu(self):
        menus.remove(self)
        return "Success"
        		
