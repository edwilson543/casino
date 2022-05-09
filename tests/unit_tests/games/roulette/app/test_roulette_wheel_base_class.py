from games.roulette.constants.game_constants import Colour
from games.roulette.constants.wheel_constants import WheelParameters
from games.roulette.app.roulette_wheel_base_class import RouletteWheel
import pytest


class TestRouletteWheel:
    """Class to test that the methods on the Roulette Wheel are working"""

    @pytest.fixture(scope="class")
    def euro_wheel(self):
        return RouletteWheel(parameters=WheelParameters.EURO_WHEEL)

    def test_spin_number_return_type(self, euro_wheel):
        num_return = euro_wheel.spin().number_return
        assert type(num_return) is int

    def test_spin_colour_return_type(self, euro_wheel):
        col_return = euro_wheel.spin().colour_return
        assert type(col_return) is Colour

    def test_bias_wheel_size_euro_wheel(self, euro_wheel):
        assert euro_wheel.bias_wheel_size() == 36

    def test_wheel_colour_counts_red(self, euro_wheel):
        assert euro_wheel.colour_counts(colour=Colour.RED) == 18

    def test_wheel_colour_counts_black(self, euro_wheel):
        assert euro_wheel.colour_counts(colour=Colour.BLACK) == 18

    def test_whel_colour_counts_invalid_colour(self, euro_wheel):
        with pytest.raises(ValueError):
            euro_wheel.colour_counts(colour=Colour.BLUE)
