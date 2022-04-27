from games.roulette.app.roulette_wheel_base_class import RouletteWheel
from typing import TypeVar
from enum import Enum
from dataclasses import dataclass

##########
# Typevar to be used when referencing wheels in tpye hints throughout game
##########
WHEEL_TYPES = TypeVar(name="WHEEL_TYPES", bound=RouletteWheel)

"""
To define a new wheel complete the following steps:
1) Create wheel_defn as a mapping of the numbers on the wheel to the colours
2) Define the wheel_colour_bias - this is the colour that gets ignored when calculating probabilities
3) Create a subclass of the RouletteWheel base class for each wheel, using the defined parameters
4) Add the wheel to the wheel_options dict below, using an identification key

5) Go to wheel_defns_user in command_line -> roulette_definitions
6) Add some colour ids - these should be unique, using as many characters as necessary e.g. BLU and BLA if blue and
black feature on the same wheel
7) Define a colour_options_text for that wheel, which should correspond to the colour ids (omitting the bias colour
as an option for betting on)
8) Define the wheel as a subclass of RouletteWheelUser
"""  # TODO - find a cleaner way of defining the user wheels -
# multiple inheritance for inheriting default values, if this is possible?
# named tuple/ data classes?
"""  
9) Add the user wheel option to the wheel_options_user dict and the wheel_options_text string, 
so that it can be chosen in the game, with the relevant key
10) Add the relevant bet type options to the user wheel by going to
user_interface->command_line->roulette->definitions-> bet_type_defns_user
and adding the wheel_id as a primary key in the navigation parameters
"""


##########
# Colours
##########
class Colours:
    RED = 'red'
    # TODO finsih and implement in definitions below


##########
# Data class for storing parameters
##########
@dataclass
class RouletteWheelParameters:
    """Data class for storing the different attributes of each wheel, so they can be put in the
    enum at the bottom and imported for User specific wheels"""
    wheel_name: str
    wheel_id: str
    slots: dict
    bias_colour: str


##########
# Wheel definitions
##########
# EUROWHEEL
euro_wheel_name = "EUROWHEEL"
euro_wheel_id = 'E'
euro_wheel_slots = {0: 'green', 1: 'red', 2: 'black', 3: 'red', 4: 'black', 5: 'red', 6: 'black', 7: 'red',
                    8: 'black', 9: 'red', 10: 'black', 11: 'black', 12: 'red', 13: 'black', 14: 'red', 15: 'black',
                    16: 'red', 17: 'black', 18: 'red', 19: 'red', 20: 'black', 21: 'red', 22: 'black', 23: 'red',
                    24: 'black', 25: 'red', 26: 'black', 27: 'red', 28: 'black', 29: 'black', 30: 'red', 31: 'black',
                    32: 'red', 33: 'black', 34: 'red', 35: 'black', 36: 'red'}
euro_wheel_bias_colour = 'green'

euro_wheel = RouletteWheel(wheel_name=euro_wheel_name, wheel_id=euro_wheel_id,
                           slots=euro_wheel_slots, bias_colour=euro_wheel_bias_colour)
euro_wheel_parameters = RouletteWheelParameters(wheel_name=euro_wheel_name, wheel_id=euro_wheel_id,
                                                slots=euro_wheel_slots, bias_colour=euro_wheel_bias_colour)

# AMERICANWHEEL
american_wheel_name = "AMERICANWHEEL"
american_wheel_id = 'A'
american_wheel_slots = {-1: 'green', 0: 'green', 1: 'red', 2: 'black', 3: 'red', 4: 'black', 5: 'red', 6: 'black',
                        7: 'red', 8: 'black', 9: 'red', 10: 'black', 11: 'black', 12: 'red', 13: 'black', 14: 'red',
                        15: 'black', 16: 'red', 17: 'black', 18: 'red', 19: 'red', 20: 'black', 21: 'red', 22: 'black',
                        23: 'red', 24: 'black', 25: 'red', 26: 'black', 27: 'red', 28: 'black', 29: 'black', 30: 'red',
                        31: 'black', 32: 'red', 33: 'black', 34: 'red', 35: 'black', 36: 'red'}
# note -1 corresponds to 00, which is in effect the same as 0
american_wheel_bias_colour = 'green'

american_wheel = RouletteWheel(wheel_name=american_wheel_name, wheel_id=american_wheel_id,
                               slots=american_wheel_slots, bias_colour=american_wheel_bias_colour)
american_wheel_parameters = RouletteWheelParameters(wheel_name=american_wheel_name, wheel_id=american_wheel_id,
                                                    slots=american_wheel_slots, bias_colour=american_wheel_bias_colour)


###############################
# Create subclass of the RouletteWheel base class for each defined wheel
###############################
# class EuroWheel(RouletteWheel):
#     def __init__(self):
#         wheel_id = euro_wheel_id
#         slots = euro_wheel_slots
#         bias_colour = euro_wheel_bias_colour
#         super().__init__(wheel_id, slots, bias_colour)
#
#
# class AmericanWheel(RouletteWheel):
#     def __init__(self):
#         wheel_id = american_wheel_id
#         slots = american_wheel_slots
#         bias_colour = american_wheel_bias_colour
#         super().__init__(wheel_id, slots, bias_colour)

##############################
# Dictionary and associated text for the different wheel options
##############################
# wheel_options = {'E': EuroWheel(), 'A': AmericanWheel()}

class WheelIds(str, Enum):
    EUROWHEEL = euro_wheel_id
    AMERICANWHEEL = american_wheel_id


class WheelParameters(RouletteWheelParameters, Enum):
    EUROWHEEL = euro_wheel_parameters
    AMERICANWHEEL = american_wheel_parameters


class WheelOptions(Enum):
    EUROWHEEL = euro_wheel
    AMERICANWHEEL = american_wheel
