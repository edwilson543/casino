from Games.Roulette.definitions.wheel_defns import wheel_options, wheel_options_text
from Games.Roulette.definitions.bet_type_defns import bet_cats_and_types, bet_cat_options_text
from Games.Roulette.definitions.bet_type_defns import bet_type_options_text, bet_type_min_max_bet
from math import floor
from time import sleep


class RouletteInitiator:
    """
    Class to initiate the roulette game.
    Not sure if it's bad practice to use static methods like this?
    """

    def __init__(self, min_deposit: int, deposit_multiples: int):
        self.min_deposit = min_deposit
        self.deposit_multiples = deposit_multiples

    def game_initiator(self):
        """Method to initiate the game by getting the user to type 'go'"""
        while True:  # initiate game
            user_ready = input("Type 'GO' when ready to play \n--->").upper()
            if user_ready == "GO":
                break

    def deposit_amount(self):
        """
        Method to get the user to specify how much they want to deposit.
        Parameters need to be defined such that min_deposit % deposit_multiples should be 0
        """
        while True:
            deposit_amount = input("How much would you like to deposit to play with?\n"
                                   f"Deposits are allowed as multiples of £{self.deposit_multiples},"
                                   f"the minimum deposit is £{self.min_deposit}. \n--->")
            try:
                user_pot = int(deposit_amount.replace("£", ""))  # in case some types in e.g. £100 rather than 150
                if user_pot >= self.min_deposit and user_pot % self.deposit_multiples == 0:
                    confirmation = input(f"Are you sure you would like to deposit £{user_pot} to play with?\n"
                                         "[Y]es, [N]o \n--->").upper()
                    if confirmation != 'Y':
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
                return wheel_choice
            else:
                print("Invalid wheel choice, please try again")


class BetSelector:
    """class to allow users to select the type of bet to place
    note note yet to place the bet"""

    def __init__(self, wheel_id: str, player_funds: int):
        self.wheel_id = wheel_id
        self.player_funds = player_funds

    def choose_bet_category(self):
        while True:
            bet_cat = input("What category of bet would you like to place?"
                            f"\n{bet_cat_options_text[self.wheel_id]}\n--->").upper()
            if bet_cat in list(bet_cats_and_types[self.wheel_id].keys()):
                return bet_cat
            else:
                print("Not a valid bet category, try again")

    def choose_bet_type(self, bet_cat):
        while True:
            bet_type = input("What category of bet would you like to place?"
                             f"\n{bet_type_options_text[self.wheel_id][bet_cat]}\n--->").upper()
            if bet_type in bet_cats_and_types[self.wheel_id][bet_cat]:
                return bet_type
            else:
                print("Not a valid bet type, try again")

    def choose_stake_amount(self, bet_type):
        min_stake = bet_type_min_max_bet[self.wheel_id][bet_type]['min']
        max_stake = bet_type_min_max_bet[self.wheel_id][bet_type]['max']
        while True:
            stake = input("How much would you like to stake?\n"
                          f"Minimum stake: £{min_stake}, Maximum stake: £{max_stake}, integer stakes only.\n"
                          f"You have £{self.player_funds} left to play with.\n--->")
            try:
                stake = int(stake.replace("£", ""))  # get rid of the £ sign if the user types one
                if stake > self.player_funds:
                    print(f"A £{stake} stake exceeds your current funds")
                    continue  # TODO Add some feature here to allow user to do a top up or go all in
                elif min_stake <= stake <= max_stake:
                    confirmation = input(f"Confirm your stake of £{stake}?\n"
                                         "[Y]es, [N]o \n--->").upper()
                    if confirmation != 'Y':
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
    Each different bet is defined using two methods - a place_bet_type_bet and a get_winning_set_bet_type method.
    The place bet method is to navigate users to placing a bet.
    The get_winning_set is to get the set of tuples that if a spin falls in result in a win.
    The place_bet and get_winning_set methods then map each wheel and bet type onto the relevant methods
    """

    def __init__(self, bet_type_id: str, wheel_id: str, stake: int):  # Note mappings not initialised
        self.stake = stake
        self.bet_type_id = bet_type_id
        self.wheel_id = wheel_id

        self.wheel = wheel_options[self.wheel_id]
        self.place_bet_mapping = {'E': {'C': self.place_colours_bet, 'S': self.place_straight_up_bet},
                                  'A': {'C': self.place_colours_bet, 'S': self.place_straight_up_bet}}
        self.get_winning_set_mapping = {'E': {'C': self.get_winning_slots_colours,
                                              'S': self.get_winning_slots_straight_up},
                                        'A': {'C': self.get_winning_slots_colours,
                                              'S': self.get_winning_slots_straight_up}}

    def place_bet(self):
        """Method to take the place_bet_mapping and apply the relevant method"""
        return self.place_bet_mapping[self.wheel_id][self.bet_type_id]()

    def get_winning_slots(self, player_bet: list):
        """
        Parameters: player_bet is a generic list of one or more elements, which is a user specified bet. This is matched
        with the player_bet parameter within each specific bet method
        Method to take the get_winning_set_mapping and apply the relevant method"""
        return self.get_winning_set_mapping[self.wheel_id][self.bet_type_id](player_bet=player_bet)

    # Lower level methods for each specific bet, to be applied using the mapping methods above

    def place_colours_bet(self):
        """
        Returns:
        User bet_choice -  as a list for compatibly with other bet methods.
        potential_winnings of the bet - bet outcome is not determined, only what a bet win would return
        """
        while True:
            bet_choice = input(f"What colour would you like to bet on?\n{self.wheel.colour_options}\n--->").upper()
            if bet_choice in self.wheel.colour_ids.keys():
                potential_winnings = floor(self.stake * self.wheel.payout_scaler / (
                        self.wheel.colour_counts(self.wheel.colour_ids[bet_choice]) / self.wheel.wheel_size()))
                confirmation = input(f"Confirm £{self.stake} stake on {self.wheel.colour_ids[bet_choice]}?\n"
                                     f"Winning this bet will return: £{potential_winnings}"
                                     f"\n[Y]es, [N]o\n--->").upper()
                if confirmation != 'Y':
                    continue
                print(f"£{self.stake} stake placed on {self.wheel.colour_ids[bet_choice]}.")
                return [bet_choice], potential_winnings
            else:
                print("Invalid colour choice, please try again")

    def get_winning_slots_colours(self, player_bet: list):
        """
        Returns: a list of the slot numbers which are of the specified colour
        Note use of generic 'user_bet' is so that get_winning_slots has the same arguments as each different bet method
        """
        colour = self.wheel.colour_ids[player_bet[0]]
        # from the place_colours_bet method we know player_bet contains just one element
        return [slot_num for slot_num in self.wheel.slots.keys() if self.wheel.slots[slot_num] == colour]

    def place_straight_up_bet(self):
        number_options_text = self.wheel.user_number_options_text()
        number_options_range = self.wheel.user_number_options_range()
        while True:
            bet_choice = input(f"What number would you like to bet on?\nThe options are {number_options_text}.\n--->")
            try:
                bet_choice = int(bet_choice)
                if bet_choice in number_options_range:
                    potential_winnings = floor(self.stake * self.wheel.payout_scaler * self.wheel.wheel_size())
                    confirmation = input(f"Confirm £{self.stake} stake on {bet_choice}?\n"
                                         f"Winning this bet will return: £{potential_winnings}"
                                         f"\n[Y]es, [N]o\n--->").upper()
                    if confirmation != 'Y':
                        continue
                    print(f"£{self.stake} stake placed on {bet_choice}")
                    return [bet_choice], potential_winnings
                else:
                    print(f"{bet_choice} is not a valid bet choice, please try again")
            except ValueError:
                print(f"{bet_choice} is not a valid bet choice, please try again")

    def get_winning_slots_straight_up(self, player_bet: list):
        """Note this seems pointless but it's so that the get_winning_slots can be applied consistently."""
        return player_bet


class BetEvaluation:
    def __init__(self, potential_winnings: int, winning_slots: list, wheel_id: str):
        self.potential_winnings = potential_winnings
        self.winning_slots = winning_slots
        self.wheel_id = wheel_id
        self.wheel = wheel_options[wheel_id]

    def evaluate_bet(self):
        while True:
            user_ready = input("Type 'SPIN' to spin the wheel!\n--->").upper()
            if user_ready != "SPIN":
                print("Please try spinning the wheel again.")
                continue
            else:
                spin_outcome_num, spin_outcome_col = self.wheel.spin()
                print(f"Wheel spinning...")
                sleep(1)  # TODO could use these throughout. Could define a range of sleep times
                print(f"Ball has landed on {spin_outcome_num}, ({spin_outcome_col.upper()})!")
                sleep(1)
                if spin_outcome_num in self.winning_slots:
                    print(f"Congratulations! You have won £{self.potential_winnings}")
                    return self.potential_winnings
                else:
                    print("Better luck next time, your bet did not win.")
                    return 0


class GameContinuation:
    """
    Class to keep the game going until the user runs out of money or quits.
    We'll need some quick checks like play on same wheel, new bet type, top up etc.
    The purpose will be to map users to where they need to be within the existing mechanics.
    """
    pass
