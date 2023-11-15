def solution(skills):
    n = len(skills)
    results = [1] * n
    
    # start from round 1
    current_round = 1
    
    # Keep track of the matches for each round
    current_matches = list(range(n))
    
    # Continue until we have a single winner
    while len(current_matches) > 1:
        next_matches = []
        
        # Iterate through the matches to find winners and losers
        for i in range(0, len(current_matches) - 1, 2):
            # Compare the skill levels of the two players
            if skills[current_matches[i]] > skills[current_matches[i + 1]]:
                winner = current_matches[i]
                loser = current_matches[i + 1]
            else:
                winner = current_matches[i + 1]
                loser = current_matches[i]
            
            # The winner moves on to the next round
            next_matches.append(winner)
            
            # Record the current round as the last round the loser participated in
            results[loser] = current_round
        
        # Prepare for the next round
        current_matches = next_matches
        
        # Increment the round if there are still matches to be played
        if len(current_matches) > 1:
            current_round += 1
    
    # The winner has participated in all the rounds
    results[current_matches[0]] = current_round
    
    return results


print(solution([2,3,4,5,6,7]))


