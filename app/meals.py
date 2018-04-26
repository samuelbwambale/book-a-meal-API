meals = []
count = 0

class Meal(object):
    def __init__(self, price,desc):
        count += 1
        self.id = count
        self.desc = desc
        self.price = price

    def	addMeal(self):
	    meals.append(self) 
	    return "Success"
	
    def deleteMeal(self):
        meals.remove(self)
        return "Success"         

    def updateMeal(self,price,desc):
        self.price = price
        self.desc = desc   
        return "Success"
     

    
