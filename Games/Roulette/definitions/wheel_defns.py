from Games.Roulette.app.roulette_wheel_base_class import RouletteWheel

"""
To define a new wheel complete the following steps:
1) Create wheel_defn as a mapping of the numbers on the wheel to the colours
2) Add some colour ids - these should be unique, using as many characters as necessary e.g. BLU and BLA if blue and
black feature on the same wheel
3) Define a colour_options_text for that wheel, which should correspond to the colour ids 
5) Define the wheel_colour_bias - this is the colour that gets ignored when calculating probabilities
6) Create a subclass of the RouletteWheel base class for each wheel, using the defined parameters
7) Add the wheel to the wheel_options dict below, using an identification key
8) Add the wheel option to the wheel_options_text so that it can be chosen in the game, with the same key
9) Add relevant bet type options to the wheel in bet_type_defns, using the wheel id key from wheel_options
10) Map relevant bet type methods for the wheel in roulette_base_classes RouletteWheel class, defining any new methods
if necessary.
"""
# TODO add dictionaries for the boards to the definitions, maybe with a string rep of form "|1|2|\n-----\n|3|4|"
###############################
# Wheel definitions and payouts
###############################
euro_wheel_defn = {0: 'green', 1: 'red', 2: 'black', 3: 'red', 4: 'black', 5: 'red', 6: 'black', 7: 'red',
                   8: 'black', 9: 'red', 10: 'black', 11: 'black', 12: 'red', 13: 'black', 14: 'red', 15: 'black',
                   16: 'red', 17: 'black', 18: 'red', 19: 'red', 20: 'black', 21: 'red', 22: 'black', 23: 'red',
                   24: 'black', 25: 'red', 26: 'black', 27: 'red', 28: 'black', 29: 'black', 30: 'red', 31: 'black',
                   32: 'red', 33: 'black', 34: 'red', 35: 'black', 36: 'red'}
euro_wheel_colour_ids = {'G': 'green', 'R': 'red', 'B': 'black'}
euro_wheel_colour_options_text = "[G]reen, [R]ed, [B]lack"
euro_wheel_bias_colour = 'green'

american_wheel_defn = {-1: 'green', 0: 'green', 1: 'red', 2: 'black', 3: 'red', 4: 'black', 5: 'red', 6: 'black',
                       7: 'red', 8: 'black', 9: 'red', 10: 'black', 11: 'black', 12: 'red', 13: 'black', 14: 'red',
                       15: 'black', 16: 'red', 17: 'black', 18: 'red', 19: 'red', 20: 'black', 21: 'red', 22: 'black',
                       23: 'red', 24: 'black', 25: 'red', 26: 'black', 27: 'red', 28: 'black', 29: 'black', 30: 'red',
                       31: 'black', 32: 'red', 33: 'black', 34: 'red', 35: 'black', 36: 'red'}
# note -1 corresponds to 00, which is in effect the same as 0
american_wheel_colour_ids = {'G': 'green', 'R': 'red', 'B': 'black'}
american_wheel_colour_options_text = "[G]reen, [R]ed, [B]lack"
american_wheel_bias_colour = 'green'

template_wheel_defn = {0: 'black', 1: 'white'}
template_wheel_colour_ids = {'B': 'black', 'W': 'white'}
template_wheel_colour_options_text = "[B]lack, [W]hite"
template_wheel_bias_colour = 'black'


###############################
# Create subclass of the RouletteWheel base class for each defined wheel
###############################
class EuroWheel(RouletteWheel):
    def __init__(self):
        slots = euro_wheel_defn
        colour_ids = euro_wheel_colour_ids
        colour_options = euro_wheel_colour_options_text
        bias_colour = euro_wheel_bias_colour
        super().__init__(slots, colour_ids, colour_options, bias_colour)


class AmericanWheel(RouletteWheel):
    def __init__(self):
        slots = american_wheel_defn
        colour_ids = american_wheel_colour_ids
        colour_options = american_wheel_colour_options_text
        bias_colour = american_wheel_bias_colour
        super().__init__(slots, colour_ids, colour_options, bias_colour)


class TemplateWheel(RouletteWheel):
    def __init__(self):
        slots = template_wheel_defn
        colour_ids = template_wheel_colour_ids
        colour_options = template_wheel_colour_options_text
        bias_colour = template_wheel_bias_colour
        super().__init__(slots, colour_ids, colour_options, bias_colour)


##############################
# Dictionary and associated text for the different wheel options
##############################
wheel_options = {'E': EuroWheel(), 'A': AmericanWheel()}
wheel_options_text = "[E]uropean, [A]merican"
