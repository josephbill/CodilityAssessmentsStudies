# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # keep track of the longest switch
    max_slice = 1
    # a single element is always switching so current_slice can be 1 
    current_slice = 1 
    # checking my array to check for equality between the elemtents 
    for i in range(1, len(A)):
        if A[i] == A[i - 1]:
            #increase current length 
            current_slice += 1 
        else:
            #if not equal , update the max slice if current slice is longer 
            max_slice = max(max_slice,current_slice)
            # reset current slice to length 1 for the new switch cycle 
            current_slice = 1
    # outside this loop , I need to update the max slice in case the longest slice ends at the last element 
    max_slice = max(max_slice,current_slice)
    return max_slice
