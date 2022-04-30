from dataclasses import dataclass
from collections import namedtuple
from typing import TypeVar
import numpy as np


##########
# Data class for storing wheel parameters
##########
@dataclass
class RouletteWheelParameters:
    """
    Data class for storing the different attributes of each wheel, so they can be stored and imported separately
    """
    wheel_name: str
    slots: dict
    bias_colour: str

WHEEL_PARAMETER_TYPES = TypeVar(name="WHEEL_PARAMETER_TYPES", bound=RouletteWheelParameters)

##########
#  Return type object of a roulette wheel spin
##########
wheel_spin_return = namedtuple("wheel_spin_return", "number_return colour_return")


##########
# Base class defining the Roulette Wheel
##########
class RouletteWheel:
    """
    Base class for the roulette wheel - from which we can define different wheel configurations.

    Instance attributes:
    __________
    wheel_name: fully capitalised bet_type_name of the wheel with _WHEEL suffix
    slots: slot of the roulette wheel -
    should be passed as a dictionary, with the numbers as keys and the colours as the values
    bias_colour: the colour whose counts are ignored when calculating stake returns. e.g. if you have a 37 slot
    wheel and one slot is green, then stakes are calculated from probabilities as 1/(x/36).
    """

    def __init__(self,
                 wheel_name: str,
                 slots: dict,
                 bias_colour: str):
        self.wheel_name = wheel_name
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
        return sum(value == colour for value in self.slots.values())

    def wheel_size(self) -> int:
        """Returns: The number of slots on the wheel as an int, for calculating probabilities within wager defns"""
        return len(self.slots)

##########
# Type hint to be used when referencing all wheel objects
##########
WHEEL_TYPES = TypeVar(name="WHEEL_TYPES", bound=RouletteWheel)
