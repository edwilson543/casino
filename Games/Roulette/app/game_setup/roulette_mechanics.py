# TODO make the game structure into a class - transfer bulk of play into here
from Games.Roulette.definitions.wheel_defns import wheel_options, wheel_options_text
from Games.Roulette.definitions.bet_type_defns import bet_cats_and_types, bet_type_options_text, bet_cat_options_text
from Games.Roulette.app.roulette_base_classes import RouletteWheel


class RouletteInitiator:
    """class to initiate the roulette game"""

    def __init__(self):
        pass

    def game_initiator(self):
        """Method to initiate the game by getting the user to type 'go'"""
        while True:  # initiate game
            user_ready = input("Type 'go' when ready to play \n--->")
            if user_ready == "go":
                break

    def deposit_amount(self, min_deposit: int, deposit_multiples: int):
        """
        Method to get the user to specify how much they want to deposit.
        Parameters need to be defined such that min_deposit % deposit_multiples should be 0
        """
        while True:
            deposit_amount = input("How much would you like to deposit to play with?\n"
                                   f"Deposits are allowed as multiples of £{deposit_multiples},"
                                   f"the minimum deposit is £{min_deposit}. \n--->")
            try:
                user_pot = int(deposit_amount.replace("£", ""))  # incase some types in e.g. £100 rather than 150
                if user_pot >= min_deposit and user_pot % deposit_multiples == 0:
                    confirmation = input(f"Are you sure you would like to deposit £{user_pot} to play with?\n"
                                         "[Y]es, [N]o \n--->")
                    if confirmation == 'N':
                        continue
                    print(f"You have deposited £{user_pot} to play with")
                    return user_pot
                else:
                    print('Invalid deposit amount - please try again and refer to deposit criteria.')
            except ValueError:
                print('Invalid deposit amount - please try again and refer to deposit criteria.')

    def wheel_choice(self):
        """Method to allow the user to input what wheel they would like to play on"""
        while True:
            wheel_choice = input("What wheel would you like to play on?\n"
                                 f"{wheel_options_text}\n--->").upper()  # upper to allow for lower case
            if wheel_choice in list(wheel_options.keys()):
                return wheel_options[wheel_choice]
            else:
                print("Invalid wheel choice, please try again")


class BetSelector:
    """class to allow users to select the type of bet to place
    note note yet to place the bet"""

    def __init__(self):
        pass

    def choose_bet_category(self):
        while True:
            bet_cat = input("What category of bet would you like to place?"
                            f"\n{bet_cat_options_text}\n--->").upper()
            if bet_cat in list(bet_cats_and_types.keys()):
                return bet_cat
            else:
                print("Not a valid bet category, try again")

    def choose_bet_type(self, bet_cat):
        while True:
            bet_type = input("What category of bet would you like to place?"
                             f"\n{bet_type_options_text[bet_cat]}\n--->").upper()
            if bet_type in bet_cats_and_types[bet_cat]:
                return bet_type
            else:
                print("Not a valid bet type, try again")


class BetPlacer:
    """Class that given the type of bet will define what the bet actually is, including stake"""
    def __init__(self, bet_type: str):
        self.bet_type = bet_type

    def stake_amount(self):
        """
        Method to get the user to specify how much they want to bet.
        Parameters need to be defined such that min_deposit % deposit_multiples should be 0
        """
        pass



class BetOutcome:
    pass  # to move in the roulette wheel subclass and make this a class
