import ipdb
def divide(a,b):
    result = a/b
    return result 
try:
    ipdb.set_trace()  # start our debugging 
    result = divide(10,0)
    print(result)
except ZeroDivisionError as e:
    print("error " , e)