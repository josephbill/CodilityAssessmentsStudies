
def solution(X):
    # Implement your solution here
    # sort 
    difference_array = []
    sort_ed = sorted(X)
    for i in range(len(sort_ed) - 1):
        current_index = sort_ed[i]
        next_index = sort_ed[i + 1]
        difference = next_index - current_index
        difference_array.append(difference)
        current_index = next_index
        next_index = next_index + i

    result = max(difference_array)
    return result


print(solution([5,5,5,7,7,7]))