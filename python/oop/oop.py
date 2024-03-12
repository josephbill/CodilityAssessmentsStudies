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

Components of OOP 
Class Attributes and methods : they belong to the class and not the instances (objects)

1. Class Attributes 
- these are variables shared by all instances of the class 
- defined within the class block outside any method(s)
- they can be accessed using the class name or the instance of the class 

'''

class Vehicle: 
    # class attribute 
    wheel = 4 

    # instance attributes/methods 
    def __init__(self, brand , model) -> None:
        self.brand  = brand
        self.model = model

    brakessytem = False
    def wheeler(self):
        print(self.wheel)


# Access using class name 
print(Vehicle.wheel) 
# access using an instance (object)
car1 = Vehicle("Toyota", "Camry")
print(car1.wheel) # 4
car1.wheel = 6
Vehicle.wheel = 10
# these attributes can be modified directly only from instance 
print(car1.wheel) # 6
print(Vehicle.wheel)

'''
Class methods 
- these methods are bound to the classes rather than the instances 
- they are defined using the @classmethod decorator , and takes a special parameter 'cls' which references the 
class itself 
- class methods can access and modify class attributes but NOT instance attributes directly. 
'''

class Circle: 
    pi = 3.14 

    def __init__(self, radius) -> None:
        self.radius = radius

    # class methods 
    # how to define and access class attributes 
    @classmethod
    def change_pi(cls, new_pi):
        cls.pi = new_pi

    @classmethod
    def revert_pi(cls):
        cls.change_pi(3.14)
      

    def printRadius(self):
        print(f"{self.radius}")


# access class attributes before change 
print(Circle.pi) 
# calling the class methods 
Circle.change_pi(3.14159)
# Circle.printRadius()  #works only for object creation
# class attribute after change 
print(Circle.pi)
# reverting pi
Circle.revert_pi()
print(Circle.pi)
