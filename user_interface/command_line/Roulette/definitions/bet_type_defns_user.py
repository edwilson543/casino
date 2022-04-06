from user_interface.command_line.Roulette.app.roulette_wheel_base_class_user import RouletteWheelUser
from Games.Roulette.definitions.bet_type_defns import ColoursBet, StraightUpBet

"""UI classes that inherit from the relevant class in bet_type_defns
These classes are to add the UI that allows users to make their bet choice."""


class ColoursBetUser(ColoursBet):
    def __init__(self,
                 min_bet: int = 5,
                 max_bet: int = 50,
                 bet_type_id: str = 'C',
                 win_criteria: list = None,
                 payout: int = None,
                 playing_wheel_id: str = None,
                 wheel: RouletteWheelUser = None):
        super().__init__(min_bet, max_bet, bet_type_id, win_criteria, payout, playing_wheel_id, wheel)

    def get_user_bet_choice(self):
        """
        Method to define the user's bet choice
        Returns: user colour choice (as a string)
        """
        while True:
            bet_choice = input(
                f"What colour would you like to bet on?\n{self.playing_wheel.colour_options}\n--->").upper()
            if bet_choice in self.playing_wheel.colour_ids.keys():
                bet_choice_colour = self.playing_wheel.colour_ids[bet_choice]
                confirmation = input(f"Confirm bet on {bet_choice_colour}\n?"
                                     f"[Y]es, [N]o\n--->").upper()
                if confirmation != 'Y':
                    continue
                print(f"Bet placed on {bet_choice_colour}!")
                return bet_choice_colour
            else:
                print("Invalid colour choice, please try again")


class StraightUpBetUser(StraightUpBet):
    """Class for defining win criteria and payout for a straight up bet"""

    def __init__(self,
                 min_bet: int = 10,
                 max_bet: int = 20,
                 bet_type_id: str = 'S',
                 win_criteria: list = None,
                 payout: int = None,
                 playing_wheel_id: str = None,
                 playing_wheel: RouletteWheelUser = None):
        super().__init__(min_bet, max_bet, bet_type_id, win_criteria, payout, playing_wheel_id, playing_wheel)

    def get_user_bet_choice(self):
        number_options_text = self.playing_wheel.user_number_options_text()
        number_options_range = self.playing_wheel.user_number_options_range()
        while True:
            bet_choice = input(f"What number would you like to bet on?\nThe options are {number_options_text}.\n--->")
            try:
                bet_choice_int = int(bet_choice)
                if bet_choice_int in number_options_range:
                    confirmation = input(f"Confirm bet on {bet_choice_int}\n?"
                                         f"[Y]es, [N]o\n--->").upper()
                    if confirmation != 'Y':
                        continue
                    print(f"Bet placed on {bet_choice_int}!")
                    return bet_choice_int
                else:
                    print(f"{bet_choice} is not a valid bet choice, please try again")
            except ValueError:
                print(f"{bet_choice} is not a valid bet choice, please try again")


###################
# Add the newly defined user bet class to the bet_type_options dictionary below
###################
bet_type_options_user = {'C': ColoursBetUser(), 'S': StraightUpBetUser()}
