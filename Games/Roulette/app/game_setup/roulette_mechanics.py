from Games.Roulette.definitions.wheel_defns import wheel_options, wheel_options_text
from Games.Roulette.definitions.bet_type_defns import bet_cats_and_types, bet_type_options_text, bet_cat_options_text
from Games.Roulette.definitions.bet_type_defns import bet_type_min_max_bet
from Games.Roulette.app.roulette_base_classes import RouletteWheel
import math  # seems unideal to import whole module but just importing floor from math gave an error when called


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
                return wheel_choice, wheel_options[wheel_choice]
            else:
                print("Invalid wheel choice, please try again")


class BetSelector:
    """class to allow users to select the type of bet to place
    note note yet to place the bet"""

    def __init__(self):
        pass

    def choose_bet_category(self, wheel_id: str):
        while True:
            bet_cat = input("What category of bet would you like to place?"
                            f"\n{bet_cat_options_text[wheel_id]}\n--->").upper()
            if bet_cat in list(bet_cats_and_types[wheel_id].keys()):
                return bet_cat
            else:
                print("Not a valid bet category, try again")

    def choose_bet_type(self, bet_cat, wheel_id: str):
        while True:
            bet_type = input("What category of bet would you like to place?"
                             f"\n{bet_type_options_text[wheel_id][bet_cat]}\n--->").upper()
            if bet_type in bet_cats_and_types[wheel_id][bet_cat]:
                return bet_type
            else:
                print("Not a valid bet type, try again")

    def choose_stake_amount(self, bet_type, user_funds, wheel_id: str):
        min_stake = bet_type_min_max_bet[wheel_id][bet_type]['min']
        max_stake = bet_type_min_max_bet[wheel_id][bet_type]['max']
        while True:
            stake = input("How much would you like to stake?\n"
                          f"Minimum stake: £{min_stake}, Maximum stake: £{max_stake}, integer stakes only\n--->")
            try:
                stake = int(stake.replace("£", ""))  # get rid of the £ sign if the user types one
                if stake > user_funds:
                    print(f"A £{stake} stake exceeds your current funds")
                    continue  # TODO Add some feature here to allow user to do a top up or go all in
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
    Each different bet is defined as its own method #TODO write explanation here
    """

    def __init__(self, bet_type_id: str, wheel_id: str, stake: int):  # Note mappings not initialised
        self.stake = stake
        self.bet_type_id = bet_type_id
        self.wheel_id = wheel_id
        self.place_bet_mapping = {'E': {'C': self.place_colours_bet, 'S': self.place_straight_up_bet},
                                  'D': {'C': self.place_colours_bet, 'S': self.place_straight_up_bet}}
        self.get_winning_set_mapping = {'E': {'C': self.get_winning_set_colours, 'S': self.get_winning_set_straight_up},
                                        'D': {'C': self.get_winning_set_colours, 'S': self.get_winning_set_straight_up}}

    def place_bet(self):  # TODO do not include wheel as parameter
        """Method to take the place_bet_mapping and apply the relevant method"""
        return self.place_bet_mapping[self.wheel_id][self.bet_type_id]()

    def get_winning_set(self, wheel: RouletteWheel):
        """Method to take the get_winning_set_mapping and apply the relevant method"""
        pass

    # Lower level methods for each specific bet

    def place_colours_bet(self):
        wheel = wheel_options[self.wheel_id]
        colour_options = wheel.user_colour_options()
        colour_dict = wheel.generate_colour_ids()
        while True:
            bet_choice = input(f"What colour would you like to bet on?\n {colour_options}\n--->").upper()
            if bet_choice in colour_dict.keys():
                confirmation = input(f"Confirm £{self.stake} stake on {colour_dict[bet_choice]}?\n"
                                     f"Winning this bet will return: £"
                                     f"{math.floor(self.stake / (wheel.colour_counts(colour_dict[bet_choice]) / wheel.wheel_size()))}"
                                     f"\n[Y]es, [N]o\n--->").upper()
                if confirmation == 'N':
                    continue
                print(f"£{self.stake} stake placed on {colour_dict[bet_choice]}!")
                return bet_choice
            else:
                print("Invalid colour choice, please try again")

    def get_winning_set_colours(self):
        print('winning_set')
        pass

    def place_straight_up_bet(self):
        pass

    def get_winning_set_straight_up(self):
        pass
