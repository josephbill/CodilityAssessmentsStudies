'''
Dictionary mapping : refers to associating keys with values in a dictionary data structure.
Use this to replace the 'switch' statement if you have a large number of cases to consider. 
Or if you prefer a cleaner approach 

It leverages on dictionaries and functions to achieve the switch case functionality. 
'''

student_scores = {
    "Alice": 85,
    "Joseph": 100
}

print(student_scores["Alice"])  # 85

def option1():
    return "Option 1 is chosen"

def option2():
    return "Option 2 is chosen"

def option3():
    return "Option 3 is chosen"

def defaultOption():
    return "Default option is chosen"


# dictionary 
options = {
    1: option1,
    2: option2,
    3: option3
}

# function to simulate the switch case 
def switch_case(option):
    # we use the inbuilt .get method to get the values associated with a dictionary key 
    return options.get(option, defaultOption)()

print(switch_case(1))