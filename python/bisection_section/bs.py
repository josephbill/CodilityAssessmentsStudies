def binary_search(sorted_list, target):
    # Initialize left and right pointers
    left = 0
    right = len(sorted_list) - 1
    
    while left <= right:
        # Calculate the middle index
        middle = (left + right) // 2
        print(middle, " item is " , sorted_list[middle])
        
        # Check if the middle element is equal to the target
        if sorted_list[middle] == target:
            return middle  # Target found, return its index
        
        # If the target is less than the middle element, search the left half
        elif sorted_list[middle] > target:
            right = middle - 1
            print("right" , right)
        
        # If the target is greater than the middle element, search the right half
        else:
            left = middle + 1
            print("left" , left)

    # Target not found in the list
    return -1

# Example usage
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = 6

result = binary_search(my_list, target_value)

if result != -1:
    print(f"Element {target_value} found at index {result}.")
else:
    print(f"Element {target_value} not found in the list.")
