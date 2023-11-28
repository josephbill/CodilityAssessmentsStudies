def solution(A):
    # First, check if it is possible to have 10 bricks in each box
    #check to actual check if we can have 10 bricks in all boxes 
    total_bricks = sum(A)
    n_boxes = len(A)
    if total_bricks != 10 * n_boxes:
        return -1

    moves = 0
    # Iterate over the boxes
    for i in range(n_boxes):
        # If the current box has more than 10 bricks,
        # We need to move the excess to the next boxes
        if A[i] > 10:
            excess = A[i] - 10
            A[i] -= excess
            A[i+1] += excess
            moves += excess
        # If the current box has less than 10 bricks,
        # We need to bring the required number from the next boxes
        elif A[i] < 10:
            deficit = 10 - A[i]
            A[i] += deficit
            A[i+1] -= deficit
            moves += deficit
    return moves

# Examples
print(solution([7, 15, 10, 8]))  # Should return 7
print(solution([11, 10, 8, 12, 8, 10, 11]))  # Should return 6
print(solution([7, 14, 10]))  # Should return -1