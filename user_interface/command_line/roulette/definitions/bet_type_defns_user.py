"""To define a new bet, first go to roulette->definitions->bet_type_defns"""
from games.roulette.definitions.bet_type_defns import ColoursBet, StraightUpBet
from games.roulette.app.roulette_wheel_base_class import WHEEL_TYPES
from games.roulette.constants.game_constants import Colour, ColourPrompts
from user_interface.command_line.roulette.app.roulette_bet_base_class_user import RouletteBetUser
from enum import Enum


##########
# Define 'get_user_bet_choice' method for each user bets
# Use MRO SpecificBetClass, RouletteBetUser (shouldn't be needed for now anyway)
##########
class ColoursBetUser(ColoursBet, RouletteBetUser):
    def __init__(self,
                 bet_type_name: str = None,
                 min_bet: int = None,
                 max_bet: int = None,
                 stake: int = None,
                 bet_choice: Colour = None,
                 win_criteria: list[int] = None,
                 payout: int = None,
                 playing_wheel: WHEEL_TYPES = None,
                 bet_choice_string_rep: str = None):
        super(RouletteBetUser, self).__init__(bet_type_name, min_bet, max_bet, stake, bet_choice, win_criteria, payout,
                                              playing_wheel)
        self.bet_choice_string_rep = bet_choice_string_rep

    def determine_valid_bet_choices_text(self):
        """"Returns: a string of all the valid colours bet options (i.e. excluding bias colour)"""
        colour_list = [colour.name for colour in super().determine_valid_bet_choices()]
        colour_options_text = ", ".join([getattr(ColourPrompts, colour).value for colour in colour_list])
        return colour_options_text

    def get_user_bet_choice(self) -> Colour:
        """
        Method to define the user's bet choice - they are required to enter a valid colour_id on the given wheel.
        Returns: user colour choice (as a member of the Colour Enum, e.g. Colour.RED
        """
        colour_options: set[Colour] = super().determine_valid_bet_choices()
        colour_options_text: str = self.determine_valid_bet_choices_text()
        while True:
            colour_choice = input(
                f"What colour would you like to bet on?\n{colour_options_text}\n--->").upper()
            try:
                colour_choice = Colour(colour_choice)
                if colour_choice in colour_options:
                    return colour_choice
                else:
                    print(f"{colour_choice} not a valid choice, please try again")
                    continue
            except ValueError or AttributeError:
                print(f"{colour_choice} not a valid choice, please try again")

    def get_bet_choice_string_rep(self) -> str:
        """String representation of the bet choice that has been made for feeding back to the user"""
        colour: str = getattr(self.bet_choice, "name").lower()
        return colour + " colours bet"  # on a ...


class StraightUpBetUser(StraightUpBet, RouletteBetUser):
    """Class for defining win criteria and payout for a straight-up bet"""

    def __init__(self,
                 bet_type_name: str = None,
                 min_bet: int = None,
                 max_bet: int = None,
                 stake: int = None,
                 bet_choice: int = None,
                 win_criteria: list[int] = None,
                 payout: int = None,
                 playing_wheel: WHEEL_TYPES = None,
                 bet_choice_string_rep: str = None):
        super(RouletteBetUser, self).__init__(bet_type_name, min_bet, max_bet, stake, bet_choice, win_criteria, payout,
                                              playing_wheel)
        self.bet_choice_string_rep = bet_choice_string_rep

    def determine_valid_bet_choices_text(self):
        """
        Returns: text string describing the numbers of the roulette wheel
        Example output form: '0 to 36 (inclusive)'
        Note this would need to change if defining a roulette wheel which skips numbers
        """
        min_number = min(list(set(self.playing_wheel.slots.keys())))
        max_number = max(list(set(self.playing_wheel.slots.keys())))
        return f"{min_number} to {max_number} (inclusive)"

    def get_user_bet_choice(self) -> int:
        """
        Method to define the user's bet choice - they are required to enter a valid slot number on the given wheel.
        Returns: user slots choice (as an int, example: 15).
        """
        number_options_range = super().determine_valid_bet_choices()
        number_options_text = self.determine_valid_bet_choices_text()
        while True:
            bet_choice = input(f"What number would you like to bet on?\nThe options are {number_options_text}.\n--->")
            try:
                bet_choice_int = int(bet_choice)
                if bet_choice_int in number_options_range:
                    return bet_choice_int
                else:
                    print(f"{bet_choice} is not a valid bet choice, please try again")
            except ValueError:
                print(f"{bet_choice} is not a valid bet choice, please try again")

    def get_bet_choice_string_rep(self) -> str:
        """String representation of the bet choice that has been made for feeding back to the user"""
        return "straight up bet on " + str(self.bet_choice)  # on a ...


##########
# Enum for storing all the bet classes
##########
class BetTypeOptionsUser(Enum):
    COLOURS_BET = ColoursBetUser
    STRAIGHTUP_BET = StraightUpBetUser
