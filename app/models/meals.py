meals = []

class Meal(object):
    count = 0
    
    def __init__(self, desc, price):
        self.id = Meal.count+1
        self.desc = desc
        self.price = price
        

    def	addMeal(self):
	    meals.append() 
	    return True
	
    def deleteMeal(self):
        meals.remove(self)
        return True        

    def updateMeal(self,price,desc):
        self.desc = desc
        self.price = price   
        return True  

    def to_dict(self):
        return {
           'id': self.id,
           'desc': self.desc,
           'price': self.price
       }

def get_meal_by_id(meal_id):
    for meal in meals:
        if meal['id'] == meal_id: 
            return meal


        


     

    
