'''
functions are code blocks performing specific tasks 
In python we define functions using the def keyword 
- functions can take arguments (parameters), perform operations , optionally return a value 
'''

# syntax 
def function_name(parameters):
    # function body 
    # perform operations 
    # invoke other functions 
    return parameters


def calculate_area(length, width):
    area = length * width
    return area 
result = calculate_area(5,4)
print("area " , result)


# default arguments : you can define default values for your parameters 
def greet(name="Joseph"):
    return "hello " + name + "!"
print(greet())
print(greet("Mary"))

# variable number of arguments : you can define functions that accept a variable number of arguments 
# *args keyword to represent numerics [bundled as a list] , **kwargs keyword to represents key and pair values(bundled as a dictionary)
# for args and kwargs : use return at the end 
def sum_values(*args):
    total = 0
    for num in args:
        total += num
    return total


print(sum_values(1,2,3,4))

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key + ': ', value)

print(print_info(name="Alice", age=30, country="Kenya"))


# Lambda expressions/ functions : also known anonymous functions , are small, inline functions defined using 
# the lambda keyword 

def square(x):
    return x * x

print(square(4))


# equivalent lambda function 
square = lambda x,y: (x + y) ** 2 
print(square(4,5))