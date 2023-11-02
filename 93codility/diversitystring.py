def solution(N):
    # get from 26 the occurances of uniqueness that we can get 
    # reptition of the distincts letters 
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                'n','o','p','q','r','s','t','u','v','w','x','y','z']
    if N <= 26:
        return ''.join(chr(97 + i) for i in range(N))
    
    # maximum number of distinct letters 
    max_letters = 1
    for i in range(1,len(alphabet)): # 26 letters 
        if N % i == 0:
            max_letters = i 
    print(max_letters)
    # repetition 
    repetition = N // max_letters
    print(repetition)

    # result 
    result = ''
    for i in range(max_letters):
        result += chr(97 + i) * repetition

    return result 



print(solution(31))
