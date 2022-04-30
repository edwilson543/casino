from dataclasses import dataclass, asdict

from games.roulette.constants.wheel_constants import WheelParameters, WheelIds

from user_interface.command_line.roulette.app.roulette_wheel_base_class_user import RouletteWheelParametersUser

euro_wheel_colour_ids = {'R': 'red', 'B': 'black'}  # TODO update to use Colours and an enum rather than dict
euro_wheel_colour_options_text = "[R]ed, [B]lack"

american_wheel_colour_ids = {'R': 'red', 'B': 'black'}  # TODO update to use Colours
american_wheel_colour_options_text = "[R]ed, [B]lack"

euro_wheel_user_parameters = RouletteWheelParametersUser(
    **asdict(WheelParameters.EURO_WHEEL),
    colour_ids=euro_wheel_colour_ids,
    colour_options=euro_wheel_colour_options_text)

american_wheel_user_parameters = RouletteWheelParametersUser(
    **asdict(WheelParameters.AMERICAN_WHEEL),
    colour_ids=american_wheel_colour_ids,
    colour_options=american_wheel_colour_options_text)


@dataclass
class WheelParametersUser:
    EURO_WHEEL = euro_wheel_user_parameters
    AMERICAN_WHEEL = american_wheel_user_parameters


##########
# Text to display to the user giving them the various wheel options
##########
wheel_options_text = f"[{WheelIds.EURO_WHEEL.value}]uropean, " \
                     f"[{WheelIds.AMERICAN_WHEEL.value}]merican"
