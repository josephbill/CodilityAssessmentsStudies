'''
Decorators in python allow us to modify or extend the behaviour of functions or methods without changing the ]
actual code 

They take in a function as input , and return a new function 

- logging : print 
- authentication

'''

# define a decorator 
def my_decorator(funct):
    def innerFunction():
        # here logic for the extended behaviour
        print("something happens before function call") 
        funct()
        # here more logic
        print("something happens after function call") 


    return innerFunction


# define function to be decorated 
@my_decorator
def sayHello():
    print("Hello!")


# decorators to use on the function 
sayHello()