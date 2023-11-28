'''
Write a procedure called oddTuples, which takes a tuple as input,
and returns a new tuple as output, where every other element of the input tuple is copied,
starting with the first one. So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), 
then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').
'''
def oddTuple(atuple):
    '''
    1. iterate the input tuple , with an odd step i.e. 1, len(atuple) , 1
    2. add this to the new tuple 
    '''
    emptyTuple = ()
    result = list(emptyTuple)
    for i in range(0,len(atuple),2):
        result.append(atuple[i])
    emptyTuple = tuple(result)
    return emptyTuple



print(oddTuple(('I', 'am', 'a', 'test', 'tuple')))


listA = [1, 4, 3, 0]
print(sorted(listA))