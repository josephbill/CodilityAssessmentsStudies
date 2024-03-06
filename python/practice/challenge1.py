'''
There are N boxes (numbered from 0 to N−1) arranged in a row. The K-th box contains A[K] bricks. In one move you can take one brick from some box and move it to a box next to it (on the left or on the right). What is the minimum number of moves needed to end up with exactly 10 bricks in every box?


Write a function:

function solution(A);

that, given an array A of N integers[n], returns the minimum number of moves needed to end up with exactly 10 bricks in every box. [box return , with exactly 10 bricks]
If this is not possible, the function should return −1.

Examples:

1. For A = [7, 15, 10, 8], the function should return 7. You can perform the following sequence of moves:
   - move three bricks from box number 1 to the box on the left: [10, 12, 10, 8];
   - move two bricks from box number 1 to the box on the right: [10, 10, 12, 8];
   - finally, move two bricks from box number 2 to the last box: [10, 10, 10, 10].


2. For A = [11, 10, 8, 12, 8, 10, 11], the function should return 6. You can perform the following sequence of moves:
    - move a brick from box number 0 to box number 2 (using two moves);
    - move a brick from the last box two positions to the left (using two moves);
    - move a brick from the middle box to each of its neighbors (another two moves).


3. For A = [7, 14, 10], the function should return −1. It is not possible to end up with exactly 10 bricks in each box.

1. Inputs 
    - a list of number received by the function, : a list of length N : length A = boxes. 
    - each element of 'A' denoted as [A][i] represents the number of bricks in that i'th box. 
    - reference to the number of moves -> move item to the box next to it (sequenced) - keep track of number of moves 
      (variable moves to keep track.)

      
2. Outputs 
    - -1 If this is not possible , having 10 bricks per box , the function should return −1.
    - if possible return the possible minimum number of moves to end up with exactly 10 bricks in every box

3. Constraints (keep consideration of.(limits))
   - input is a list : length of the input array is  > than 0
   - minimum number of moves is + 
   - the no of bricks in each box can range from 0 or > than : so make 10 bricks per box
   - only one brick can be moved per move : keep track by appending ::  moves += i
   - move in a sequence 0 to next

4. Requirements 
   - function should return minimum number of moves needed , or -1 
   - function should handle the constraints 

   pseudocode 

   1. define the function to take list A 
   2. find the sum of the total number of bricks ,  find if its divisible by 10 if not return -1 ?
   or   - nofboxes = len(A) 
        - multiply total number of boxes by 10 to check if the total number of bricks(sum of the list) is not equal to result.  
        - find if its divisible by 10 if not return -1 
    * also check if the total number of bricks in the whole list ,divided by the length of the entire list is divisible by 10 
    [100,50]
    150 / 2  : 75 = 10 

    [7,15,10,2]  = total number of bricks  =  34 /10  : no -1 
                  length / number of boxes =  4 

                  34 = 4 * 10  

                  [7, 15, 10, 8]  = 40 / 10 = 4 rem 0 : complete the set 
                   40 = 40
                   continue : completes the set 

                   ======== continue with logic or return -1 =============
    3. initialize a counter to track number reason   : moves = 0            
    4. iterate through each box to calculate the difference or excess btw the current and the targetted number of bricks 
      [7,6,10,8]
      0 , 7 - 10 : -3
      1 , 15 - 10 : 3 
    5. if bricks are excess : move excess bricks to next box and update the moves by the excess bricks.  
    6. if bricks are less than 10 : bring the deficit from the next box. update the moves by the deficit bricks. 
    7. return our number of moves. 


'''

def solution(A):
    # checking if possible to have 10 bricks in each box 
    total_bricks = sum(A)
    no_of_boxes = len(A)
    if total_bricks != 10 * no_of_boxes:
        return -1 
    # keep track of the moves 
    moves = 0
    # iterate over the boxes 
    for i in range(no_of_boxes):
        # check each brick for any deficit or excess
        if A[i] > 10:
            excess = A[i] - 10 
            # if any excess i move the excess to the brick 
            A[i] -= excess
            A[i + 1] += excess
            # update my moves 
            moves += excess
            #  deficit 
        elif A[i] < 10:
            deficit = 10 - A[i]
            # if any deficit , bring in the diff. from the next box 
            A[i] += deficit
            A[i + 1] -= deficit
            moves += deficit
    return moves 

print(solution([7,15,10,8])) # 7 
print(solution([11,10,8,12,8,10,11])) # 6 
print(solution([7,14,10])) # 1