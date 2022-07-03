"""Unit tests for the RouletteBet object"""

# Standard library imports
import pytest

# Local application imports
from games.roulette.app.roulette_wheel_base_class import wheel_spin_return
from games.roulette.app.roulette_bet_base_class import RouletteBet
from games.roulette.constants.wheel_constants import WheelParameters
from games.roulette.app.roulette_wheel_base_class import RouletteWheel
from games.roulette.constants.bet_constants import default_colours_bet_parameters


class TestRouletteBet:
    """Class to test the methods defined on the roulette bet"""

    @pytest.fixture(scope="class")
    def euro_wheel(self):
        """Wheel object all bets will be tested on"""
        return RouletteWheel(parameters=WheelParameters.EURO_WHEEL)

    @pytest.fixture(scope="function")  # function as otherwise setter method calls affect later tests
    def test_bet(self, euro_wheel):
        """Basic bet object to be tested - individual tests alter attributes before testing"""
        return RouletteBet(fixed_parameters=default_colours_bet_parameters, playing_wheel=euro_wheel)

    # Tests that the abstract methods raise a notimplemented error for insufficiently defined bets
    def test_determine_valid_bet_choices_insufficiently_defined_bet(self, test_bet):
        with pytest.raises(NotImplementedError):
            test_bet.determine_valid_bet_choices()

    def test_determine_win_criteria_insufficiently_defined_bet(self, test_bet):
        with pytest.raises(NotImplementedError):
            test_bet.determine_win_criteria()

    # Tests for the calculate payout method
    def test_calculate_payout_sufficiently_defined_bet(self, test_bet):
        test_bet.set_win_criteria(win_criteria=[1, 2, 3])
        test_bet.set_stake_amount(amount=20)
        calculated_payout = test_bet.calculate_payout()
        expected_payout = 240  # as the euro wheel has 36 unbiased slots, bet choice covers 2 slots, stake is 20
        assert calculated_payout == expected_payout

    def test_calculate_payout_insufficiently_defined_bet(self, test_bet):
        with pytest.raises(AttributeError):
            test_bet.calculate_payout()

    # Tests for the evaluate_bet method
    @pytest.fixture(scope="class")
    def spin_outcome(self):
        """Spin outcome to evaluate on. Note colour return is irrelevant"""
        return wheel_spin_return(number_return=1, colour_return="")

    def test_evaluate_sufficiently_defined_winning_bet(self, test_bet, spin_outcome):
        test_bet.set_win_criteria(win_criteria=[1, 2, 3])
        test_bet.set_payout(amount=240)
        calculated_winnings = test_bet.evaluate_bet(spin_outcome)
        expected_winnings_return = 240
        assert calculated_winnings == expected_winnings_return

    def test_evaluate_sufficiently_defined_losing_bet(self, test_bet, spin_outcome):
        test_bet.set_win_criteria(win_criteria=[10, 11, 12])
        test_bet.set_payout(amount=240)
        calculated_winnings = test_bet.evaluate_bet(spin_outcome)
        expected_winnings_return = 0  # as bet has lost
        assert calculated_winnings == expected_winnings_return

    def test_evaluate_insufficiently_defined_bet(self, test_bet, spin_outcome):
        with pytest.raises(AttributeError):
            test_bet.evaluate_bet(spin_outcome=spin_outcome)
