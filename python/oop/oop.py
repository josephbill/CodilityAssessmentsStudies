'''
- OOP is a programming paradigm that revolves around 'objects'
- Objects 
  - entities that contain data in the form of fields often known as attributes or properties
  - they also contain code in the form of of procedures often known as methods

  -blueprint Vehicle : acceleration speed , brake , color , shape , engine 
    objects  - Toyota , Jeep , Mercedes , /......
    current object (instance)
 - Blueprints (classes) -> classes define the blueprints(plan) for objects 


 Classes and Objects 
 String Object 
    - props : length , punctuation , whitespace , ascii_letters
    - methods : upper() - converting all chr in a string to uppercase  
      lower() 

- A class is like an object constructor 
- or a blueprint for creating the objects 
'''


str()
# to create a class we use a keyword :  class 
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

# x = "joseph"
# x.upper()

# print(x.upper())

class MyClass: 
    '''
    if you define your class without a constructor, then python associates the default __init__
    that does nothing 
    '''
    def __init__(self):
        pass
    y = 10
    # nested , jskjkfjkdjf , kfdjfkdf
    def method(self):
        x = 5 
        print(f"this is a string" ,str(self.y))


obj = MyClass()
obj.method()

'''
Fundamentals of OOP programming 
1. Encapsulation : bundling of data(attributes/props.) and methods that operate on that data into a single
class 
2. Abstraction : involves simplifying complex systems by modelling classes appropriate to the problem 
3. Inheritance : allows classes(subclass, derived class) to inherit attributes and methods from another class (superclass, base class)
Aids in reusablity and establishes relationships btw classes 
4. Polymorphism : Allows methods to do different things based on the object that calls them.
'''