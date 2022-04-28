"""To define a new wheel, first go to roulette->definitions->wheel_parameters_and_definitions"""

from games.roulette.definitions.wheel_parameters_and_defns import WheelIds, WheelParameters
from user_interface.command_line.roulette.app.roulette_wheel_base_class_user import RouletteWheelUser

from enum import Enum
from typing import TypeVar

##########
# Typevar to be used when referencing wheels in type hints throughout game
##########
USER_WHEEL_TYPES = TypeVar(name="USER_WHEEL_TYPES", bound=RouletteWheelUser)

##################
# Wheel relevant UI definitions
# Note these exclude this bias colour, as this cannot be bet on as a colours bet
##################
euro_wheel_colour_ids = {'R': 'red', 'B': 'black'}  # TODO update to use Colours
euro_wheel_colour_options_text = "[R]ed, [B]lack"

euro_wheel_user = RouletteWheelUser(wheel_name=WheelIds.EURO_WHEEL.name,
                                    slots=WheelParameters.EURO_WHEEL.value.slots,
                                    bias_colour=WheelParameters.EURO_WHEEL.value.bias_colour,
                                    colour_ids=euro_wheel_colour_ids,
                                    colour_options=euro_wheel_colour_options_text)

american_wheel_colour_ids = {'R': 'red', 'B': 'black'}  # TODO update to use Colours
american_wheel_colour_options_text = "[R]ed, [B]lack"

american_wheel_user = RouletteWheelUser(wheel_name=WheelIds.AMERICAN_WHEEL.name,
                                        slots=WheelParameters.AMERICAN_WHEEL.value.slots,
                                        bias_colour=WheelParameters.AMERICAN_WHEEL.value.bias_colour,
                                        colour_ids=euro_wheel_colour_ids,
                                        colour_options=euro_wheel_colour_options_text)


##########
# Enum for storing all the user RouletteWheelUser class instances
##########
class WheelOptionsUser(Enum):
    EURO_WHEEL = euro_wheel_user
    AMERICAN_WHEEL = american_wheel_user


wheel_options_text = f"[{WheelIds.EURO_WHEEL.value}]uropean, " \
                     f"[{WheelIds.AMERICAN_WHEEL.value}]merican"
