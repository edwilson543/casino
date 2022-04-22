import numpy as np
from collections import namedtuple

wheel_spin_return = namedtuple("wheel_spin_return", "number_return colour_return")

class RouletteWheel:
    """Base class for the roulette wheel - from which we can define different wheel configurations"""

    def __init__(self,
                 wheel_id: str,
                 slots: dict,
                 bias_colour: str):
        """
        Parameters
        __________
        slots: slot of the roulette wheel -
        should be passed as a dictionary, with the numbers as keys and the colours as the values
        bias_colour: the colour whose counts are ignored when calculating stake returns. e.g. if you have a 37 slot
        wheel and one slot is green, then stakes are calculated from probabilities as 1/(x/36).
        """
        self.wheel_id = wheel_id
        self.slots = slots
        self.bias_colour = bias_colour

    def spin(self) -> wheel_spin_return:
        """Returns: One random spin of the wheel as a dictionary, with number and colour as the key/value pairs"""
        min_slot = min(self.slots.keys())
        max_slot = max(self.slots.keys())
        number_return = np.random.randint(low=min_slot, high=max_slot + 1)
        # note the randint interval is half-open hence need of the + 1
        colour_return = self.slots[number_return]
        return wheel_spin_return(number_return, colour_return)

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
