from games.bet_base_class import Bet
from games.roulette.app.roulette_wheel_base_class import WHEEL_TYPES
from games.roulette.app.roulette_wheel_base_class import wheel_spin_return

from math import floor
from typing import Union, TypeVar
from abc import abstractmethod
from dataclasses import dataclass


##########
# Data class for storing all the known roulette bet parameters
##########
@dataclass(frozen=True)
class RouletteBetParameters:
    """
    Class to specify all roulette bet parameters that are independent of choice i.e. known upfront.
    Note these can be wheel specific - to do so, define a new instance of this data class specific to a given wheel.
    """
    bet_type_name: str
    min_bet: int
    max_bet: int


# TODO update all type hints to use Typevars - bet_choice probably one to do
##########
# Base class defining a generic roulette bet
##########
class RouletteBet(Bet):
    """
    Each bet on the roulette wheel will be defined as a subclass of this class.
    RouletteBet <- RouletteBetUser | +
    RouletteBet <- ColoursBet, StraightUpBet, ... | + determine_win_criteria
    ColoursBetUser,... -< ColoursBet & RouletteBetUser
    """

    def __init__(self,
                 bet_type_name: str = None,
                 min_bet: int = None,
                 max_bet: int = None,
                 stake: int = None,
                 bet_choice: Union[int, str, list] = None,
                 win_criteria: list[int] = None,
                 payout: int = None,
                 playing_wheel: WHEEL_TYPES = None):
        super().__init__(bet_type_name, min_bet, max_bet, stake, bet_choice, win_criteria, payout)
        self.playing_wheel = playing_wheel

    @abstractmethod
    def determine_valid_bet_choices(self, *args, **kwargs):
        """
        Abstract method for determining the valid bet choices of a given bet.
        Defined differently for each specific roulette bet (e.g. ColoursBet) in bet_type_defns.
        """
        raise NotImplementedError("Call to determine_valid_bet_choices referred to RouletteBet super class")

    @abstractmethod
    def determine_win_criteria(self, *args, **kwargs):
        """
        Abstract method for calculating the win criteria of a given bet.
        Defined differently for each specific roulette bet (e.g. ColoursBet) in bet_type_defns.
        """
        raise NotImplementedError("Call to determine_win_criteria referred to RouletteBet super class")

    def set_playing_wheel(self, wheel: WHEEL_TYPES):
        """Method to set the playing_wheel attribute of the bet"""
        self.playing_wheel = wheel

    def calculate_payout(self):
        """
        Calculates the payout of a £1 roulette bet, (unit_payout) and multiplies this by the stake.
        This is determined by using the bias_wheel_size (which ignores the 'bias_colour') when calculating the
        probability of winning, so that the return always reflects a degree of the house always wins.

        Requires the win_criteria (and thus bet_choice) attribute to have already been set
        """
        win_probability_over_estimate = len(self.win_criteria) / self.playing_wheel.bias_wheel_size()
        unit_payout = floor(1 / win_probability_over_estimate)
        return unit_payout * self.stake

    def evaluate_bet(self, spin_outcome: wheel_spin_return) -> int:
        """
        Method to determine the outcome of spinning the wheel, relative to the bet_choice.
        Parameters: bet_choice - this is used to call the method 'determine_win_criteria' of the bet subclass,
        which returns a list of integers specific to the input format of the bet placement
        Returns:
        spin_outcome_num: an integer representing the slot of the roulette wheel the ball landed on
        spin_outcome_col: a string representing the colour of the roulette wheel the ball landed on
        winnings: either 0 or x>0, depending on whether the user won their bet

        Requires all attributes to have been set
        """
        if spin_outcome.number_return in self.win_criteria:
            return self.payout
        else:
            return 0


##########
# Typevar to be used when referencing bets in type hints throughout game
##########
BET_TYPES = TypeVar(name="BET_TYPES", bound=RouletteBet)
