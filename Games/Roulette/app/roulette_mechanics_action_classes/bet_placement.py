from Games.Roulette.definitions.wheel_defns import wheel_options
from math import floor


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
        potential_winnings of the bet - bet outcome is not determined, only what a bet win would return. This is
        calculated based on the 'fake' probability of winning, i.e. ignoring the bias_colour.
        """
        while True:
            bet_choice = input(f"What colour would you like to bet on?\n{self.wheel.colour_options}\n--->").upper()
            if bet_choice in self.wheel.colour_ids.keys():
                potential_winnings = self.stake * floor(
                    1 / (self.wheel.colour_counts(self.wheel.colour_ids[bet_choice]) / self.wheel.bias_wheel_size()))
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
        Paramaters:
        player_bet: in format e.g. ['R'] where R is the colour_id for the colour red
        Returns:
        A list of the slot numbers which are of the specified colour
        Note use of generic 'user_bet' is so that get_winning_slots has the same arguments as each different bet method
        """
        colour = self.wheel.colour_ids[player_bet[0]]
        # from the place_colours_bet method we know player_bet contains just one element
        return [slot_num for slot_num in self.wheel.slots if self.wheel.slots[slot_num] == colour]

    def place_straight_up_bet(self):
        number_options_text = self.wheel.user_number_options_text()
        number_options_range = self.wheel.user_number_options_range()
        while True:
            bet_choice = input(f"What number would you like to bet on?\nThe options are {number_options_text}.\n--->")
            try:
                bet_choice = int(bet_choice)
                if bet_choice in number_options_range:
                    potential_winnings = self.stake * floor(self.wheel.bias_wheel_size())
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
