def find_leader(n):
    candidate = None 
    count = 0

# getting our candidate 
    for num in n:
        if count == 0:
            candidate = num
            count = 1 
        elif num == candidate:
            count += 1
        else:
            count -= 1

#  count appearances 
    count_candidate = n.count(candidate)
    #  leader check : is the count greater than half the size of the sequence 
    if count_candidate > len(n) / 2:
        return candidate
    else:
       return None


nums = [2,2,1,1,1,2,2,1]
result = find_leader(nums)

if result:
    print("majority element " , result)
else: 
    print("no majority found")