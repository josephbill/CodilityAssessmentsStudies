def digit_sum(num):
    # Function to calculate the sum of digits of a number
    return sum(int(digit) for digit in str(num))

def solution(A):
    max_sum = -1
    digit_sums = {}
    
    for num in A:
        sum_of_digits = digit_sum(num)
        if sum_of_digits in digit_sums:
            # Calculate the sum of the two numbers with equal digit sums
            max_sum = max(max_sum, num + digit_sums[sum_of_digits])
        else:
            # Store the number's sum of digits
            digit_sums[sum_of_digits] = num
    
    return max_sum

# Examples
print(solution([51, 71, 17, 42]))  # Output should be 93
print(solution([42, 33, 60]))       # Output should be 102
print(solution([51, 32, 43]))       # Output should be -1
