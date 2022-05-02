from games.roulette.constants.game_constants import Colour
from games.roulette.constants.wheel_constants import WheelParameters
from games.roulette.app.roulette_wheel_base_class import RouletteWheel
from dataclasses import asdict

euro_wheel = RouletteWheel(**asdict(WheelParameters.EURO_WHEEL))  # Used throughout tests


class TestRouletteWheel:
    def test_spin_number_return_type(self):
        num_return = euro_wheel.spin().number_return
        assert type(num_return) is int

    def test_spin_colour_return_type(self):
        col_return = euro_wheel.spin().colour_return
        assert type(col_return) is Colour

    def test_bias_wheel_size_euro_wheel(self):
        assert euro_wheel.bias_wheel_size() == 36

    def test_wheel_colour_counts_red(self):
        assert euro_wheel.colour_counts(colour=Colour.RED) == 18
