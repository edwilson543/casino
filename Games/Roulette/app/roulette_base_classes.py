from Games.games_base_classes import Bet
from math import floor
import numpy as np


class RouletteWheel:
    """Base class for the roulette wheel - from which we can define different wheel configurations"""

    def __init__(self,
                 slots: dict,
                 colour_ids: dict,
                 colour_options: str,
                 bias_colour: str):
        """
        Parameters
        __________
        slots: slot of the roulette wheel -
        should be passed as a dictionary, with the numbers as keys and the colours as the values
        colour_ids: a mapping of colour id (e.g. 'R') to each colour (e.g. 'red')
        colour_options: a string used to get user input on what colour they'd like to bet on
        bias_colour: the colour whose counts are ignored when calculating stake returns. e.g. if you have a 37 slot
        wheel and one slot is green, then stakes are calculated from probabilities as 1/(x/36).
        """
        self.slots = slots
        self.colour_ids = colour_ids
        self.colour_options = colour_options
        self.bias_colour = bias_colour

    def spin(self):
        """Returns: One random spin of the wheel as a dictionary, with number and colour as the key/value pairs"""
        min_slot = min(self.slots.keys())
        max_slot = max(self.slots.keys())
        number_return = np.random.randint(low=min_slot, high=max_slot + 1)
        # note the randint interval is half-open hence need of the + 1
        colour_return = self.slots[number_return]
        return number_return, colour_return

    def bias_wheel_size(self) -> int:
        """
        Returns: The number of slots on the wheel, minus a count of the number of slots of biased colours.
        The purpose is so that when calculating the return for a bet, the bias wheel size is used to calculate the
        probability of winning so that the house always wins."""
        return self.wheel_size() - self.colour_counts(colour=self.bias_colour)

    def colour_counts(self, colour: str) -> int:
        """Returns: the number of slots on the wheel of the specified colour"""
        return sum(map(colour.__eq__, self.slots.values()))

    def wheel_size(self) -> int:
        """Returns: The number of slots on the wheel as an int, for calculating probabilities within wager defns"""
        return len(self.slots)

    # UI methods - will need to be moved elsewhere

    def user_number_options_text(self):
        """
        Returns: text string describing the numbers of the roulette wheel
        Example output form: '0 to 36 (inclusive)'
        Note this would need to change if defining a roulette wheel which skips numbers
        """
        min_number = min(list(set(self.slots.keys())))
        max_number = max(list(set(self.slots.keys())))
        return f"{min_number} to {max_number} (inclusive)"

    def user_number_options_range(self):
        """Returns a range which specifies the valid number choices"""
        min_number = min(list(set(self.slots.keys())))
        max_number = max(list(set(self.slots.keys())))
        return range(min_number, max_number + 1)


# TODO Not sure if this counts as a base class, or if it should instead go in the bet_type_defns
# TODO find a better way of including the playing wheel defn
# By calculating the payout before defining the wheel we have problems
class RouletteBet(Bet):
    """Each bet on the Roulette wheel will be defined as a subclass of this class."""

    def __init__(self, payout: int,
                 win_criteria: list,
                 min_bet: int,
                 max_bet: int,
                 bet_type_id: str,
                 playing_wheel_id: str):
        super().__init__(payout, win_criteria, min_bet, max_bet)
        self.bet_type_id = bet_type_id
        self.playing_wheel_id = playing_wheel_id
        self.playing_wheel = RouletteWheel  # Maybe there's a better way of including the wheel here

    def calculate_payout(self):
        """Calculates the payout of a £1 roulette bet, determined by using the bias_wheel_size (which ignores the
        'bias_colour') when calculating the probability of winning, so that the return always reflects a degree of
        'the house always wins."""
        win_probability_over_estimate = len(self.win_criteria) / self.playing_wheel.bias_wheel_size()
        self.payout = floor(1 / win_probability_over_estimate)

    def determine_win_criteria(self, *args):
        """Abstract method for calculating the win crtieria of a given bet - will be bet specific.
        The determine_win_criteria method will be used to take an input and generate a list of winning slot for a
        given bet"""
        pass
