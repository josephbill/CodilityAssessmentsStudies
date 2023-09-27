# Create a dictionary 
# access , modification , adding , removing of entries 
# trasversal / looping

employees = {
    "John" : {"age" : 30 , "position" : "CTO"},
    "Jane" : {"age" : 30 , "position" : "Developer"},
    "Mike" : {"age" : 30 , "position" : "Accountant"}, 
}

# accessing 
print(employees["John"]["position"])

# modification 
employees["Jane"]["age"] = 31

# adding new entries 
employees["Bill"] = "True"

print(employees)