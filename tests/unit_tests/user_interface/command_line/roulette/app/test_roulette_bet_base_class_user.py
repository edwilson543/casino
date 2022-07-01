"""Unit tests for the RouletteBetUser class."""

# Standard library imports
import pytest

# Local application imports
from games.roulette.app.roulette_bet_base_class import RouletteBetParameters

# Local application UI imports
from user_interface.command_line.games.roulette.app.roulette_bet_base_class_user import RouletteBetUser
from tests.utils_command_line_testing import override_input_function_with_input_sequence


class TestRouletteBetUser:

    # Fixtures to define the bet object to be tested
    @pytest.fixture(scope="class")
    def min_bet(self):
        return 5

    @pytest.fixture(scope="class")
    def max_bet(self):
        return 10

    @pytest.fixture(scope="class")
    def test_bet_parameters(self, min_bet, max_bet):
        """Parameters for the test bet to be used throughout testing"""
        return RouletteBetParameters(bet_type_name="TEST", min_bet=min_bet, max_bet=max_bet)

    @pytest.fixture(scope="function")
    def test_bet(self, test_bet_parameters):
        """RouletteBetUser test bet object to be used throughout testing"""
        return RouletteBetUser(fixed_parameters=test_bet_parameters)

    # Tests for the non-implementation of abstract methods
    def test_determine_valid_bet_choices_text_always_raises_error(self, test_bet):
        with pytest.raises(NotImplementedError):
            test_bet.determine_valid_bet_choices_text()

    def test_get_user_bet_choice_always_raises_error(self, test_bet):
        with pytest.raises(NotImplementedError):
            test_bet.get_user_bet_choice()

    def test_get_bet_choice_string_rep_always_raises_error(self, test_bet):
        with pytest.raises(NotImplementedError):
            test_bet.get_bet_choice_string_rep()

    # Fixtures to test different betting scenarios
    @pytest.fixture(scope="class")
    def permitted_bet(self, min_bet):
        return min_bet + 1

    @pytest.fixture(scope="class")
    def unpermitted_low_bet(self, min_bet):
        return min_bet - 1

    @pytest.fixture(scope="class")
    def unpermitted_high_bet(self, max_bet):
        return max_bet + 1

    # Tests on the choose_stake_amount method
    def test_choose_stake_amount_raises_error_for_low_player_funds(self, test_bet, unpermitted_low_bet):
        with pytest.raises(ValueError):
            test_bet.choose_stake_amount(player_funds=unpermitted_low_bet)

    def test_choose_stake_amount_shortest_working_sequence(self, monkeypatch, test_bet, permitted_bet):
        input_sequence = [f"{permitted_bet}"]
        override_input_function_with_input_sequence(monkeypatch, input_sequence=input_sequence)
        stake_amount = test_bet.choose_stake_amount(player_funds=100000)
        assert stake_amount == permitted_bet

    def test_choose_stake_amount_working_sequence_with_string_cleanse(self, monkeypatch, test_bet, permitted_bet):
        input_sequence = [f"£{permitted_bet}#", f"£{permitted_bet}"]
        override_input_function_with_input_sequence(monkeypatch, input_sequence=input_sequence)
        stake_amount = test_bet.choose_stake_amount(player_funds=100000)
        assert stake_amount == permitted_bet

    def test_choose_stake_amount_longer_working_sequence(self, monkeypatch, test_bet, permitted_bet):
        input_sequence = [f"£{permitted_bet}#", f"{permitted_bet}"]
        override_input_function_with_input_sequence(monkeypatch, input_sequence=input_sequence)
        stake_amount = test_bet.choose_stake_amount(player_funds=100000)
        assert stake_amount == permitted_bet

    def test_choose_stake_amount_initially_bet_too_low(self, monkeypatch, test_bet, unpermitted_low_bet, permitted_bet):
        input_sequence = [f"{unpermitted_low_bet}", f"{permitted_bet}"]
        override_input_function_with_input_sequence(monkeypatch, input_sequence=input_sequence)
        stake_amount = test_bet.choose_stake_amount(player_funds=1000)
        assert stake_amount == permitted_bet

    def test_choose_stake_amount_initially_bet_too_high(self, monkeypatch, test_bet, unpermitted_high_bet,
                                                        permitted_bet):
        input_sequence = [f"{unpermitted_high_bet}", f"{permitted_bet}"]
        override_input_function_with_input_sequence(monkeypatch, input_sequence=input_sequence)
        stake_amount = test_bet.choose_stake_amount(player_funds=1000)
        assert stake_amount == permitted_bet
