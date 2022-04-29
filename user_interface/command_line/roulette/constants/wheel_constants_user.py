from dataclasses import dataclass
from games.roulette.constants.wheel_constants import RouletteWheelParameters, WheelParameters

##########
# Dataclass for definiing the RouletteBet User Parameters
@dataclass
class RouletteWheelParametersUser(RouletteWheelParameters):
    colour_ids: dict
    colour_options: str


euro_wheel_colour_ids = {'R': 'red', 'B': 'black'}  # TODO update to use Colours and an enum rather than dict
euro_wheel_colour_options_text = "[R]ed, [B]lack"

american_wheel_colour_ids = {'R': 'red', 'B': 'black'}  # TODO update to use Colours
american_wheel_colour_options_text = "[R]ed, [B]lack"

euro_wheel_user_parameters = RouletteWheelParametersUser(  # TODO do from dict
    wheel_name=WheelParameters.EURO_WHEEL.wheel_name,
    slots=WheelParameters.EURO_WHEEL.wheel_name,
    bias_colour=WheelParameters.EURO_WHEEL.bias_colour,
    colour_ids=euro_wheel_colour_ids,
    colour_options=euro_wheel_colour_options_text)

american_wheel_user_parameters = RouletteWheelParametersUser(
    wheel_name=WheelParameters.AMERICAN_WHEEL.wheel_name,
    slots=WheelParameters.AMERICAN_WHEEL.slots,
    bias_colour=WheelParameters.AMERICAN_WHEEL.bias_colour,
    colour_ids=american_wheel_colour_ids,
    colour_options=american_wheel_colour_options_text)


@dataclass
class WheelParametersUser:
    EURO_WHEEL = euro_wheel_user_parameters
    AMERICAN_WHEEL = american_wheel_user_parameters
