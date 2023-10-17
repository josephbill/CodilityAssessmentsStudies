def print_asters(n):
    for i in range(1, n + 1):
        row = " "
        for j in range(1, i + 1):
             row += "* "
        print(row)
    

print(print_asters(4))


# upside down print 
def upside_down(n):
    for i in range(n, 0, -1):  # Reverse the loop order
        row = ' '.join(['*' for _ in range(i)])  # Create the row with asterisks
        print(row)

print_asters(4)

print(upside_down(4))
