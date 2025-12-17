# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    # If no history return "Paper" (Beats common "Rock" opening)
    if len(opponent_history) == 0:
        return "P" 
    
    
        
    return guess
