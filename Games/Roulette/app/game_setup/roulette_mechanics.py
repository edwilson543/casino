# TODO make the game structure into a class - transfer bulk of play into here
import sys


class RouletteInitiator:
    def __init__(self):
        pass

    def game_initiator(self):
        for attempt in range(10):  # initiate game
            user_ready = input("Type 'go' when ready to play \n--->")
            if user_ready == "go":
                break
        else:
            sys.exit("Too many invalid attempts - game over")

    def deposit_amount(self):
        for attempt in range(10):  # set deposit amount
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
        for attempt in range(10):  # select wheel
            wheel_choice = input("What wheel would you like to play on? \n[E]uropean, [O]ther\n--->")  # add options
            if wheel_choice == 'E':
                return wheel_choice
            else:
                print("Invalid wheel choice, please try again")
        else:
            sys.exit("Too many invalid attempts - game over")


class BetSelector:
    pass  # class that will select what type of bet is to be place


class BetPlace:
    pass  # class that given the type of bet will define what the bet actually is
    # Should output the bet in the same format as the spin output
    # can then test if spin in BetPlace.outcome()
