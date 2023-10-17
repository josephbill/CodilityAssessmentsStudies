# 0,1,1,2,3,5,8....
fibonnaci_sequence = {}
def fibonnaci(n): 
    # check if the calc. of n is stored in the dictionary 
    # fibonnaci_sequence[n]  : access : storage 
    if n in fibonnaci_sequence:
        return fibonnaci_sequence[n]
    
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        # create our fibonnaci value 
        value = fibonnaci(n-1) + fibonnaci(n-2) 
        # store the value to dictionary 
        fibonnaci_sequence[n] = value

    return value

for n in range(1,101):
    print(n, ":" , fibonnaci(n))


