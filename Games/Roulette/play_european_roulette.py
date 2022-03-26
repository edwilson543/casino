from Games.Roulette.app.game_setup.roulette_components import euro_wheel
import sys

active_wheel = None
user_pot = 0
active_bet_type = None
active_bet_mapping = {'C': 'colours', 'S': 'straight_up', 'O': 'other'}  # update to be imported from somewhere

"""
To become the game initiation base class: game_initiation, wheel_selection and deposit
"""

for attempt in range(10):  # initiate game
    user_ready = input("Type 'go' when ready to play \n--->")
    if user_ready == "go":
        break
else:
    sys.exit("Too many invalid attempts - game over")

for attempt in range(10):  # set deposit amount
    deposit_amount = input("How much would you like to deposit to play with (£)?"
                           "\nDeposits are allowed as real numbers \n--->") # should probably only allow >0
    try:
        user_pot = int(deposit_amount)
        break
    except ValueError:
        print('Invalid deposit amount - please try again')
else:
    sys.exit("Too many invalid attempts - game over")

for attempt in range(10):  # select wheel
    wheel_choice = input("What wheel would you like to play on? \n[E]uropean, [O]ther\n--->") # add options
    if wheel_choice == 'E':
        active_wheel = euro_wheel
        break
    else:
        print("Invalid wheel choice, please try again")
else:
    sys.exit("Too many invalid attempts - game over")

"""
To become the game play class: loop over bet type and stake
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