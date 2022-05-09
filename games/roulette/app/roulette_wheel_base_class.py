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
    Parameters:
    ----------
    wheel_name: fully capitalised bet_type_name of the wheel with _WHEEL suffix
    slots: slot of the roulette wheel -
    should be passed as a dictionary, with the numbers as keys and the colours as the values
    bias_colour: the colour whose counts are ignored when calculating stake returns. e.g. if you have a 37 slot
    wheel and one slot is green, then stakes are calculated from probabilities as 1/(x/36).
    board: a numpy array representing the roulette board corresponding to the wheel Only includes non-bias slots (i.e.
    does not include 0)
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
    Note that all instance attributes are contained in "parameters" - see RouletteWheelParameters dataclass above
    """

    def __init__(self, parameters: RouletteWheelParameters):
        self.parameters = parameters

    def spin(self) -> wheel_spin_return:
        """Returns: One random spin of the wheel as type wheel_spin_return (defined above)"""
        min_slot = min(self.parameters.slots.keys())
        max_slot = max(self.parameters.slots.keys())
        number_return = random.randint(low=min_slot, high=max_slot + 1)
        # note the randint interval is half-open hence need of the + 1
        colour_return = self.parameters.slots[number_return]
        return wheel_spin_return(number_return, colour_return)

    def bias_wheel_size(self) -> int:
        """
        Returns: The number of slots on the wheel, minus a count of the number of slots of biased colours.
        The purpose is so that when calculating the return for a bet, the bias wheel size is used to calculate the
        probability of winning so that the house always wins."""
        return len(self.parameters.slots) - self.colour_counts(colour=self.parameters.bias_colour)

    def colour_counts(self, colour: Colour) -> int:
        """Returns: the number of slots on the wheel of the specified colour"""
        if colour in self.parameters.slots.values():
            return sum(value == colour for value in self.parameters.slots.values())
        else:
            raise ValueError(f"{colour} is not a colour on the {self.parameters.wheel_name}.")


##########
# Type hint to be used when referencing all wheel objects
##########
WHEEL_TYPES = TypeVar(name="WHEEL_TYPES", bound=RouletteWheel)
