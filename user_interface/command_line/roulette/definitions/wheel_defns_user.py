"""To define a new wheel, first go to roulette->definitions->wheel_parameters_and_definitions"""

from user_interface.command_line.roulette.constants.wheel_constants_user import WheelParametersUser
from user_interface.command_line.roulette.app.roulette_wheel_base_class_user import RouletteWheelUser

from enum import Enum



##################
# Wheel relevant UI definitions
##################
#  TODO do from dict
euro_wheel_user = RouletteWheelUser(
    wheel_name=WheelParametersUser.EURO_WHEEL.wheel_name,
    slots=WheelParametersUser.EURO_WHEEL.slots,
    bias_colour=WheelParametersUser.EURO_WHEEL.bias_colour,
    colour_ids=WheelParametersUser.EURO_WHEEL.colour_ids,
    colour_options=WheelParametersUser.EURO_WHEEL.colour_ids)


american_wheel_user = RouletteWheelUser(
    wheel_name=WheelParametersUser.AMERICAN_WHEEL.wheel_name,
    slots=WheelParametersUser.AMERICAN_WHEEL.slots,
    bias_colour=WheelParametersUser.AMERICAN_WHEEL.bias_colour,
    colour_ids=WheelParametersUser.AMERICAN_WHEEL.colour_ids,
    colour_options=WheelParametersUser.AMERICAN_WHEEL.colour_options)


##########
# Enum for storing all the user RouletteWheelUser class instances
##########
class WheelOptionsUser(Enum):
    EURO_WHEEL = euro_wheel_user
    AMERICAN_WHEEL = american_wheel_user


