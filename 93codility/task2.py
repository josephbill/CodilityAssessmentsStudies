# You have just rolled a dice several times. The N roll results that you remember are described by an array A. However, there are F rolls whose results you have forgotten. The arithmetic mean of all of the roll results (the sum of all the roll results divided by the number of rolls) equals M.

# What are the possible results of the missing rolls?

# Write a function:

# def solution(A, F, M)

# that, given an array A of length N, an integer F and an integer M, returns an array containing possible results of the missed rolls. The returned array should contain F integers from 1 to 6 (valid dice rolls). If such an array does not exist then the function should return [0].

# Examples:

# 1. Given A = [3, 2, 4, 3], F = 2, M = 4, your function should return [6, 6]. The arithmetic mean of all the rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 24 / 6 = 4.

# 2. Given A = [1, 5, 6], F = 4, M = 3, your function may return [2, 1, 2, 4] or [6, 1, 1, 1] (among others).

# 3. Given A = [1, 2, 3, 4], F = 4, M = 6, your function should return [0]. It is not possible to obtain such a mean.

# 4. Given A = [6, 1], F = 1, M = 1, your function should return [0]. It is not possible to obtain such a mean.

# Write an efficient algorithm for the following assumptions:

# N and F are integers within the range [1..100,000];
# each element of array A is an integer within the range [1..6];
# M is an integer within the range [1..6].