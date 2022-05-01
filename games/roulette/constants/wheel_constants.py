from games.roulette.app.roulette_wheel_base_class import RouletteWheelParameters
from dataclasses import dataclass
from enum import Enum
from numpy import array

##########
# Global wheel parameters
##########
class WheelIds(str, Enum):
    """Class for storing wheel bet_type_name and an associated id"""
    EURO_WHEEL = "E"
    AMERICAN_WHEEL = "A"


# TODO implement Colours Enum in the definitions below, and on UI side

# EURO_WHEEL parameters
euro_wheel_parameters = RouletteWheelParameters(
    wheel_name=WheelIds.EURO_WHEEL.name,
    slots={0: 'green', 1: 'red', 2: 'black', 3: 'red', 4: 'black', 5: 'red', 6: 'black', 7: 'red',
           8: 'black', 9: 'red', 10: 'black', 11: 'black', 12: 'red', 13: 'black', 14: 'red', 15: 'black',
           16: 'red', 17: 'black', 18: 'red', 19: 'red', 20: 'black', 21: 'red', 22: 'black', 23: 'red',
           24: 'black', 25: 'red', 26: 'black', 27: 'red', 28: 'black', 29: 'black', 30: 'red', 31: 'black',
           32: 'red', 33: 'black', 34: 'red', 35: 'black', 36: 'red'},
    bias_colour='green',
    board = array([[1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34],
                  [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35],
                   [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]]))

# AMERICAN_WHEEL parameters
american_wheel_parameters = RouletteWheelParameters(
    wheel_name=WheelIds.AMERICAN_WHEEL.name,
    slots={-1: 'green', 0: 'green', 1: 'red', 2: 'black', 3: 'red', 4: 'black', 5: 'red', 6: 'black',
           7: 'red', 8: 'black', 9: 'red', 10: 'black', 11: 'black', 12: 'red', 13: 'black', 14: 'red',
           15: 'black', 16: 'red', 17: 'black', 18: 'red', 19: 'red', 20: 'black', 21: 'red', 22: 'black',
           23: 'red', 24: 'black', 25: 'red', 26: 'black', 27: 'red', 28: 'black', 29: 'black', 30: 'red',
           31: 'black', 32: 'red', 33: 'black', 34: 'red', 35: 'black', 36: 'red'},
    # note -1 corresponds to 00, which is in effect the same as 0
    bias_colour='green',
    board = array([[1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34],
                  [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35],
                   [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]]))


@dataclass
class WheelParameters:
    EURO_WHEEL = euro_wheel_parameters
    AMERICAN_WHEEL = american_wheel_parameters
