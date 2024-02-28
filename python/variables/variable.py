#variables are used to store data and can be manipulated and referenced throughout the execution 
# of the program

'''
  key points 
  1. declaration : 
  2. Assignment : '='
  3. Variable name
  4. Data types
  5. Changing values : the value of the variable can be changed during the execution of the program
  6. Variable scope : determining where a variable can be accesed or modified in a program 
'''

first_name = "Joseph"
first_name = "Mary"
print(first_name)

'''
Data types
 - integer (int) : rep. whole numbers > 1 
 - Float (float) : represents real numbers 3.14, 0.5 
 - String (str) : represents sequences of characters within quotes: " "
 - Boolean (bool) : true or false 
 - List (list) : represents an ordered collection of items : [1,2,3,4]
 - Tuple (tuple) : similar to list but immutable : (1,2,3)
 - Dictionary (dict) : represents key-value pairs : { key:value, key:value   }

'''

'''
Type conversion : type casting 
this process involves converting one data type to another 
In python we use built in functions or constructors 
'''

# integer to a float 
int_var = 5
float_var = float(int_var)
print(float_var)

#string to integer 
str_var = '15'
print(int(str_var) + 10)


'''
Variable Scope 
global scope : defined outside a function and can be accessed throughout the program script 
local scope : defined within a function and can only be accessed within that function 
'''

global_var = 10

def functionname():
    local_var = 15
    print(global_var)
    print(local_var)
    

# calling a function 
functionname()


'''
Syntax Error : when code violates the rules of the python syntax : (Indentation errors) (Name error)
Runtime Error : Occur during execution of the code. (TypeError) (ZeroDivisionError)
Logical Error : occur when code produces undesired results due to a flawed logic. (print,ipdb)
'''


