#  You are going to build a stone wall. The wall should be straight and N meters long, and its thickness should be constant; however, it should have different heights in different places. The height of the wall is specified by an array H of N positive integers. H[I] is the height of the wall from I to I+1 meters to the right of its left end. In particular, H[0] is the height of the wall's left end and H[N−1] is the height of the wall's right end.

# The wall should be built of cuboid stone blocks (that is, all sides of such blocks are rectangular). Your task is to compute the minimum number of blocks needed to build the wall.

# Write a function:

# def solution(H)

# that, given an array H of N positive integers specifying the height of the wall, returns the minimum number of blocks needed to build it.

# For example, given array H containing N = 9 integers:

#   H[0] = 8    H[1] = 8    H[2] = 5
#   H[3] = 7    H[4] = 9    H[5] = 8
#   H[6] = 7    H[7] = 4    H[8] = 8
# the function should return 7


# pseudo

# The given problem involves determining the minimum number of stone blocks needed to build a stone wall with specified heights. Let's break down the subproblems involved in solving this task:

# Computing Differences in Heights:

# Calculate the differences in heights between adjacent elements of the array H. This helps identify where the wall changes in height.
# Identifying Peaks and Valleys:

# Identify the peaks and valleys in the height differences. Peaks represent the start of a new block, and valleys represent the end of a block.
# Counting Blocks:

# Count the number of blocks needed based on the peaks and valleys. Each peak requires a new block, and each valley represents the end of a block.
# Handling Edge Cases:

# Consider edge cases, such as the first and last elements of the height array, which are treated as peaks and valleys respectively.
# Implementing the Solution:

# Write a function (e.g., solution(H)) that incorporates the above steps to return the minimum number of blocks needed to build the wall.

# Identifying peaks and valleys in the height differences involves finding the positions in the array where the height changes from increasing to decreasing (peak) or from decreasing to increasing (valley). Here's a step-by-step approach to achieve this:

# Initialize an empty stack to keep track of the peaks and valleys.

# Iterate through the heights in the array, comparing each height to the previous one.

# If the current height is greater than the previous height, it indicates a potential peak. Push the current height's index onto the stack.

# If the current height is less than the previous height, it indicates a potential valley. Pop heights from the stack until a height that is less than or equal to the current height is encountered. Each popped index corresponds to the end of a block (valley).

# Count the number of blocks based on the number of peaks and valleys.

def identify_peaks_and_valleys(heights):
    stack = []  # Initialize an empty stack to track peaks and valleys
    blocks = 0  # Initialize the number of blocks

    for i in range(len(heights)):
        # Pop heights from the stack until a valley is encountered
        while stack and heights[i] < stack[-1]:
            stack.pop()
            blocks += 1

        # If the current height is greater, it's a potential peak
        if not stack or heights[i] > stack[-1]:
            stack.append(heights[i])

    # Each remaining height in the stack corresponds to a peak
    blocks += len(stack)
    return blocks

# Example usage
heights = [8, 8, 5, 7, 9, 8, 7, 4, 8]
min_blocks = identify_peaks_and_valleys(heights)
print("Minimum number of blocks needed:", min_blocks)  # Output: 7
