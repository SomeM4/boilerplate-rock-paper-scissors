# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    # If no history return "Paper" (Beats common "Rock" opening)
    if len(opponent_history) == 0:
        return "P" 
    
    # Strategy 1: Beats opponent play last
    last_opp = opponent_history[-1]
    
    # Strategy 2: Pattern Detection
    if len(opponent_history) >= 3:
        # If opponent last two move are the same, counter it
        if opponent_history[-1] == opponent_history[-2]:
            if last_opp == "R": return "P"
            if last_opp == "P": return "S"
            if last_opp == "S": return "R"
            
        # Check for cycles
        recent = opponent_history[-3::]
        if recent == ["R", "P", "S"] or recent == ["S", "P", "R"]:
            return "R"
        elif recent == ["P", "S", "R"] or recent == ["R", "S", "P"]:
            return "P"
            
    if last_opp == "R":
        return "P"
    elif last_opp == "P":
        return "S"
    elif last_opp == "S":
        return "R"
        
    return guess
