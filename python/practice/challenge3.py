# I must make sure that the above is done the minimum amount of times
# Therefore, organized the numbers in the list a as follows.

# 1) I split the numbers in a to groups
# Numbers that need bricks and numbers that have an excess of bricks
# Numbers that need bricks are stored in a list called needy_li
# Numbers that have an excess of bricks are stored in an array called excess_li

# 2) I split organized both these lists according to their indexes in a.
# greatest index in a to lowest index in a

# Let me point out that for each member of excess_li I have the following information [value,index,needs] in a list
# as shown and in the order shown, and for each memeber of excess_li I have [value,index,excess]. Where value is
# the given number in a, index is the index of the given number in the list, needs is the bricks needed and excess
# is the number of bricks that can be given

# Now I loop over each element in exess_li:
# Every time I loop I do the following:
# I am going to give bricks to all the elements in the needy_li
# I will do this untill the given element in excess_li has no more bricks to give that I why I have a while loop 
# that says that loop so long as can_give > 0
# for a given iteration of the while loop I split I used an as follows:
# if can give is greater than the amount of bricks needed.
# elif can_give is less than needy_needs.

# If if statement is truthy then i am sure that the number of bricks to be given is equal to needy_needs
# if elif statement is truthy and if is falsy then I know the number of bricks beeing given is equal to can_give

# So then if we look back to the section of very important variables and calculations we know that the moves is 
# calculated by getting the absolute value of the difference between the indexes of the needy_num and the rich_num
# (this is the steps each brick need to move) and then multiplying it by the amount of bricks being given,
# which we have found above using the if and the elif
# Once we get this product, we know this product is equal to the number of moves, therfore I cumulatively add this 
# to a variable I called total moves
# Finally after looping over every element in excess list I know I am done, therefore I just return the total moves.



# Code:

def index_organizer(e):
    return e[1]



def question_one(a):
    total_of_a = 0
    for x in a:
        total_of_a += x
    
    if(total_of_a % 10 != 0):
        return -1
    needy_li = []
    excess_li = []
    for index, value in enumerate(a):
        new_li = []
        if value < 10:
            needs = 10 - value
            new_li = [value,index,needs]
            needy_li.append(new_li)
        elif value > 10:
            excess = value - 10
            new_li = [value,index,excess]
            excess_li.append(new_li)
    
# Now I am going to need to sort these according to the their indexes.
# Greatest index to the lowest index
    needy_li.sort(key = index_organizer, reverse = True)
    excess_li.sort(key = index_organizer, reverse = True)
    print(needy_li)
    print(excess_li)
   
    
    total_moves = 0
    for x in excess_li:
        can_give = x[2]
        i = 0
        while can_give > 0:
            needy = needy_li[i]
            needy_num = needy[0]
            needy_needs = needy[2]
            if can_give >= needy_needs:
                moves = abs(x[1] - needy[1]) * needy_needs
                needy_num -=needy_needs
                can_give -= needy_needs
                needy_needs = 0
                print(i)
                
                
                print(moves)
                total_moves += moves
                del needy_li[i]
               
                
                
            elif can_give < needy_needs:
                moves = can_give * abs(x[1] - needy[1])
                needy_num -=needy_needs
                
                needy_needs -= can_give
                print(moves)
                can_give = -1
                total_moves += moves
    return total_moves
                 

# TEST CASES  
# As you run the test cases please remember not to indent invocation of function: 
question_one([12,10,12,15,8,7,6]) # I did it manually and also got 30.
# question_one([7, 15, 10, 8])
# question_one([11, 10, 8, 12, 8, 10, 11])
# question_one([7, 14, 10])