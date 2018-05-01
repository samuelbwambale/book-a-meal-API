import random
meals = []

class Meal(object):    
    def __init__(self, desc, price):
        self.desc = desc
        self.price = price

    def	addMeal(self):
	    meals.append(self) 
	    return True
	
    def deleteMeal(self):
        meals.remove(self)
        return True        

    def updateMeal(self,price,desc):
        self.desc = desc
        self.price = price   
        return True  


        


     

    
