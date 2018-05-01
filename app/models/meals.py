meals = [
    {
      "id": 21,
      "desc": "Beans with rice",
      "price": 20000    },
     {
      "id": 22,
      "desc": "Meat with cassava",
      "price": 12000    },
    {
      "id": 23,
      "desc": "Minced meat with pasta",
      "price": 14000    }
]


def get_meal_by_id(meal_id):
    for meal in meals:
        if meal['id'] == meal_id: 
            return meal 

class Meal(object):
    count = 0
    
    def __init__(self, desc, price):
        Meal.count = Meal.count + 1
        self.id = Meal.count
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


        


     

    
