"""
To define a new bet type complete the following steps:
1) Define a class for that bet as a subclass of RouletteBet, adding the methods as shown for the
existing bets below
2) Add the bet to the BetTypeOptions Enum at the bottom
3) Define parameters for that bet in bet_constants, as is done for the existing bets.
4) To add to command line UI, define a user class for that bet in bet_type_defns_user,
in the same way as is done for the existing bets.
"""
from games.roulette.app.roulette_bet_base_class import RouletteBet, RouletteBetParameters
from games.roulette.app.roulette_wheel_base_class import WHEEL_TYPES
from games.roulette.constants.game_constants import Colour
from numpy import where
from enum import Enum


##########
# Create subclass of RouletteBet base class to define each bet's 'determine_win_criteria' method
##########
class ColoursBet(RouletteBet):
    """Class for defining the win criteria of a colours bet."""

    def __init__(self,
                 fixed_parameters: RouletteBetParameters,
                 stake: int = None,
                 bet_choice: Colour = None,
                 win_criteria: list[int] = None,
                 payout: int = None,
                 playing_wheel: WHEEL_TYPES = None):
        super().__init__(fixed_parameters, stake, bet_choice, win_criteria, payout, playing_wheel)

    def determine_valid_bet_choices(self) -> set[Colour]:
        """Returns: a set of all the valid colours bet options (i.e. excluding bias colour)"""
        colour_options = set(self.playing_wheel.parameters.slots.values()).difference(
            {self.playing_wheel.parameters.bias_colour})
        return colour_options

    def determine_win_criteria(self) -> list[int]:
        """
        Returns: list of the slot numbers of the same colour as the input colour.
        Requires the bet_choice attribute to have already been set.
        """
        colour_options = self.determine_valid_bet_choices()
        if self.bet_choice in colour_options:
            return [slot_num for slot_num in self.playing_wheel.parameters.slots if
                    self.playing_wheel.parameters.slots[slot_num] == self.bet_choice]
        else:
            raise ValueError(f"{self.bet_choice} is not a permitted colours bet on the "
                             f"{self.playing_wheel.parameters.wheel_name} roulette wheel")


class StraightUpBet(RouletteBet):
    """Class for defining the win criteria for a straight up bet"""

    def __init__(self,
                 fixed_parameters: RouletteBetParameters,
                 stake: int = None,
                 bet_choice: Colour = None,
                 win_criteria: list[int] = None,
                 payout: int = None,
                 playing_wheel: WHEEL_TYPES = None):
        super().__init__(fixed_parameters, stake, bet_choice, win_criteria, payout, playing_wheel)

    def determine_valid_bet_choices(self) -> range:
        """Returns a range which specifies the valid number choices"""
        min_number = min(list(set(self.playing_wheel.parameters.slots.keys())))
        max_number = max(list(set(self.playing_wheel.parameters.slots.keys())))
        return range(min_number, max_number + 1)  # + 1 to capture highest numbered slot

    def determine_win_criteria(self) -> list[int]:
        """Returns: the bet_choice as a list (which for a colours bet will be an int).
        Requires the bet_choice attribute to have already been set."""
        bet_choice = self.bet_choice
        if bet_choice in self.determine_valid_bet_choices():
            return [bet_choice]
        else:
            raise ValueError(f"{self.bet_choice} is not a slot on the "
                             f"{self.playing_wheel.parameters.wheel_name} roulette wheel")


class SplitBet(RouletteBet):
    """Class for defining the win criteria of a colours bet."""

    def __init__(self,
                 fixed_parameters: RouletteBetParameters,
                 stake: int = None,
                 bet_choice: Colour = None,
                 win_criteria: list[int] = None,
                 payout: int = None,
                 playing_wheel: WHEEL_TYPES = None):
        super().__init__(fixed_parameters, stake, bet_choice, win_criteria, payout, playing_wheel)

    def determine_valid_bet_choices(self, int_one: int, int_two: int) -> bool:
        """
        Returns: a boolean value for whether ot not a given split bet choice is allowed.
        i.e. determines whether or not two numbers on the roulette board are adjacent (horizontally or vertically).
        """
        if not (isinstance(int_one, int) and isinstance(int_two, int)):
            raise TypeError(f"({int_one}, {int_two}) was passed to determine_valid_bet_choices in SplitBet class."
                            f"One ore more of these inputs is not of type int.")
        else:
            int_one_index_row, int_one_index_col = where(self.playing_wheel.parameters.board == int_one)
            int_two_index_row, int_two_index_col = where(self.playing_wheel.parameters.board == int_two)
            if len(int_one_index_row) == 0 or len(int_two_index_row) == 0:
                raise ValueError(f"({int_one}, {int_two}) was passed to determine_valid_bet_choices in SplitBet class."
                                 f"At least one of these numbers is nt on the "
                                 f"{self.playing_wheel.parameters.wheel_name} playing board")
            else:
                row_offset = abs(int_one_index_row - int_two_index_row)
                col_offset = abs(int_one_index_col - int_two_index_col)
                if (row_offset == 0 and col_offset == 1) or (col_offset == 0 and row_offset == 1):
                    return True  # Entered numbers are adjacent on the playing board
                else:
                    return False  # Entered numbers are not adjacent on the playing board

    def determine_win_criteria(self) -> list[int]:
        """
        Method that takes an input tuple representing an edge bet, and determines the win criteria of that bet
        in wheel terms. Seems a bit superfluous but it's a translation board -> wheel.
        """
        split_bet: (int, int) = self.bet_choice
        int_one = split_bet[0]
        int_two = split_bet[1]
        if self.determine_valid_bet_choices(int_one=int_one, int_two=int_two):
            return [int_one, int_two]
        else:
            raise ValueError(f"({int_one}, {int_two}) is not a valid split bet on the "
                             f"{self.playing_wheel.parameters.wheel_name} board")


##########
# Add the newly defined user bet class to the BetTypeOptions Enum below
# Parameters imported live into game so don't instantiate
##########
class BetTypeOptions(Enum):
    COLOURS_BET = ColoursBet
    STRAIGHTUP_BET = StraightUpBet
    SPLIT_BET = SplitBet
