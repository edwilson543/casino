"""To define a new wheel, first go to roulette->definitions->wheel_parameters_and_definitions"""

from games.roulette.definitions.wheel_parameters_and_defns import WheelParameters
from user_interface.command_line.roulette.app.roulette_wheel_base_class_user import RouletteWheelUser

from enum import Enum
from typing import TypeVar

##########
# Typevar to be used when referencing wheels in tpye hints throughout game
##########
USER_WHEEL_TYPES = TypeVar(name="USER_WHEEL_TYPES", bound=RouletteWheelUser)

##################
# Wheel relevant UI definitions
# Note these exclude this bias colour, as this cannot be bet on as a colours bet
##################
euro_wheel_colour_ids = {'R': 'red', 'B': 'black'}  # TODO update to use Colours
euro_wheel_colour_options_text = "[R]ed, [B]lack"

euro_wheel_user = RouletteWheelUser(wheel_name=WheelParameters.EUROWHEEL.value.wheel_name,
                                    wheel_id=WheelParameters.EUROWHEEL.value.wheel_id,
                                    slots=WheelParameters.EUROWHEEL.value.slots,
                                    bias_colour=WheelParameters.EUROWHEEL.value.bias_colour,
                                    colour_ids=euro_wheel_colour_ids,
                                    colour_options=euro_wheel_colour_options_text)

american_wheel_colour_ids = {'R': 'red', 'B': 'black'}  # TODO update to use Colours
american_wheel_colour_options_text = "[R]ed, [B]lack"

american_wheel_user = RouletteWheelUser(wheel_name=WheelParameters.AMERICANWHEEL.value.wheel_name,
                                        wheel_id=WheelParameters.AMERICANWHEEL.value.wheel_id,
                                        slots=WheelParameters.AMERICANWHEEL.value.slots,
                                        bias_colour=WheelParameters.AMERICANWHEEL.value.bias_colour,
                                        colour_ids=euro_wheel_colour_ids,
                                        colour_options=euro_wheel_colour_options_text)


##########
# Enum for storing all the user RouletteWheelUser class instances
##########
class WheelOptionsUser(Enum):
    EUROWHEEL = euro_wheel_user
    AMERICANWHEEL = american_wheel_user

wheel_options_text = "[E]uropean, [A]merican"

##########
# Create subclass of the RouletteWheelUser class for each defined wheel
##########
# class EuroWheelUser(RouletteWheelUser):
#     def __init__(self):
#         wheel_id = euro_wheel_id
#         slots = euro_wheel_slots
#         bias_colour = euro_wheel_bias_colour
#         colour_ids = euro_wheel_colour_ids
#         colour_options = euro_wheel_colour_options_text
#         super().__init__(wheel_id, slots, bias_colour, colour_ids, colour_options)
#
#
# class AmericanWheelUser(RouletteWheelUser):
#     def __init__(self):
#         wheel_id = american_wheel_id
#         slots = american_wheel_slots
#         bias_colour = american_wheel_bias_colour
#         colour_ids = american_wheel_colour_ids
#         colour_options = american_wheel_colour_options_text
#         super().__init__(wheel_id, slots, bias_colour, colour_ids, colour_options)


##############################
# Dictionary and associated text for the different wheel options
##############################
# wheel_options_user = {'E': EuroWheelUser(), 'A': AmericanWheelUser()}
# wheel_options_text = "[E]uropean, [A]merican"
