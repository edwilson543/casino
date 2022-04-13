from Games.Roulette.definitions.wheel_defns import euro_wheel_id, euro_wheel_defn, euro_wheel_bias_colour
from Games.Roulette.definitions.wheel_defns import american_wheel_id, american_wheel_defn, american_wheel_bias_colour
from Games.Roulette.definitions.wheel_defns import template_wheel_id, template_wheel_defn, template_wheel_bias_colour
from user_interface.command_line.Roulette.app.roulette_wheel_base_class_user import RouletteWheelUser

"""To define a new wheel, first go to Roulette->definitions->wheel_defns"""
##################
# Wheel relevant UI definitions
##################
euro_wheel_colour_ids = {'G': 'green', 'R': 'red', 'B': 'black'}
euro_wheel_colour_options_text = "[G]reen, [R]ed, [B]lack"

american_wheel_colour_ids = {'G': 'green', 'R': 'red', 'B': 'black'}
american_wheel_colour_options_text = "[G]reen, [R]ed, [B]lack"

template_wheel_colour_ids = {'B': 'black', 'W': 'white'}
template_wheel_colour_options_text = "[B]lack, [W]hite"


# TODO find out how to define specific user wheels as subclasses of the defined equivalent roulette wheel,
# i.e. using multiple inheritance, so that their parameters don't need to be imported here?
##########
# Create subclass of the RouletteWheelUser class for each defined wheel
##########
class EuroWheelUser(RouletteWheelUser):
    def __init__(self):
        wheel_id = euro_wheel_id
        slots = euro_wheel_defn
        bias_colour = euro_wheel_bias_colour
        colour_ids = euro_wheel_colour_ids
        colour_options = euro_wheel_colour_options_text
        super().__init__(wheel_id, slots, bias_colour, colour_ids, colour_options)


class AmericanWheelUser(RouletteWheelUser):
    def __init__(self):
        wheel_id = american_wheel_id
        slots = american_wheel_defn
        bias_colour = american_wheel_bias_colour
        colour_ids = american_wheel_colour_ids
        colour_options = american_wheel_colour_options_text
        super().__init__(wheel_id, slots, bias_colour, colour_ids, colour_options)


class TemplateWheelUser(RouletteWheelUser):
    def __init__(self):
        wheel_id = template_wheel_id
        slots = template_wheel_defn
        bias_colour = template_wheel_bias_colour
        colour_ids = template_wheel_colour_ids
        colour_options = template_wheel_colour_options_text
        super().__init__(wheel_id, slots, bias_colour, colour_ids, colour_options)


##############################
# Dictionary and associated text for the different wheel options
##############################
wheel_options_user = {'E': EuroWheelUser(), 'A': AmericanWheelUser()}
wheel_options_text = "[E]uropean, [A]merican"
