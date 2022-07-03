"""Unit tests for the wheel and bet type constructor"""

# Standard library imports
import pytest

# Third party imports
from numpy import all

# Local application imports
from games.roulette.app.single_player_roulette.wheel_and_bet_construction import WheelAndBetConstructor
from games.roulette.app.roulette_wheel_base_class import RouletteWheel
from games.roulette.definitions.bet_type_defns import ColoursBet
from games.roulette.constants.bet_constants import BetTypeIds, default_colours_bet_parameters
from games.roulette.constants.wheel_constants import WheelIds, euro_wheel_parameters


class TestWheelAndBetConstructor:
    """
    Class to test that the wheel and bet constructor is returning the right type objects,
    with the correct parameters.
    """
    @pytest.fixture(scope="class")
    def constructor(self):
        return WheelAndBetConstructor()

    # Wheel construction tests
    def test_get_wheel_from_wheel_name_euro_wheel_type(self, constructor):
        euro_wheel = constructor.get_wheel_from_wheel_name(wheel_name=WheelIds.EURO_WHEEL.name)
        assert type(euro_wheel) is RouletteWheel

    def test_get_wheel_from_wheel_name_euro_wheel_parameters(self, constructor):
        euro_wheel = constructor.get_wheel_from_wheel_name(wheel_name=WheelIds.EURO_WHEEL.name)
        actual_name = euro_wheel.parameters.wheel_name
        actual_slots = euro_wheel.parameters.slots
        actual_bias_colour = euro_wheel.parameters.bias_colour
        actual_board = euro_wheel.parameters.board
        assert actual_name == euro_wheel_parameters.wheel_name
        assert actual_slots == euro_wheel_parameters.slots
        assert actual_bias_colour == euro_wheel_parameters.bias_colour
        assert all(actual_board - euro_wheel_parameters.board) == 0

    def test_get_wheel_from_wheel_name_invalid_wheel(self, constructor):
        with pytest.raises(AttributeError):
            constructor.get_wheel_from_wheel_name(wheel_name="NOT_A_WHEEL")

    # Bet construction tests
    def test_get_bet_type_from_bet_type_name_colours_bet_type(self, constructor):
        colours_bet = constructor.get_bet_type_from_bet_type_name(wheel_name=WheelIds.EURO_WHEEL.name,
                                                                  bet_type_name=BetTypeIds.COLOURS_BET.name)
        assert type(colours_bet) is ColoursBet

    def test_get_bet_type_from_bet_type_name_colours_bet_parameters(self, constructor):
        colours_bet = constructor.get_bet_type_from_bet_type_name(wheel_name=WheelIds.EURO_WHEEL.name,
                                                                  bet_type_name=BetTypeIds.COLOURS_BET.name)
        actual_min_bet = colours_bet.min_bet
        actual_max_bet = colours_bet.max_bet
        assert actual_min_bet == default_colours_bet_parameters.min_bet
        assert actual_max_bet == default_colours_bet_parameters.max_bet

    def test_get_bet_from_bet_type_name_invalid_bet(self, constructor):
        with pytest.raises(AttributeError):
            constructor.get_bet_type_from_bet_type_name(bet_type_name="NOT_A_BET", wheel_name=WheelIds.EURO_WHEEL.name)
