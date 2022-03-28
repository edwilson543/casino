from Games.Roulette.definitions.wheel_defns import wheel_options, wheel_options_text
from Games.Roulette.definitions.bet_type_defns import bet_cats_and_types, bet_type_options_text, bet_cat_options_text
from Games.Roulette.definitions.bet_type_defns import bet_type_min_max_bet
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

    def choose_stake_amount(self, bet_type, user_funds):
        min_stake = bet_type_min_max_bet[bet_type]['min']
        max_stake = bet_type_min_max_bet[bet_type]['max']
        while True:
            stake = input("How much would you like to stake?\n"
                          f"Minimum stake: £{min_stake}, Maximum stake: £{max_stake}, integer stakes only\n--->")
            try:
                stake = int(stake.replace("£", ""))  # get rid of the £ sign if the user types one
                if stake > user_funds:
                    print(f"A £{stake} stake exceeds your current funds")
                    continue  # TODO Add some feature here to allow user to do a top up
                elif min_stake <= stake <= max_stake:
                    confirmation = input(f"Confirm your stake of £{stake}?\n"
                                         "[Y]es, [N]o \n--->")
                    if confirmation == 'N':
                        continue
                    print(f"£{stake} stake placed, time to choose your bet!")
                    return stake
                else:
                    print('Invalid stake - please try again and refer to bet criteria.')
            except ValueError:
                print('Invalid stake - please try again and refer to bet criteria.')


class RouletteWheelWagers:
    """
    Class for defining the different wagers on the roulette wheel.
    Should this be a subclass of the roulette wheel class/ should it be defined in base classes?
    """

    def __init__(self):
        self.place_bet_mapping = {'C': self.place_colours_bet(), 'S': self.place_straight_up_bet()}
        self.get_winning_set_mapping = {'C': self.get_winning_set_colours(), 'S': self.get_winning_set_straight_up()}

    def place_bet(self, wheel: RouletteWheel):
        """Function to take the place_bet_mapping and apply the relevant method"""
        pass

    def get_winning_set(self, wheel: RouletteWheel):
        """Function to take the get_winning_set_mapping and apply the relevant method"""
        pass

    def place_colours_bet(self, wheel: RouletteWheel):
        pass

    def get_winning_set_colours(self: RouletteWheel):
        pass

    def place_straight_up_bet(self: RouletteWheel):
        pass

    def get_winning_set_straight_up(self):
        pass