def insertion_sort(arr):
    # start our iteration from the second element to the end of the array 
    for i in range(1, len(arr)):
    #    store the current element 64
        key = arr[i]
    #   keep track of the previous index : 90
        j = i - 1
    #  start a loop that moves elements greater than the key to right 
    # to have it in descding : key > 
    #  to have it in ascending : key <
        while j>= 0 and key > arr[j]:
            # syntax to shift the key to the right 
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [64,34,25,12,22,11,90]
insertion_sort(arr)
print("Sorted Array : " , arr)