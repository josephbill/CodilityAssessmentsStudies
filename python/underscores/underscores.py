'''
In python , underscores in OOP often used in property names to indicate their intended usafe or visibility . 
1. Single underscore prefix (''_propertyname )
 - indicates the property is intended for internal use only 
 - indicates the property should be treated as a private variable (belongs to the clss)
 - there is no strict enforcement of private variables and its more of a convetion unless we are accessing gettters
 and setters using the @property decorator 

2. Double underscore prefix ('' __propertyname)
- the convention makes a property name unique and its often used to avoid name clashes in the subclasses 
(Inheritance)

3. Double underscore prefix and suffix (''__property__)  : used for special inbuilt methods in python, 
__init__ , __repr__ , __str__
'''

class SingleUnderScore:
    def __init__(self):
        self._internalProperty = None
    
    @property
    def property(self):
        return self._internalProperty
     
    @property.setter
    def property(self, value):
        self._internalProperty = value


obj = SingleUnderScore()
obj.property = "Hello"
print(obj._internalProperty)


# Name mangling 
class DoubleUnderscore():
    def __init__(self) -> None:
        self.__property = None


    def get_property(self):
        return self.__property
    
    def get_property(self,value):
        self.__property = value