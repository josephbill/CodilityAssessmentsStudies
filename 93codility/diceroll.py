# You have just rolled a dice several times. The N roll results that you remember are described by an array A. 
# However, there are F rolls whose results you have forgotten. 
# The arithmetic mean of all of the roll results (the sum of all the roll results divided by the number of rolls) equals M.
#  unknow Y : F amount of times  
# Number of rolls = len(A) + F
# M = sum of all results / numberofrolls
# M * numberofrolls = sum(A) + Y is repeated F amount of times 
# X - sum(A) = Y
# 4 = 12 + 2Y / 6
# 24 - 12 = 2Y
# 6 = Y
# f : 2 , 6, 6

# F is the same digit 
# Assumption is the number on calc. of the artithmetic mean is positive or absolute (6,4,3) : 3.25 , 3.45

# What are the possible results of the missing rolls?

# Write a function:

# def solution(A, F, M)

# that, given an array A of length N, an integer F and an integer M, returns an array containing possible results of the missed rolls. 
# The returned array should contain F integers from 1 to 6 (valid dice rolls). 
# If such an array does not exist then the function should return [0].

# Examples:
# 1. Given A = [3, 2, 4, 3, 6,6 ], F = 2, M = 4, your function should return [6, 6]. The arithmetic mean of all the rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 24 / 6 = 4.

# 2. Given A = [1, 5, 6, X , X , X , X], F = 4, M = 3, your function may return [2, 1, 2, 4] or [6, 1, 1, 1] (among others).

# 3. Given A = [1, 2, 3, 4], F = 4, M = 6, your function should return [0]. It is not possible to obtain such a mean.

# 4. Given A = [6, 1], F = 1, M = 1, your function should return [0]. It is not possible to obtain such a mean.

# Write an efficient algorithm for the following assumptions:

# N and F are integers within the range [1..100,000];
# each element of array A is an integer within the range [1..6];
# M is an integer within the range [1..6].


def solution(A, F, M):
    # Calculate the total number of rolls required
    total_rolls = len(A) + F

    # Calculate the total sum of desired outcomes
    total_outcome_sum = total_rolls * M

    # Calculate the sum of the given array A
    sum_of_A = sum(A)

    # Calculate the difference needed to achieve the desired mean
    difference = total_outcome_sum - sum_of_A

    # Calculate the value of each new roll needed to achieve the desired mean
    new_roll_value = difference / F

    # Check if the new roll value is valid (between 1 and 6)
    if new_roll_value < 1 or new_roll_value > 6:
        return [0]
    else:
        # Generate the final array with the correct distribution of the new roll value
        final_array = getNewArray(new_roll_value, F, difference)
        return final_array
    
# the get array assumes their is no remainder in operation 
# def getNewArray(r,f,d):
#     if  r < 1 or r > 6:
#         return [0]
#     else:
#         return [int(r)] * fs

def getNewArray(r, f, d):
    final_array = [int(r)] * f
    remaining_diff = d - int(r) * f
    
    # Distribute the remaining difference as evenly as possible
    for i in range(remaining_diff):
        final_array[i] += 1

    return final_array

# Examples
print(solution([1, 2, 3, 4], 4, 6))  # Output: [0]
print(solution([6, 1], 1, 1))          # Output: [0]
print(solution([1, 5,6], 4, 3))  # Output: [3,2,2,2]
print(solution([3,2,4,3], 2, 4))  # Output: [6,6]

