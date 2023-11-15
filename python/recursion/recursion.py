def fact(n):
    # base case 
    if n == 1:
        return 1
    else: 
        return n * fact(n-1)
    

print(fact(4))