### Stacks 
LIFO : Last in first out 
In this data structure insertion of the elements takes place at the top and deletion of the elements also takes place at the top. 
[1,2,3] : append , pop , size 

### Queues 
FIFO :  first in first out 
In this d.s new elements are inserted from the back but old elements are removed from the front 
[1]
.append()
.pop(0)

O(1)


breakout room question 

Problem: Fish in the River
[2,3]  A : size of the fish 
[0,1]  B : indications on swimming movement : 0 : upstream , 1: downstream. 

You are given two non-empty arrays A and B representing N voracious fish in a river, ordered from upstream to downstream. Array A contains the sizes of the fish, and array B contains the directions (0 for upstream, 1 for downstream) of the fish. If two fish move in opposite directions and there are no other (living) fish between them, they will eventually meet each other. Compute the number of fish that will stay alive.

Write a function:

python
Copy code

def solution(A, B):
    # your code here

that, given two non-empty arrays A and B of N integers, returns the number of fish that will stay alive.

For example, given the arrays A = [4, 3, 2, 1, 5] and B = [0, 1, 0, 0, 0], the function should return 4, as four fishes (4,2,1,5) will stay alive.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [0..1,000,000,000];
each element of array B is either 0 or 1, where 0 represents upstream and 1 represents downstream.
