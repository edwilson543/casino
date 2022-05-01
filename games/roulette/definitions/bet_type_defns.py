"""
To define a new bet type complete the following steps:
"""
from games.roulette.app.roulette_bet_base_class import RouletteBet
from games.roulette.app.roulette_wheel_base_class import WHEEL_TYPES
from games.roulette.constants.game_constants import Colour
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

    def determine_win_criteria(self) -> list[int]:
        """
        Returns: list of the slot numbers of the same colour as the input colour.
        Requires the bet_choice attribute to have already been set.
        """  # TODO update as for colours enum
        allowed_colours = set(self.playing_wheel.slots.values()).difference({self.playing_wheel.bias_colour})
        if self.bet_choice in allowed_colours:
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

    def determine_win_criteria(self) -> list[int]:
        """Returns: the bet_choice as a list (which for a colours bet will be an int).
        Requires the bet_choice attribute to have already been set."""
        bet_choice = self.bet_choice
        if bet_choice in self.playing_wheel.slots:
            return [bet_choice]
        else:
            raise ValueError(f"{self.bet_choice} is not a slot on the {self.playing_wheel.wheel_name} roulette wheel")


##########
# Add the newly defined user bet class to the BetTypeOptions Enum below
# Parameters imported live into game so don't instantiate
##########
class BetTypeOptions(Enum):
    COLOURS_BET = ColoursBet
    STRAIGHTUP_BET = StraightUpBet
