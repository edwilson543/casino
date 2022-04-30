from games.bet_base_class import Bet
from games.roulette.app.roulette_wheel_base_class import WHEEL_TYPES
from games.roulette.app.roulette_wheel_base_class import wheel_spin_return
from games.roulette.constants.bet_constants import WheelBetParameters

from math import floor
from typing import Union


# TODO update all type hints to use Typevars - bet_choice probably one to do
class RouletteBet(Bet):
    """
    Each bet on the roulette wheel will be defined as a subclass of this class.
    RouletteBet <- RouletteBetUser | +
    RouletteBet <- ColoursBet, StraightUpBet, ... | + determine_win_criteria
    ColoursBetUser,... -< ColoursBet & RouletteBetUser
    """

    def __init__(self,
                 bet_type: str,
                 min_bet: int = None,
                 max_bet: int = None,
                 stake: int = None,
                 bet_choice: Union[int, str, list] = None,
                 win_criteria: list[int] = None,
                 payout: int = None,
                 playing_wheel: WHEEL_TYPES = None):
        super().__init__(bet_type, min_bet, max_bet, stake, bet_choice, win_criteria, payout)
        self.playing_wheel = playing_wheel

    def set_playing_wheel(self, wheel: WHEEL_TYPES):
        """Method to set the playing_wheel attribute of the bet"""
        self.playing_wheel = wheel

    def set_min_max_bet(self):
        """
        Method to look up the min/max bet of the roulette bet, which is specific to the wheel, from the
        WheelBetParameters, and then set these as instance attributes for the min/max bet.
        Note this method will only work on subclasses of this class, whose name corresponds to the underlying data,
        once the wheel has already been set
        """
        all_wheel_bet_data = getattr(WheelBetParameters, self.playing_wheel.wheel_name)
        bet_data = getattr(all_wheel_bet_data, self.bet_type)
        min_bet = bet_data.min_bet
        max_bet = bet_data.max_bet
        self.set_min_bet(amount=min_bet)
        self.set_max_bet(amount=max_bet)

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
