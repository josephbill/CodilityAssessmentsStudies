'''
iterating means repeating some parts of your program.
for , while 

1. For loop 
used when repeating some operations a given number of times 
repeat an operation for each element within a collections (list, tuples, ranges and str)

syntax 
for variabletorepresentiterations in range(of repetitions)
    loop_body

the range is donated as 
range(lowest, highest + 1)
the range can also accept a third argument 
more formally the range syntax looks like this :: 
range(start,stop(highest+1), step)
0,n,2
- when having a 3rd argument , the sequence of values beginning with start 
- each consecutive value is increased by step
- the step should contain values smaller than stop (positive steps)
- or a value greater than stop (then use negative steps)

range(10,0, -1) represents the sequence 10,9,8,7....1
range(1,4,2) represents the sequence 1,3
we cannot omit start when we declare a step

In the range if the lowest value is 0 then you skip it in the syntax

list will have length 
use length for range 


Example question : We are given some positive integer n. Let’s compute the factorial of n and assign
it to the variable factorial. The factorial of n is n! = 1 · 2 · . . . · n. We can obtain it by
starting with 1 and multiplying it by all the integers from 1 to n

Let’s print a triangle made of asterisks (‘*’) separated by spaces. The triangle
# should consist of n rows, where n is a given positive integer, and consecutive rows should
# contain 1, 2, . . . , n asterisks. For example, for n = 4 the triangle should appear 
# as follows:
*
* *
* * *
* * * *

Example 2 with step : Let’s print a triangle made of asterisks (‘*’) separated by
spaces and consisting of n rows , but this time upside down, and make it symmetrical.
Consecutive rows should contain 2n − 1, 2n − 3, . . . , 3, 1 asterisks and 
should be indented by 0, 2, 4, . . . , 2(n − 1)
spaces. For example, for n = 4 the triangle should appear as follows:
              * * * * * * *
                * * * * *
                  * * *
                    * 

Pseudocode 
Triangle Orienation (make it upside down)
1. start at n = start from value of n decrement down : upside down 
Symmetrical Triangle 
with the widest row having 2n-1 asterisks
Spaces : indention
each row is indented with a specific number of spaces , the first row should have O spaces 

in code how do you interpret a space ? " "(space)
we need to concatenate the space with the asterisks print 
2(n − 1)

'''
x = 4
for i in range(x,0,-1):
    print(' ' * (x - i ) * 2  + "* " * (2 * i - 1))

# n = 4
# for z in range(1,n + 1):
#     print("* " * z)

# factorial = 1 
# n=5
# for i in range(1, n+1):
#     factorial *= i

# print(factorial)

# for i in range(2,10):
#     print("Looping!")
#     print(f"i is: {i}")
    

'''
while loop 
focuses on the condition which dictates the start or the end of a particular loop 
as long as the condition evaluated to true , the loop body is executed 
once it becomes false we exit the loop 

Example: Given a positive integer n, how can we count the number of digits in its decimal
representation? One way to do it is convert the integer into a string and count the characters.
Here, though, we will use only arithmetical operations instead. We can simply keep dividing
the number(n) by ten and count how many steps are needed to obtain 0.

given input : positive integer n 
whats the decimal representaiton of the positive integer 12345 

The decimal representation of a number refers to the
standard positional numeral system we commonly use, also known as the base-10 system.
In the decimal system, numbers are represented using 10 digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9.

Each digit's position in a number represents a power of 10. For example, in the number 123:
12345 
1 ten-thousands place (10:4)

The digit '1' is in the hundreds place (10^2),
The digit '2' is in the tens place (10^1),
The digit '3' is in the ones place (10^0).
Therefore, the decimal representation of a number refers to how it is expressed
 using these digits and their positional values in the base-10 system.

pseudocode 
0. we have a positive integer 
1. n/10 == 0 then the loop stops 
2. the final should be the number operations(number of divisions) needed to obtain 0

syntax 
while some_condition:
    loop body 
'''
# initialize a counter for the number of digits in its decimal representation
n = 5
result = 0
# the end of the loop is when n = 0 
# keep dividing number by 10 until it becomes 0 ,incrementing the result count each time 
while n != 0:
    n = n // 10 
    result += 1

print("Number of digits " , result)
