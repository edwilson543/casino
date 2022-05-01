"""To define a new bet, first go to roulette->definitions->bet_type_defns"""
from games.roulette.definitions.bet_type_defns import ColoursBet, StraightUpBet
from games.roulette.app.roulette_wheel_base_class import WHEEL_TYPES
from games.roulette.constants.game_constants import Colour
from user_interface.command_line.roulette.app.roulette_bet_base_class_user import RouletteBetUser
from typing import Union
from enum import Enum


##########
# Define 'get_user_bet_choice' method for each user bets
# Use MRO RouletteBetUser, SpecificBetClass (shouldn't be needed for now anyway)
##########
class ColoursBetUser(RouletteBetUser, ColoursBet):
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

    def get_user_bet_choice(self) -> str:
        """
        Method to define the user's bet choice - they are required to enter a valid colour_id on the given wheel.
        Returns: user colour choice (as a string, example: 'red').
        """
        colour_options: set[Colour] = self.playing_wheel.generate_colour_options()
        colour_options_text: str = self.playing_wheel.generate_colour_options_text()
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


class StraightUpBetUser(RouletteBetUser, StraightUpBet):
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

    def get_user_bet_choice(self) -> int:
        """
        Method to define the user's bet choice - they are required to enter a valid slot number on the given wheel.
        Returns: user slots choice (as an int, example: 15).
        """
        number_options_text = self.playing_wheel.generate_number_options_text()
        number_options_range = self.playing_wheel.generate_number_options_range()
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
