fibonnacii_sequence = {}
def fibonnacii(n):
    # 0,1 , 1,1 
    # check if nth already exists in the dictionary 
    if n in fibonnacii_sequence:
        return fibonnacii_sequence[n]
        
    if n == 1: 
        return 1
    elif n == 2:
        return 1 
    elif n > 2:
        value  = fibonnacii(n-1) + fibonnacii(n-2)
        # store the value to the dictionary 
        fibonnacii_sequence[n]  = value
                    
    return value 
    
for n in range(1,500):
    print(n, ":" , fibonnacii(n))
    
    
## Look up a list , dictionary, sets 
## 
    
    
