'''
stack = [0] * N 
size = 0 
def push(x):
    global size 
    stack[size] = x 
    size += 1
def pop():
    global size 
    size -= 1
    return stack[size]

do not pop an empty stack.
'''

'''
Reverse a string  : using STACK 
Joseph [] hpesoj 

pseudocode 
lIFO. 
1. Define function to reverse the string will take in the string as a 
parameter
2. Create a stack : define method to create stack 
define helper methods : to get size and to check if stack is empty.

'''

def createStack():
    stack = []
    return stack

# determine the size of the stack 
def size(stack):
    return len(stack)

# def isEmpty(stack):
#     return bool(stack)

def isEmpty(stack):
    if size(stack) == 0:
        return True


# to add item to stack / increase stack with size 1 
def push(stack,item):
    stack.append(item)

# to remove an item from stack / decrease the stack with size1 
def pop(stack):
    if isEmpty(stack):
        return
    return stack.pop()
  

def reverse(string):
    '''
    using the stack created how then can i reverse my string. 
    [h]
    [p]
    [e]
    [s]
    [o]
    [j]
    1. Populate the stack with each chr in the string.
    2. Define an empty string 
    string = 'hpesoj'
    3. LIFO : iterate the range of the string and then
      use .pop to get the item at the top of the stack , appending 
      the result of the pop to the empty string. 
    '''

    lenghtString = len(string)
    # create empty stack 
    stack = createStack()
    # push all chr to the stack 
    for i in range(0,lenghtString,1):
        push(stack,string[i])

    reversedString = ""
    # pop chr out of the stack while appending to empty string 
    for i in range(0,lenghtString,1):
        reversedString += pop(stack)

    return reversedString


string = "Joseph"
print("reversed string " , reverse(string))

