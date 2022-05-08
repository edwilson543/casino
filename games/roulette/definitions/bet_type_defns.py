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
from games.roulette.constants.bet_constants import HighLowBetOptions, OddsEvensBetOptions
import numpy as np
from enum import Enum
from math import floor


##########
# Create subclass of RouletteBet base class to define each bet's 'determine_win_criteria' method
##########

##########
# Outside Bets
##########
class ColoursBet(RouletteBet):
    """Class for defining the valid bet choices and win criteria of a colours bet."""

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


class HighLowBet(RouletteBet):
    """Class for defining the valid bet choices and win criteria of a High and Low bet"""

    def __init__(self,
                 fixed_parameters: RouletteBetParameters,
                 stake: int = None,
                 bet_choice: HighLowBetOptions = None,
                 win_criteria: list[int] = None,
                 payout: int = None,
                 playing_wheel: WHEEL_TYPES = None):
        super().__init__(fixed_parameters, stake, bet_choice, win_criteria, payout, playing_wheel)

    def determine_valid_bet_choices(self) -> list:
        """Returns a range which specifies the valid number choices"""
        return [HighLowBetOptions.HIGH, HighLowBetOptions.LOW]

    def determine_win_criteria(self) -> list[int]:
        """Returns: the bet_choice as a list (which for a colours bet will be an int).
        Requires the bet_choice attribute to have already been set."""
        middle_slot = floor(self.playing_wheel.bias_wheel_size() / 2)
        relevant_slots = [slot_num for slot_num in self.playing_wheel.parameters.slots if
                          self.playing_wheel.parameters.slots[slot_num] != self.playing_wheel.parameters.bias_colour]
        if self.bet_choice == HighLowBetOptions.LOW:
            winnings_slots = [slot_num for slot_num in relevant_slots if slot_num <= middle_slot]
            return winnings_slots
        elif self.bet_choice == HighLowBetOptions.HIGH:
            winning_slots = [slot_num for slot_num in relevant_slots if slot_num > middle_slot]
            return winning_slots
        else:
            raise ValueError(f"{self.bet_choice} is not a valid high / low bet on the roulette wheel")


class OddsEvensBet(RouletteBet):
    """Class for defining the valid bet choices and win criteria of a Odds and Evens bet"""

    def __init__(self,
                 fixed_parameters: RouletteBetParameters,
                 stake: int = None,
                 bet_choice: OddsEvensBetOptions = None,
                 win_criteria: list[int] = None,
                 payout: int = None,
                 playing_wheel: WHEEL_TYPES = None):
        super().__init__(fixed_parameters, stake, bet_choice, win_criteria, payout, playing_wheel)

    def determine_valid_bet_choices(self) -> list:
        """Returns a range which specifies the valid number choices"""
        return [OddsEvensBetOptions.ODDS, OddsEvensBetOptions.EVENS]

    def determine_win_criteria(self) -> list[int]:
        """Returns: the bet_choice as a list (which for a colours bet will be an int).
        Requires the bet_choice attribute to have already been set."""
        relevant_slots = [slot_num for slot_num in self.playing_wheel.parameters.slots if
                          self.playing_wheel.parameters.slots[slot_num] != self.playing_wheel.parameters.bias_colour]
        if self.bet_choice == OddsEvensBetOptions.ODDS:
            winnings_slots = [slot_num for slot_num in relevant_slots if slot_num % 2 == 1]
            return winnings_slots
        elif self.bet_choice == OddsEvensBetOptions.EVENS:
            winning_slots = [slot_num for slot_num in relevant_slots if slot_num % 2 == 0]
            return winning_slots
        else:
            raise ValueError(f"{self.bet_choice} is not a valid odds or evens bet on the roulette wheel")


##########
# Inside Bets
##########

class StraightUpBet(RouletteBet):
    """Class for defining the valid bet choices and win criteria of a straight up bet"""

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
        """
        Returns: the bet_choice as a list (which for a straight up bet will be an individual int).
        Requires the bet_choice attribute to have already been set.
        """
        bet_choice = self.bet_choice
        if bet_choice in self.determine_valid_bet_choices():
            return [bet_choice]
        else:
            raise ValueError(f"{self.bet_choice} is not a slot on the "
                             f"{self.playing_wheel.parameters.wheel_name} roulette wheel")


class SplitBet(RouletteBet):
    """
    Class for defining the valid bet choices and win criteria of a split bet (a bet across the line between two tiles
    on the playing board).
    """

    def __init__(self,
                 fixed_parameters: RouletteBetParameters,
                 stake: int = None,
                 bet_choice: (int, int) = None,
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
            int_one_index_row, int_one_index_col = np.where(self.playing_wheel.parameters.board == int_one)
            int_two_index_row, int_two_index_col = np.where(self.playing_wheel.parameters.board == int_two)
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
        Method that takes an input tuple from self representing the split bet, and determines the win criteria of that
        bet in wheel slots terms. Seems a bit superfluous but it's a translation board -> wheel.
        """
        split_bet: (int, int) = self.bet_choice
        int_one = split_bet[0]
        int_two = split_bet[1]
        if self.determine_valid_bet_choices(int_one=int_one, int_two=int_two):
            return [int_one, int_two]
        else:
            raise ValueError(f"({int_one}, {int_two}) is not a valid split bet on the "
                             f"{self.playing_wheel.parameters.wheel_name} board.")


class CornersBet(RouletteBet):
    """
    Class for defining the valid bet choices and win criteria of a corners bet (a bet on the corner of four tiles on the
    playing board).
    """

    def __init__(self,
                 fixed_parameters: RouletteBetParameters,
                 stake: int = None,
                 bet_choice: (int, int, int, int) = None,
                 win_criteria: list[int] = None,
                 payout: int = None,
                 playing_wheel: WHEEL_TYPES = None):
        super().__init__(fixed_parameters, stake, bet_choice, win_criteria, payout, playing_wheel)

    def determine_valid_bet_choices(self, int_list: list[int, int, int, int]) -> bool:
        """
        Returns: a boolean value for whether ot not a given corners bet choice is allowed.
        i.e. determines whether or not the four tiles entered meet at a corner.
        """
        if any(isinstance(int_input, int) for int_input in int_list):
            raise TypeError(f"({int_list}) was passed to determine_valid_bet_choices"
                            f" in CornersBet class. One ore more element in the list is not of type int.")
        for tile in int_list:
            index_arr = np.array(np.where(self.playing_wheel.parameters.board == tile))
            if len(index_arr) == 0:
                raise ValueError(f"{tile} was passed as one of the tiles in "
                                 f"determine_valid_bet_choices in CornersBet class. This is not a tile on the: "
                                 f"{self.playing_wheel.parameters.wheel_name} playing board")
        else:
            int_list.sort()  # puts the ints in order top-left -> bottom-left -> top-right -> bottom_right
            neighbouring_rows = (int_list[0] + 1 == int_list[1]) and (int_list[2] + 1 == int_list[3])
            n_board_rows = np.shape(self.playing_wheel.parameters.board)[0]
            neighbouring_cols = (int_list[0] + n_board_rows == int_list[2]) and (
                        int_list[1] + n_board_rows == int_list[3])
            return neighbouring_rows and neighbouring_cols

    def determine_win_criteria(self) -> list[int]:
        """
        Method that takes the bet_choice and just returns it as is - superfluous in this instance, however must be
        included for completeness and integration with the bet placement/evaluation structure
        """
        corners_bet: list[int] = self.bet_choice
        if self.determine_valid_bet_choices(int_list=corners_bet):
            return corners_bet
        else:
            raise ValueError(f"({corners_bet}) is not a valid split bet on the "
                             f"{self.playing_wheel.parameters.wheel_name} board.")


##########
# Enum for storing all the bet classes
# Parameters imported live into game so don't instantiate
##########
class BetTypeOptions(Enum):
    COLOURS_BET = ColoursBet
    STRAIGHTUP_BET = StraightUpBet
    SPLIT_BET = SplitBet
    HIGH_LOW_BET = HighLowBet
    ODDS_EVENS_BET = OddsEvensBet
