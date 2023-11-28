rows = 4
number = 1

for i in range(1, rows + 1):
    # Print spaces before the numbers
    for j in range(rows - i):
        print(" ", end=" ")

    # Print numbers in the current row
    for j in range(i):
        print(number, end=" ")
        number += 1

    # Move to the next line after each row
    print()