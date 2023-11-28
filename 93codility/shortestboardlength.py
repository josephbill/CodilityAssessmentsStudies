# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# i think a binary search to find shortest broad length 
# a helper method to check whether it's actually possible to fill all holes with given broad length 
def solution(A):
    # Implement your solution here
    # helper function to check if i can cover all holes using a bisection search
    def can_i_cover_all_holes(mid):
        need_boards = 0
        last_index = A[0]

        for position in A:
            #check if distance between the current position and last position is 
            #greater than mid point 
            if position - last_index > mid:
                need_boards += 1
                last_index = position

        return need_boards
    #sort for binary search 
    A.sort()
    #intial low and high bounds for search 
    low, high = 1, A[-1] - A[0] + 1
    #perfoming search for shortest board length 
    while low < high:
        mid = (low + high) // 2

        if can_i_cover_all_holes(mid) <= 1:
            high = mid
        else:
            low = mid + 1

    return low
