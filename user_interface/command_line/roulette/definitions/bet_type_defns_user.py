"""To define a new bet, first go to roulette->definitions->bet_type_defns"""
from games.roulette.definitions.bet_type_defns import ColoursBet, StraightUpBet
from games.roulette.constants.bet_constants import BetTypeIds
from user_interface.command_line.roulette.app.roulette_bet_base_class_user import RouletteBetUser
from user_interface.command_line.roulette.definitions.wheel_defns_user import USER_WHEEL_TYPES
from typing import Union, TypeVar
from enum import Enum


##########
# Typevar to be used when referencing user bets in type hints throughout game
##########
USER_BET_TYPES = TypeVar(name="USER_BET_TYPES", bound=RouletteBetUser)


##########
# Define 'get_user_bet_choice' method for each user bets
# Use MRO RouletteBetUser, SpecificBetClass (shouldn't be needed for now anyway)
##########
class ColoursBetUser(RouletteBetUser, ColoursBet):
    def __init__(self,
                 min_bet: int = None,
                 max_bet: int = None,
                 stake: int = None,
                 bet_choice: Union[int, str, list] = None,
                 win_criteria: list[int] = None,
                 payout: int = None,
                 playing_wheel: USER_WHEEL_TYPES = None):
        bet_type: str = BetTypeIds.COLOURS_BET.name
        super(ColoursBet, self).__init__(bet_type, min_bet, max_bet, stake,
                         bet_choice, win_criteria, payout, playing_wheel)

    def get_user_bet_choice(self) -> str:
        """
        Method to define the user's bet choice - they are required to enter a valid colour_id on the given wheel.
        Returns: user colour choice (as a string, example: 'red').
        """
        while True:
            bet_choice = input(
                f"What colour would you like to bet on?\n{self.playing_wheel.colour_options}\n--->").upper()
            if bet_choice in self.playing_wheel.colour_ids:
                bet_choice_colour = self.playing_wheel.colour_ids[bet_choice]
                return bet_choice_colour
            else:
                print(f"{bet_choice} not a valid choice, please try again")


class StraightUpBetUser(RouletteBetUser, StraightUpBet):
    """Class for defining win criteria and payout for a straight-up bet"""

    def __init__(self,
                 min_bet: int = None,
                 max_bet: int = None,
                 stake: int = None,
                 bet_choice: Union[int, str, list] = None,
                 win_criteria: list[int] = None,
                 payout: int = None,
                 playing_wheel: USER_WHEEL_TYPES = None):
        bet_type = BetTypeIds.STRAIGHTUP_BET.name
        super(StraightUpBet, self).__init__(bet_type, min_bet, max_bet, stake,
                         bet_choice, win_criteria, payout, playing_wheel)

    def get_user_bet_choice(self) -> int:
        """
        Method to define the user's bet choice - they are required to enter a valid slot number on the given wheel.
        Returns: user slots choice (as an int, example: 15).
        """
        number_options_text = self.playing_wheel.user_number_options_text()
        number_options_range = self.playing_wheel.user_number_options_range()
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


##########
# Enum for storing all the bet classes
##########
class BetTypeOptionsUser(Enum):
    COLOURS_BET = ColoursBetUser()
    STRAIGHTUP_BET = StraightUpBetUser()

