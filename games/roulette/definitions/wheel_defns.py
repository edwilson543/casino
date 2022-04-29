"""
To define a new wheel complete the following steps:
"""
from games.roulette.app.roulette_wheel_base_class import RouletteWheel
from games.roulette.constants.wheel_constants import WheelParameters
from typing import TypeVar
from enum import Enum


##########
# Typevar to be used when referencing wheels in type hints throughout game
##########
WHEEL_TYPES = TypeVar(name="WHEEL_TYPES", bound=RouletteWheel)

##########
# Instantiation of wheel objects from the parameters
##########
euro_wheel = RouletteWheel(
    wheel_name=WheelParameters.EURO_WHEEL.wheel_name,
    slots=WheelParameters.EURO_WHEEL.slots,
    bias_colour=WheelParameters.AMERICAN_WHEEL.bias_colour)

american_wheel = RouletteWheel(
    wheel_name=WheelParameters.AMERICAN_WHEEL.wheel_name,
    slots=WheelParameters.AMERICAN_WHEEL.slots,
    bias_colour=WheelParameters.AMERICAN_WHEEL.bias_colour)


# TODO how to avoid having to type wheel name (EURO_WHEEL and AMERICAN_WHEEL) over and over again?
class WheelOptions(Enum):
    EURO_WHEEL = euro_wheel
    AMERICAN_WHEEL = american_wheel
