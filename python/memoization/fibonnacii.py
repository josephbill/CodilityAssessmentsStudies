# fibonnacci sequence without memoization 
# define the nth term of a fibonnaci sequece 
# Implicit memoization : cache the return value for similar inputs passed to function
fibonnaci_sequence = {}
def fibonnaci(n):
#  check if the result is in dict. for the nth term 
   if n in fibonnaci_sequence:
     return fibonnaci_sequence[n]

   if n == 1:
    return 1
   elif n == 2: 
     return 1 
   elif n > 2: 
    #  sequence dictates the that the elements are a sum of the previous two numbers in the sequence 
    value = fibonnaci(n-1) + fibonnaci(n-2)

    fibonnaci_sequence[n] = value

   return value


# above process is slow because of the recursive actions our algo. needs to make 
# e.g if the nth term is 5 , it means the fibonnacci(3) and fibonnaci(2) needs to be calculated 
# , indicating that recursive functions cause the delay


for n in range(1,101):
  print(n, ":" , fibonnaci(n))