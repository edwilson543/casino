# TODO make the game structure into a class - transfer bulk of play into here
import sys
from Games.Roulette.constants.bet_type_mapping import active_bet_mapping

attempts = 25  # default acceptance of keyboard spam before sys exit


class RouletteInitiator:
    """class to initiate the roulette game"""

    def __init__(self):
        pass

    def game_initiator(self):
        for attempt in range(attempts):  # initiate game
            user_ready = input("Type 'go' when ready to play \n--->")
            if user_ready == "go":
                break
        else:
            sys.exit("Too many invalid attempts - game over")

    def deposit_amount(self):
        for attempt in range(attempts):  # set deposit amount
            deposit_amount = input("How much would you like to deposit to play with (£)?"
                                   "\nDeposits are allowed as real numbers \n--->")  # should probably only allow >0
            try:
                user_pot = int(deposit_amount)
                return user_pot
            except ValueError:
                print('Invalid deposit amount - please try again')
        else:
            sys.exit("Too many invalid attempts - game over")

    def wheel_choice(self):
        for attempt in range(attempts):  # select wheel
            wheel_choice = input("What wheel would you like to play on? \n[E]uropean, [O]ther\n--->")  # add options
            if wheel_choice == 'E':
                return wheel_choice
            else:
                print("Invalid wheel choice, please try again")
        else:
            sys.exit("Too many invalid attempts - game over")


class BetSelector:
    """class to allow users to select the type of bet to place
    note note yet to place the bet"""

    def __init__(self):
        pass

    def choose_bet_type(self):
        # TODO split this into bet category then bet type"""
        for attempt in range(attempts):  # choose bet category
            bet_cat = input("What category of bet would you like to place?"
                            "\n[I]nside or [O]utside \n--->")
            if bet_cat in ['I', 'O']:
                if bet_cat == 'I':
                    for attempt_ind in range(attempts):  # choose specific bet type
                        bet_type = input("What type of bet would you like to place?"
                                         "\n[C]olour or [O]ther \n--->")  # update options
                        if bet_type in ['C', 'O']:
                            active_bet_type = active_bet_mapping[f"{bet_type}"]
                            return active_bet_type
                        else:
                            print("Not a valid bet type, try again")
                    else:
                        sys.exit("Too many invalid attempts - game over")
                elif bet_cat == 'O':
                    for attempt_ind in range(attempts):  # choose specific bet type
                        bet_type = input("What type of bet would you like to place?"
                                         "\n[S]traight_up or [O]ther \n--->")  # update options
                        if bet_type in ['S', 'O']:
                            active_bet_type = active_bet_mapping[f"{bet_type}"]
                            return active_bet_type
                        else:
                            print("Not a valid bet type, try again")
            else:
                print("Not a valid bet category, try again")
        else:
            sys.exit("Too many invalid attempts - game over")


class BetPlace:
    pass  # class that given the type of bet will define what the bet actually is
    # Should output the bet in the same format as the spin output
    # can then test if spin in BetPlace.outcome()

class BetOutcome:
    pass # to move in the roulette wheel subclass and make this a class
