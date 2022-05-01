from games.roulette.constants.game_constants import Colour
from dataclasses import dataclass
from collections import namedtuple
from typing import TypeVar
from numpy import random, array


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
    bias_colour: Colour
    board: array

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
    board: a numpy array representing the roulette board corresponding to the wheel Only includes non-bias slots (i.e.
    does not include 0)
    """

    def __init__(self,
                 wheel_name: str,
                 slots: dict,
                 bias_colour: Colour,
                 board: array):
        self.wheel_name = wheel_name
        self.slots = slots
        self.bias_colour = bias_colour
        self.board = board

    def spin(self) -> wheel_spin_return:
        """Returns: One random spin of the wheel as a dictionary, with number and colour as the key/value pairs"""
        min_slot = min(self.slots.keys())
        max_slot = max(self.slots.keys())
        number_return = random.randint(low=min_slot, high=max_slot + 1)
        # note the randint interval is half-open hence need of the + 1
        colour_return = self.slots[number_return]
        return wheel_spin_return(number_return, colour_return)

    def bias_wheel_size(self) -> int:
        """
        Returns: The number of slots on the wheel, minus a count of the number of slots of biased colours.
        The purpose is so that when calculating the return for a bet, the bias wheel size is used to calculate the
        probability of winning so that the house always wins."""
        return len(self.slots) - self.colour_counts(colour=self.bias_colour)

    def colour_counts(self, colour: Colour) -> int:
        """Returns: the number of slots on the wheel of the specified colour"""
        return sum(value == colour for value in self.slots.values())

    def generate_colour_options(self) -> set[Colour]:
        """Returns: a set of all the valid colours bet options (i.e. excluding bias colour)"""
        colour_options = set(self.slots.values()).difference({self.bias_colour})
        return colour_options

    def generate_number_options_range(self):
        """Returns a range which specifies the valid number choices"""
        min_number = min(list(set(self.slots.keys())))
        max_number = max(list(set(self.slots.keys())))
        return range(min_number, max_number + 1)


##########
# Type hint to be used when referencing all wheel objects
##########
WHEEL_TYPES = TypeVar(name="WHEEL_TYPES", bound=RouletteWheel)
