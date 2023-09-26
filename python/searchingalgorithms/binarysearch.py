def binary_search(arr,target):
    # left and right pointers for my array collection 
    left,right = 0 , len(arr) - 1
    #  the idea of the pointers 
    #  1. To get a midpoint : we need the left pointer to be less than or equal to the right pointer 
    while left <= right:
        # calculate the midpoint 
        # // : / : integer division 
        mid = left + (right - left ) // 2
        # Integer Overflow : this is more compact 
        # mid = (left + right )// 2
        # once we have the midpoint check if target value matches the midpoint index value.
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target: 
            left = mid + 1
        else: 
            right = mid - 1

    return -1

arr = [1,2,3,4,5,6,7]
target = 7
result = binary_search(arr,target)
print(f"Index of {target} is {result}")


'''
1. Intialization : 
intially left is = 0 (index of the first element )
right = 6 (length of array - 1)
- mid point is calculated at this point :         
mid = left + (right - left ) // 2

2. Comparison with the target 
arr[mid] = arr[3] = 4 
since the target is greater than the midpoint , we move 
the left pointer to [3] mid  +  1 = 4

3. New midpoint calculation 
left is now 4 , right remains 6 
calc the new midpoint : mid = 4 + (6 - 4 ) // 2 =  5


back to 2

4. Left is 6 and right has remained to be 6 
mid = 6 + (6 - 6 ) // 2 =  6

target found = 7 is returned 

- 1 
if -1 = "Value not found!!"


'''