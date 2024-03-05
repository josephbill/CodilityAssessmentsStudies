# List and tuples 
my_list = [1,2,3,4,5]
print(my_list[0])
print(my_list[-1])
my_list.append(6)
my_list.pop()
print(len(my_list))
for i in range(len(my_list)):
    print(my_list[i])
'''
1. access the elements 
2. access the elements from the end 
3. Appending the elements 
4. Remove and return and the last element 
5. Switch the pointers (n, n-1)
6. length -> loops (loop the collection)
7. type casting (converting a sequence to another sequence type)
8. Is the sequence mutable or immutable 
'''

my_tuple = (1,2,3,4,"joseph")
print(my_tuple[4])
print(len(my_tuple))


# sets 
'''
Its a collections that unchangeable(immutable) , unordered , unindexed 
but you can remove(remove) and add (add) new items , join two sets(union)
{}
Duplicates are not allowed (no two items with the same value)
True and 1 as the same thing
False and 0 as the same thing
https://www.w3schools.com/python/python_sets_methods.asp
'''

my_set = {"apple","banana","Orange",True,1}
print(my_set)
print(type(my_set))
for i in my_set:
    print(i)


'''
Dictionaries : 
collection of key and value pairs 
{"a":1, "b": 2}
1. accessing value by key 
2. adding new key value pairs 
3. deleting the key value pairs 
4. checking if a key exists 
5. len of the dictionary 
'''
my_dict = {"a":1, "b": 2}
print(my_dict["a"])
del my_dict["b"]
my_dict["d"] = 4
print('b' in my_dict)
print(len(my_dict))


'''
List Comprehension :: Practice question : give us solution 
'''


'''
Write a function that takes a list of integers as input and returns the count of distinct(unique) elements in the list.
nums = [1,2,3,4,5,2,3,1,4]
# 5

pseudocode 
1. change the list to a set (type casting)
'''
nums = [1,2,3,4,5,2,3,1,4]
def distincts(nums):
    unique_set = set(nums)
    return print(len(unique_set))

distincts(nums)


'''
Write a function that takes two lists of integers as input and returns a list containing only the common elements
 between the two input lists
 list1 = [1,2,3,4,5]
 list2 = [4,5,6,7,8]
output [4,5]
'''
list1 = [1,2,3,[1,2,3],5]
list2 = [4,5,6,7,8]
def commonelements(list1,list2):
    common = set(list1) & (set(list2))
    return print(list(common))

commonelements(list1,list2)
    
