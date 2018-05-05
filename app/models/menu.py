from datetime import datetime
from meals import Meal, get_meal_by_id


menus = []

def get_menu_by_id(menu_id):
    for menu in menus:
        if menu['id'] == menu_id: 
            return menu

def get_menu_for_today():
    for menu in menus:
        if menu['forToday'] == True:
            return menu

class Menu:
    count = 0
    def __init__(self, forToday, meals):
        Menu.count = Menu.count + 1
        self.id = Menu.count
        self.forToday = forToday
        self.meals = []
    
    def add_meal_to_menu(self, meal_id):
        selected_meal = get_meal_by_id(meal_id)
        self.meals.append(selected_meal)

    def updateMenu(self, forToday, meals):
        self.forToday = forToday
        self.meals = meals

    def deleteMenu(self):
        menus.remove(self)
        return "Success"

    def to_dict(self):
        return {
            'id': self.id,
            'forToday': self.forToday, 
            'meals': [meal.to_dict() for meal in self.meals]
        }
        		
