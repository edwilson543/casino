from Games.Roulette.app.roulette_wheel_base_class import RouletteWheel
from typing import TypeVar

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
user_interface->command_line->Roulette->definitions-> bet_type_defns_user
and adding the wheel_id as a primary key in the navigation parameters
"""
# TODO add adjacency lists (maybe implementedd with a dictionary) for the boards to the definitions
# Then in the UI wheel, add a string rep of form "|1|2|\n-----\n|3|4|"
###############################
# Wheel definitions and payouts
###############################
euro_wheel_id = 'E'
euro_wheel_defn = {0: 'green', 1: 'red', 2: 'black', 3: 'red', 4: 'black', 5: 'red', 6: 'black', 7: 'red',
                   8: 'black', 9: 'red', 10: 'black', 11: 'black', 12: 'red', 13: 'black', 14: 'red', 15: 'black',
                   16: 'red', 17: 'black', 18: 'red', 19: 'red', 20: 'black', 21: 'red', 22: 'black', 23: 'red',
                   24: 'black', 25: 'red', 26: 'black', 27: 'red', 28: 'black', 29: 'black', 30: 'red', 31: 'black',
                   32: 'red', 33: 'black', 34: 'red', 35: 'black', 36: 'red'}
euro_wheel_bias_colour = 'green'

american_wheel_id = 'A'
american_wheel_defn = {-1: 'green', 0: 'green', 1: 'red', 2: 'black', 3: 'red', 4: 'black', 5: 'red', 6: 'black',
                       7: 'red', 8: 'black', 9: 'red', 10: 'black', 11: 'black', 12: 'red', 13: 'black', 14: 'red',
                       15: 'black', 16: 'red', 17: 'black', 18: 'red', 19: 'red', 20: 'black', 21: 'red', 22: 'black',
                       23: 'red', 24: 'black', 25: 'red', 26: 'black', 27: 'red', 28: 'black', 29: 'black', 30: 'red',
                       31: 'black', 32: 'red', 33: 'black', 34: 'red', 35: 'black', 36: 'red'}
# note -1 corresponds to 00, which is in effect the same as 0
american_wheel_bias_colour = 'green'

template_wheel_id = 'T'
template_wheel_defn = {0: 'black', 1: 'white'}
template_wheel_bias_colour = 'black'


###############################
# Create subclass of the RouletteWheel base class for each defined wheel
###############################
class EuroWheel(RouletteWheel):
    def __init__(self):
        wheel_id = euro_wheel_id
        slots = euro_wheel_defn
        bias_colour = euro_wheel_bias_colour
        super().__init__(wheel_id, slots, bias_colour)


class AmericanWheel(RouletteWheel):
    def __init__(self):
        wheel_id = american_wheel_id
        slots = american_wheel_defn
        bias_colour = american_wheel_bias_colour
        super().__init__(wheel_id, slots, bias_colour)


class TemplateWheel(RouletteWheel):
    def __init__(self):
        wheel_id = template_wheel_id
        slots = template_wheel_defn
        bias_colour = template_wheel_bias_colour
        super().__init__(wheel_id, slots, bias_colour)


##############################
# Dictionary and associated text for the different wheel options
##############################
wheel_options = {'E': EuroWheel(), 'A': AmericanWheel()}

