def linear_search(arr, target):
     for i in range(len(arr)):
          if arr[i] == target:
             return i
     return -1


arr = [3,1,4,1,5,8,9,5,3,5]
target = 1
result = linear_search(arr,target)
print(f"Index of {target} is {result}")