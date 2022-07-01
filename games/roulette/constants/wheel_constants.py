"""
Module content:
- Wheel IDs/prompts and ancillary function for getting a prompt listing the defined wheels
- Parameters necessary for defining each wheel.

To define a new wheel complete the following steps:
1) Add an ID, prompt for that wheel
2) Add all necessary parameters for that wheel, as is done for the existing wheel
3) Add the new wheel to the WheelParameters Enum at the bottom
4) Add all relevant bets (can just use the default bets) to that wheel, in the WheelBetParameters Enum found in
bet_constants
"""

# Standard library imports
from dataclasses import dataclass
from enum import Enum

# Third party imports
from numpy import array

# Local application imports
from games.roulette.app.roulette_wheel_base_class import RouletteWheelParameters
from games.roulette.constants.game_constants import Colour


##########
# Wheel IDs and corresponding prompts
##########
class WheelIds(Enum):
    """Enum class for storing wheel bet_type_name and an associated id"""
    EURO_WHEEL = "E"
    AMERICAN_WHEEL = "A"


class WheelPrompts(Enum):
    """Class giving all the wheel prompts. Defined here as it has to match the IDs"""
    EURO_WHEEL = "[E]uropean"
    AMERICAN_WHEEL = "[A]merican"


def get_wheel_options_text():
    """Function to return a string of prompts showing the user all the available wheels on the command line."""
    full_prompt = ", ".join([prompt.value for prompt in WheelPrompts])
    return full_prompt


##########
# All wheel parameters
##########

# EURO_WHEEL parameters
euro_wheel_parameters = RouletteWheelParameters(
    wheel_name=WheelIds.EURO_WHEEL.name,
    slots={0: Colour.GREEN, 1: Colour.RED, 2: Colour.BLACK, 3: Colour.RED, 4: Colour.BLACK, 5: Colour.RED,
           6: Colour.BLACK, 7: Colour.RED, 8: Colour.BLACK, 9: Colour.RED, 10: Colour.BLACK, 11: Colour.BLACK,
           12: Colour.RED, 13: Colour.BLACK, 14: Colour.RED, 15: Colour.BLACK, 16: Colour.RED, 17: Colour.BLACK,
           18: Colour.RED, 19: Colour.RED, 20: Colour.BLACK, 21: Colour.RED, 22: Colour.BLACK, 23: Colour.RED,
           24: Colour.BLACK, 25: Colour.RED, 26: Colour.BLACK, 27: Colour.RED, 28: Colour.BLACK, 29: Colour.BLACK,
           30: Colour.RED, 31: Colour.BLACK, 32: Colour.RED, 33: Colour.BLACK, 34: Colour.RED, 35: Colour.BLACK,
           36: Colour.RED},
    bias_colour=Colour.GREEN,
    board=array([[1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34],
                 [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35],
                 [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]]))  # Note excludes 0 - shouldn't be needed

# AMERICAN_WHEEL parameters
american_wheel_parameters = RouletteWheelParameters(
    wheel_name=WheelIds.AMERICAN_WHEEL.name,
    slots={-1: Colour.GREEN, 0: Colour.GREEN, 1: Colour.RED, 2: Colour.BLACK, 3: Colour.RED, 4: Colour.BLACK,
           5: Colour.RED, 6: Colour.BLACK, 7: Colour.RED, 8: Colour.BLACK, 9: Colour.RED, 10: Colour.BLACK,
           11: Colour.BLACK, 12: Colour.RED, 13: Colour.BLACK, 14: Colour.RED, 15: Colour.BLACK, 16: Colour.RED,
           17: Colour.BLACK, 18: Colour.RED, 19: Colour.RED, 20: Colour.BLACK, 21: Colour.RED, 22: Colour.BLACK,
           23: Colour.RED, 24: Colour.BLACK, 25: Colour.RED, 26: Colour.BLACK, 27: Colour.RED, 28: Colour.BLACK,
           29: Colour.BLACK, 30: Colour.RED, 31: Colour.BLACK, 32: Colour.RED, 33: Colour.BLACK, 34: Colour.RED,
           35: Colour.BLACK, 36: Colour.RED},
    # note -1 corresponds to 00, which is in effect the same as 0
    bias_colour=Colour.GREEN,
    board=array([[1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34],
                 [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35],
                 [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]]))  # Note excludes 0 nad 00 (-1) - shouldn't be needed


@dataclass
class WheelParameters:
    """Dataclass storing all the parameters that define the playing wheels"""
    EURO_WHEEL = euro_wheel_parameters
    AMERICAN_WHEEL = american_wheel_parameters
