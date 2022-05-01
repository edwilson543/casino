"""
To define a new bet type complete the following steps:
"""
from games.roulette.app.roulette_bet_base_class import RouletteBet
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
                 bet_type_name: str,
                 min_bet: int = None,
                 max_bet: int = None,
                 stake: int = None,
                 bet_choice: Colour = None,
                 win_criteria: list[int] = None,
                 payout: int = None,
                 playing_wheel: WHEEL_TYPES = None):
        super().__init__(bet_type_name, min_bet, max_bet, stake,
                         bet_choice, win_criteria, payout, playing_wheel)

    def determine_valid_bet_choices(self) -> set[Colour]:
        """Returns: a set of all the valid colours bet options (i.e. excluding bias colour)"""
        colour_options = set(self.playing_wheel.slots.values()).difference({self.playing_wheel.bias_colour})
        return colour_options

    def determine_win_criteria(self) -> list[int]:
        """
        Returns: list of the slot numbers of the same colour as the input colour.
        Requires the bet_choice attribute to have already been set.
        """
        colour_options = self.determine_valid_bet_choices()
        if self.bet_choice in colour_options:
            return [slot_num for slot_num in self.playing_wheel.slots if
                    self.playing_wheel.slots[slot_num] == self.bet_choice]
        else:
            raise ValueError(f"{self.bet_choice} is not a permitted colours bet on the "
                             f"{self.playing_wheel.wheel_name} roulette wheel")


class StraightUpBet(RouletteBet):
    """Class for defining the win criteria for a straight up bet"""

    def __init__(self,
                 bet_type_name: str,
                 min_bet: int = None,
                 max_bet: int = None,
                 stake: int = None,
                 bet_choice: int = None,
                 win_criteria: list[int] = None,
                 payout: int = None,
                 playing_wheel: WHEEL_TYPES = None):
        super().__init__(bet_type_name, min_bet, max_bet, stake,
                         bet_choice, win_criteria, payout, playing_wheel)

    def determine_valid_bet_choices(self) -> range:
        """Returns a range which specifies the valid number choices"""
        min_number = min(list(set(self.playing_wheel.slots.keys())))
        max_number = max(list(set(self.playing_wheel.slots.keys())))
        return range(min_number, max_number + 1)  # + 1 to capture highest numbered slot

    def determine_win_criteria(self) -> list[int]:
        """Returns: the bet_choice as a list (which for a colours bet will be an int).
        Requires the bet_choice attribute to have already been set."""
        bet_choice = self.bet_choice
        if bet_choice in self.determine_valid_bet_choices():
            return [bet_choice]
        else:
            raise ValueError(f"{self.bet_choice} is not a slot on the {self.playing_wheel.wheel_name} roulette wheel")

class SplitBet(RouletteBet):
    """Class for defining the win criteria of a colours bet."""

    def __init__(self,
                 bet_type_name: str,
                 min_bet: int = None,
                 max_bet: int = None,
                 stake: int = None,
                 bet_choice: Colour = None,
                 win_criteria: list[int] = None,
                 payout: int = None,
                 playing_wheel: WHEEL_TYPES = None):
        super().__init__(bet_type_name, min_bet, max_bet, stake,
                         bet_choice, win_criteria, payout, playing_wheel)

    def determine_valid_bet_choices(self, int_one: int, int_two: int) -> bool:
        """
        Returns: a boolean value for whether ot not a given split bet choice is allowed.
        i.e. determines whether or not two numbers on the roulette board are adjacent (horizontally or vertically).
        """
        try:
            int_one_index_row, int_one_index_col = where(self.playing_wheel.board == int_one)
            int_two_index_row, int_two_index_col = where(self.playing_wheel.board == int_two)
            if int_one_index_row.item() == int_two_index_row.item() or int_one_index_col.item() == int_two_index_col.item():
                return True
            else:
                return False
        except ValueError:
            pass


    def determine_win_criteria(self) -> list[int]:
        """
        Returns: list of the slot numbers of the same colour as the input colour.
        Requires the bet_choice attribute to have already been set.
        """
        colour_options = self.determine_valid_bet_choices()
        if self.bet_choice in colour_options:
            return [slot_num for slot_num in self.playing_wheel.slots if
                    self.playing_wheel.slots[slot_num] == self.bet_choice]
        else:
            raise ValueError(f"{self.bet_choice} is not a permitted colours bet on the "
                             f"{self.playing_wheel.wheel_name} roulette wheel")


##########
# Add the newly defined user bet class to the BetTypeOptions Enum below
# Parameters imported live into game so don't instantiate
##########
class BetTypeOptions(Enum):
    COLOURS_BET = ColoursBet
    STRAIGHTUP_BET = StraightUpBet
