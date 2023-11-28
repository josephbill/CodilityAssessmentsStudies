def fact(n):
    # base case 
    if n == 1:
        return 1
    else: 
        return n * fact(n-1)
    

print(fact(4))

# observations 
'''
1. Each recursive call creates it's own scope 
2. Flow of control passes back to previous scope once function call returns the value i.e. 

a. a global scope is created when fact is called 
b. then the first scope : fact when n is 4 :  the return here is : return 4 * fact(3)
c. the second scope : fact when n is 3 :  the return here is : return 3 * fact(2)
d. the third scope : fact when n is 2 :  the return here is : return 2 * fact(1)
c. the fourth scope : fact when n is 1:  the return here is  : 1

thus fact(1) is 1  meaning d  = 2 , thus fact(2) is 2 , meaning c = 6 , thus fact(3) is 6 , meaning when fact(4) return is 24 i.e. 4 * 6 
'''