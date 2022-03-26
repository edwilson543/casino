from Games.Roulette.app.game_setup.roulette_components import euro_wheel
from Games.Roulette.app.game_setup.roulette_mechanics import RouletteInitiator
import sys

active_wheel = None
user_pot = 0
active_bet_type = None
active_bet_mapping = {'C': 'colours', 'S': 'straight_up', 'O': 'other'}  # update to be imported from somewhere

play_setup = RouletteInitiator()
play_setup.game_initiator()
user_pot = play_setup.deposit_amount()
print(user_pot) # just to check its working
active_wheel = play_setup.wheel_choice()
print(active_wheel) # just to check its working

"""
To become the bet selector and bet place class: loop over bet type and stake
"""

for attempt in range(10):  # choose bet type
    bet_type = input("What type of bet would you like to place?"
                     "\n[I]nside or [O]utside \n--->")
    if bet_type in ['I', 'O']:
        if bet_type == 'I':
            for attempt_ind in range(10):  # choose specific bet type
                bet_type = input("What type of bet would you like to place?"
                                 "\n[C]olour or [O]ther \n--->")  # update options
                if bet_type in ['C', 'O']:
                    active_bet_type = active_bet_mapping[f"{bet_type}"]
                    break
                else:
                    print("Not a valid bet type, try again")
            else:
                sys.exit("Too many invalid attempts - game over")
            break
        elif bet_type == 'O':
            for attempt_ind in range(10):  # choose specific bet type
                bet_type = input("What type of bet would you like to place?"
                                 "\n[S]traight_up or [O]ther \n--->")  # update options
                if bet_type in ['S', 'O']:
                    active_bet_type = active_bet_mapping[f"{bet_type}"]
                break
            else:
                print("Not a valid bet type, try again")
            break
    else:
        print("Not a valid bet type, try again")
else:
    sys.exit("Too many invalid attempts - game over")

print(active_bet_type)

# active bet needs to be expanded down to

# TODO finish script - while deposit>0 just loop over the bet script, once it has feature to change pot
