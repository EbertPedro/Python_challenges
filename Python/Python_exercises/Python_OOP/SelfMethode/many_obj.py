class car():
    def __init__(self, model, color):
        self.model = model
        self.color = color
        print("This is a constructor!!")
        
    def show(self):
        print("The model is: %s" %self.model)
        print("The color is: %s" %self.color)
        
car_obj1 = car("Audi","Black")
car_obj2 = car("Toyota","Blue")

car_obj1.show()
car_obj2.show()

# #Also, we can show in this way:
# car("Audi","Black").show()
# car("Toyota","Blue").show()