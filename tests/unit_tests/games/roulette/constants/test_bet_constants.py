from games.roulette.constants.bet_constants import WheelDefaultBetOptionsAndParameters, default_colours_bet_parameters, \
    default_straight_up_bet_parameters
from games.roulette.constants.bet_constants import InsideBetTypePrompts, OutsideBetTypePrompts
import pytest


class TestIndividualWheelMinMaxBetParameters:

    @pytest.fixture(scope="class")
    def default_wheel_bet_options(self):
        return WheelDefaultBetOptionsAndParameters(COLOURS_BET=default_colours_bet_parameters,
                                                            STRAIGHTUP_BET=default_straight_up_bet_parameters)

    def test_construct_wheel_bet_options_prompt(self, default_wheel_bet_options):
        expected_prompt = f"Outside: {OutsideBetTypePrompts.COLOURS_BET.value}, " \
                          f"{OutsideBetTypePrompts.HIGH_LOW_BET.value}, " \
                          f"{OutsideBetTypePrompts.ODDS_EVENS_BET.value}" \
                          f"\n" \
                          f"Inside: {InsideBetTypePrompts.STRAIGHTUP_BET.value}, " \
                          f"{InsideBetTypePrompts.SPLIT_BET.value}, " \
                          f"{InsideBetTypePrompts.CORNERS_BET.value}"
        actual_prompt = default_wheel_bet_options.construct_wheel_bet_options_prompt()
        assert expected_prompt == actual_prompt
