# pseudocode bit of this : 
# <!-- What's are the knows -->
# 1. n is a positive integer (absolute)
# 2. printing starts at 1 
# 3. printing ends at 4
# 4. value increase by 1 on each iteration 
# 5. space between asterisks (format for the output)
# 6. n represents the rows 
# range(start,stop,step)

def solution(n):
    for i in range(1,n+1):
        row = ''
        for j in range(1,i + 1):
            row += "* "
        print(row)

print(solution(4))
        
def upside_down(n):
    for i in range(n,0,-1):
        row = ' '.join(["*" for j in range(i)])
        print(row)

print(upside_down(4))


arrayofnumbers = [1,2,3,4,5]

for num in range(len(arrayofnumbers)):
    print(arrayofnumbers[num])


n = 4 
for i in range(1,n+1):
    print(i)


def negative(temperatures):
    days = 0
    for t in temperatures:
        print(t)
        if t < 0:
            days += 1
    return days

print(negative([6, 7, 8, 8]))  # Output: 0
