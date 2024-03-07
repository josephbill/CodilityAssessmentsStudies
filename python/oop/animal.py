'''
Inheritance
parent/base class : without the parentheses 
derived/subclass : parentheses 

Multi-Inheritance : this means that a class can inherit attributes and methods from multiple base classes 
'''
class Animal:
    # define constructor 
    # attributes and anything else 
    def __init__(self, name) -> None:
        self.name = name

    def sound(self, sound):
        print(f"The animal makes this sound : {sound}" )

    def diet(self):
        return f"This is the diet block"

class B: 
    def method_b(self):
        pass


class Carnivore(Animal):
   def __init__(self,name, gender , animalgroup) -> None:
        super().__init__(name)
        self.gender = gender
        self.animalgroup = animalgroup

        '''
        the rules of polymorphism 
        1. Use the same method to override 
        2. Give new execution 
        '''

   def diet(self,day):
       if(day == "Monday"):
           return f"Meat and Milk"
       elif(day == "Tuesday"):
           return f"Water and Meat"
       
       


class Herbivore(Animal):
    pass


class Omnivores(Animal, B):
    pass

lion = Carnivore("Lion","Male", "Carnivore")
print(f" {lion.name} {lion.gender} {lion.animalgroup}")
print(lion.sound("roar"))
print(lion.diet("Tuesday"))

antelope = Herbivore("Antelope")




