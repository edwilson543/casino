"""
To define a new wheel complete the following steps:
"""
from games.roulette.app.roulette_wheel_base_class import RouletteWheel
from typing import TypeVar
from enum import Enum
from dataclasses import dataclass


# TODO how to avoid having to type wheel name (EURO_WHEEL and AMERICAN_WHEEL) over and over again?

##########
# Colours
##########
class Colours:
    RED = 'red'
    # TODO finish and implement in definitions below


##########
# Typevar to be used when referencing wheels in type hints throughout game
##########
WHEEL_TYPES = TypeVar(name="WHEEL_TYPES", bound=RouletteWheel)


##########
# Global wheel parameters
##########
class WheelIds(str, Enum):
    """Class for storing wheel name and id"""
    EURO_WHEEL = "E"
    AMERICAN_WHEEL = "A"


##########
# Data class for storing wheel parameters
##########
@dataclass
class RouletteWheelParameters:
    """Data class for storing the different attributes of each wheel, so they can be put in the
    enum at the bottom and imported for User specific wheels"""
    wheel_name: str
    slots: dict
    bias_colour: str


##########
# Wheel definitions
##########
# EURO_WHEEL parameters
euro_wheel_parameters = RouletteWheelParameters(
    wheel_name=WheelIds.EURO_WHEEL.name,
    slots={0: 'green', 1: 'red', 2: 'black', 3: 'red', 4: 'black', 5: 'red', 6: 'black', 7: 'red',
           8: 'black', 9: 'red', 10: 'black', 11: 'black', 12: 'red', 13: 'black', 14: 'red', 15: 'black',
           16: 'red', 17: 'black', 18: 'red', 19: 'red', 20: 'black', 21: 'red', 22: 'black', 23: 'red',
           24: 'black', 25: 'red', 26: 'black', 27: 'red', 28: 'black', 29: 'black', 30: 'red', 31: 'black',
           32: 'red', 33: 'black', 34: 'red', 35: 'black', 36: 'red'},
    bias_colour='green')

# AMERICAN_WHEEL parameters
american_wheel_parameters = RouletteWheelParameters(
    wheel_name=WheelIds.AMERICAN_WHEEL.name,
    slots={-1: 'green', 0: 'green', 1: 'red', 2: 'black', 3: 'red', 4: 'black', 5: 'red', 6: 'black',
           7: 'red', 8: 'black', 9: 'red', 10: 'black', 11: 'black', 12: 'red', 13: 'black', 14: 'red',
           15: 'black', 16: 'red', 17: 'black', 18: 'red', 19: 'red', 20: 'black', 21: 'red', 22: 'black',
           23: 'red', 24: 'black', 25: 'red', 26: 'black', 27: 'red', 28: 'black', 29: 'black', 30: 'red',
           31: 'black', 32: 'red', 33: 'black', 34: 'red', 35: 'black', 36: 'red'},
    # note -1 corresponds to 00, which is in effect the same as 0
    bias_colour='green')

##########
# Instantiation of wheel objects from the parameters
##########
euro_wheel = RouletteWheel(
    wheel_name=WheelIds.EURO_WHEEL.name,
    slots=euro_wheel_parameters.slots,
    bias_colour=euro_wheel_parameters.bias_colour)

american_wheel = RouletteWheel(
    wheel_name=WheelIds.AMERICAN_WHEEL.AMERICAN_WHEEL,
    slots=american_wheel_parameters.slots,
    bias_colour=american_wheel_parameters.bias_colour)


class WheelParameters(Enum):
    EURO_WHEEL = euro_wheel_parameters
    AMERICAN_WHEEL = american_wheel_parameters


class WheelOptions(Enum):
    EURO_WHEEL = euro_wheel
    AMERICAN_WHEEL = american_wheel
