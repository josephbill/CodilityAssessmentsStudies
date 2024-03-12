'''
zoo app
1. Animal feature , Department feature , Employees feature 
- Object relationship  refers to how objects interact with one another and how they are connected within a program 
- Common types of object relationships 
  a. Association    c. Composition
  b. Aggregation    d. Inheritance 
'''
#  Association 
'''
- Represents a relationship where objects of one class are connected to objects of another class
- It can be one to one , one to many , many to many 
- Each object maintains its own identity and exists independently of the other 
'''
class Animal:
    def __init__(self,name) -> None:
        self.name = name


class Department: 
    def __init__(self, name) -> None:
        self.name = name 


class Employee:
    def __init__(self,name, department, animal) -> None:
        self.name = name
        self.department = department
        self.animal = animal
        
# employee1 = Employee("X","XY","XYZ")
# Create the association 
sales_department = Department("Sales")
financial_department = Department("Finance")

animal1 = Animal("Lion")

employee1 = Employee("Joseph Mbugua", sales_department, animal1)
employee2 = Employee("Mary", financial_department, animal1)

print(f"{employee1.name} belongs to {employee1.department.name} who takes charge of this animal {employee1.animal.name}")
# print(f"{employee2.name} belongs to {employee2.department.name}")

# Aggregration 
'''
- A stronger form of association where once class is part of another class 
- It represents a 'has-a' relationship 
- The contained object can still exist independently of the container 
'''

# class Department: 
#     def __init__(self, name) -> None:
#         self.name = name 


# class Employee:
#     # has a department object 
#     def __init__(self,name, department) -> None:
#         self.name = name
#         self.department = department


'''
Composition : is a strong form of aggregration : the lifetime of the contained object depends on the lifetime 
of the container 
- its represents a 'owns-a' relationship
- where the container is destroyed then the contained object is also destroyed 
'''

class Engine: 
    def __init__(self,horsepower) -> None:
        self.horsepower = horsepower

class Car: 
    def __init__(self, model ,horsepower) -> None:
        self.model = model 
        self.engine = Engine(horsepower)

# composition : Car owns Engine 
car1 = Car("Toyota", 203)    
print(car1.engine.horsepower)

engine1 = Engine(205)
print(engine1.horsepower)