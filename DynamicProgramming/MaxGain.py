lookup = {}

def MaxGain(coins, gain_so_far=0):
    key = tuple(coins)
    if lookup.has_key(key):
        return lookup[key]

    result = gain_so_far

    if len(coins)==0:
        return gain_so_far
    else:
        choice_1 = coins[0]
        game_state_1 = GameState_after_opponents_move(coins[1:])

        choice_2 = coins[-1]
        game_state_2 = GameState_after_opponents_move(coins[:-1])

        result = max( MaxGain(game_state_1, gain_so_far + choice_1), MaxGain(game_state_2, gain_so_far + choice_2) )

    lookup[key] = result
    return result


def GameState_after_opponents_move(coins):
    result = []

    if len(coins)>1:
           choice_1 = coins[0]
           GameState_after_choice_1 = coins[1:]
           player1_gain_from_choice_1 = MaxGain(GameState_after_choice_1, choice_1)
           
           choice_2 = coins[-1]
           GameState_after_choice_2 = coins[:-1]
           player1_gain_from_choice_2 = MaxGain(GameState_after_choice_2, choice_2)

           "opponent plays such that he leaves minimum gain for player 1"
           if player1_gain_from_choice_1 > player1_gain_from_choice_2:
               result = GameState_after_choice_2
           else:
               result = GameState_after_choice_1

    return result


print MaxGain([8,15,3,7])





