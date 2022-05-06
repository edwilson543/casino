from games.roulette.app.roulette_wheel_base_class import wheel_spin_return
from games.roulette.app.roulette_bet_base_class import RouletteBet
from games.roulette.constants.wheel_constants import WheelParameters
from games.roulette.app.roulette_wheel_base_class import RouletteWheel
from games.roulette.constants.bet_constants import default_colours_bet_parameters
import pytest


euro_wheel = RouletteWheel(parameters=WheelParameters.EURO_WHEEL)  # Used throughout testing here


class TestRouletteBet:
    def test_determine_valid_bet_choices(self):
        with pytest.raises(NotImplementedError):
            RouletteBet(fixed_parameters=default_colours_bet_parameters).determine_valid_bet_choices()

    def test_determine_win_criteria(self):
        with pytest.raises(NotImplementedError):
            RouletteBet(fixed_parameters=default_colours_bet_parameters).determine_win_criteria()

    def test_calculate_payout_sufficiently_defined_bet(self):
        test = RouletteBet(fixed_parameters=default_colours_bet_parameters,
                           stake=20, win_criteria=[1, 2, 3], playing_wheel=euro_wheel)
        expected_payout = 240  # as the euro wheel has 36 unbiased slots, bet choice covers 2 slots, stake is 20
        calculated_payout = test.calculate_payout()
        assert calculated_payout == expected_payout

    def test_evaluate_sufficiently_defined_winning(self):
        test = RouletteBet(fixed_parameters=default_colours_bet_parameters,
                           win_criteria=[1, 2, 3], payout=240)
        expected_winnings_return = 240
        spin_outcome = wheel_spin_return(number_return=1, colour_return="")  # Colour return is irrelevant here
        calculated_winnings = test.evaluate_bet(spin_outcome)
        assert calculated_winnings == expected_winnings_return

    def test_evaluate_sufficiently_defined_losing_bet(self):
        test_bet = RouletteBet(fixed_parameters=default_colours_bet_parameters,
                               win_criteria=[1, 2, 3], payout=240, playing_wheel=euro_wheel)
        expected_winnings_return = 0  # as bet has lost
        spin_outcome = wheel_spin_return(number_return=10, colour_return="")
        calculated_winnings = test_bet.evaluate_bet(spin_outcome)
        assert calculated_winnings == expected_winnings_return

    def test_calculate_payout_undefined_bet(self):
        with pytest.raises(AttributeError):
            RouletteBet(fixed_parameters=default_colours_bet_parameters).calculate_payout()
