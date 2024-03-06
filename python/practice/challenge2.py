'''
Inputs 
   1. An array A of length N 
   2. Each element in A can be denoted as A[i]

Output 
   1. maximum sum of two numbers whose digits add up to an equal sum 
   2. if not present return -1 

Constraints 
   1. length of array 'a' :  work within the length 
   2. Each element in the array is an integer 

Requirements 
   1. return maximum sum of any two numbers in the list 
   2. the sum of digits of each element should be considered for finding the pairs 
   3. If no such pair return -1 git
   4. function should handle the constraints 

pseudocode 
1. iterate through the array : 
find the sum of each number i.e. digits of the elements to find the pairs (function to calculate the sum of digits of a number)
2. iterate through each number to check if the sums of the digits are equal 
3. store a reference(array , dict.) for the number digit sum , then we pick the pairs from the reference and get the sums of the pairs 
[51, 71, 17, 42]
{
  "6" : [51,42]
  "8" : [71,17]
}
4. track maximum sum found. 
5. return the maximum sum or -1 if theres no pair 
'''

def digitSum(num):
    # function to get the sum of digits of a number
    return sum(int(digit) for digit in str(num))

def solution(A):
    # max sum reference 
    max_sum = -1
    # reference for the sum results of the digits 
    digit_sum  = {}
    # iterating the array to get the maximum sum for the pairs 
    for num in A: 
        print(f"current num in A in iteration ${num}" )
        sum_of_digits = digitSum(num)
        print(f"current sum of digits for ${num} is ${sum_of_digits} ")
        # i need to store the above sum to the dictionary references 
        if sum_of_digits in digit_sum:
            print(f"current key in dict in iteration ${sum_of_digits}" )
            # calculate the sum of the two numbers with equal digit sums
            '''
               num : represents the current element in iteration 
                max_sum : represents the current maximum sum

              ---------------- max(max_sum, num + digit_sum[sum_of_digits])================
               sum_of_digits : represents the sum of that number 
               digit_sum[sum_of_digits] : retrieves the sum of the digits num  from the digits_sum dictionary

               max_sum, num + digit_sum[sum_of_digits]  : calculate the sum of the num and the sum of its digits 
               the function compares the current maximum sum of the number num and its digits sum and updates the maximum sum to be 
               the greater amongst the two values. 

               [51,71,17,42]
               1. max sum = -1 
               2. the sum is used as the key {"6" : [51,42], "8" : [71,17]}
               3. we compare the current max_sum to the new max_sum from the pair and update the max_sum with respective figure.
               ----------------------------------------------------------------------------
            '''
            # max_sum = max(max_sum  ,  num + digit_sum[sum_of_digits]) 
            # calculate the sum of the current number's digits 
            current_sum = num + digit_sum[sum_of_digits]
            print(f"{num} : {digit_sum[sum_of_digits]} : ${current_sum}")
            # update the max sum 
            max_sum = max(max_sum, current_sum)
        else:
            # store the sum in the dictionary reference
            digit_sum[sum_of_digits] = num
    
    return max_sum

print(solution([51, 71, 17, 42]))  # Output should be 93
print(solution([42, 33, 60]))       # Output should be 102
print(solution([51, 32, 43]))       # Output should be -1




