class Car:
    global x
    x = "Joseph"
    # constructor 
    # self points to the current instance(object)
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # class methods 
    def display_info(self,furtherarguments):
        print(f"Car: {self.brand} {self.model} {x}")


#  to create an object for the class :  we simply use the constructor syntax in python : Class()
car1 = Car("Toyota", "Corolla")
car2 = Car("Mercedes", "Benz")
car3 = Car("Jeep", "X2")
#  to access the attributes belonging to an object : .notation
print(f"Car 1 is  : {car1.brand} : {car1.model}")
# access the methods 
car2.display_info("x")
