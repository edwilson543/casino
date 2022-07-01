"""Unit tests for the Player base class"""

# Local application imports
from games.roulette.constants.game_constants import RouletteGameParameters

# Local application UI imports
from user_interface.games.players.player_base_class_user import PlayerUser
import pytest
from tests.utils_command_line_testing import override_input_function_with_input_sequence


class TestPlayerUserUnit:

    @pytest.fixture(scope="function")
    def test_player(self):
        """Player to be tested with the minimum number of parameters defined."""
        return PlayerUser(name="Testee", username="testee123", password="testee321")

    # get_initial_deposit_amounts fixture and tests
    @pytest.fixture(scope="class")
    def acceptable_deposit(self) -> int:
        """Acceptable deposit amount to be used when testing deposits"""
        return RouletteGameParameters.deposit_parameters.min_deposit + \
            RouletteGameParameters.deposit_parameters.deposit_multiples

    def test_get_initial_deposit_amount_shortest_valid_sequence(self, monkeypatch, test_player, acceptable_deposit):
        """Test whether get_initial_deposit_amount is working for the shortest sequence of inputs"""
        input_sequence: list[str] = [f"{acceptable_deposit}", "Y"]
        override_input_function_with_input_sequence(monkeypatch, input_sequence=input_sequence)
        deposit_amount = test_player.get_initial_deposit_amount()
        assert deposit_amount == acceptable_deposit

    def test_get_initial_deposit_amount_longer_valid_sequence(self, monkeypatch, test_player, acceptable_deposit):
        """Test whether get_initial_deposit_amount is working for the shortest sequence of inputs"""
        input_sequence: list[str] = ["3.14159", "money", f"{acceptable_deposit}", "Y"]
        override_input_function_with_input_sequence(monkeypatch, input_sequence=input_sequence)
        deposit_amount = test_player.get_initial_deposit_amount()
        assert deposit_amount == acceptable_deposit

    def test_get_initial_deposit_amount_sequence_edit_deposit(self, monkeypatch, test_player, acceptable_deposit):
        """Test whether get_initial_deposit_amount is working for the shortest sequence of inputs"""
        other_acceptable_deposit = acceptable_deposit * 2
        input_sequence: list[str] = [f"{acceptable_deposit}", "N", f"{other_acceptable_deposit}", "Y"]
        override_input_function_with_input_sequence(monkeypatch, input_sequence=input_sequence)
        deposit_amount = test_player.get_initial_deposit_amount()
        assert deposit_amount == other_acceptable_deposit

    # get_top_up_amount fixture and tests
    @pytest.fixture(scope="class")
    def acceptable_top_up(self) -> int:
        """Acceptable top up amount to be used when testing deposits"""
        return RouletteGameParameters.top_up_parameters.min_top_up + \
            RouletteGameParameters.top_up_parameters.top_up_multiples

    def test_get_top_up_amount_shortest_valid_sequence(self, monkeypatch, test_player, acceptable_top_up):
        """Test whether get_initial_deposit_amount is working for the shortest sequence of inputs"""
        input_sequence: list[str] = [f"{acceptable_top_up}", "Y"]
        override_input_function_with_input_sequence(monkeypatch, input_sequence=input_sequence)
        deposit_amount = test_player.get_top_up_amount()
        assert deposit_amount == acceptable_top_up

    def test_get_top_up_amount_longer_valid_sequence(self, monkeypatch, test_player, acceptable_top_up):
        """Test whether get_initial_deposit_amount is working for the shortest sequence of inputs"""
        input_sequence: list[str] = ["3.14159", "money", f"{acceptable_top_up}", "Y"]
        override_input_function_with_input_sequence(monkeypatch, input_sequence=input_sequence)
        deposit_amount = test_player.get_top_up_amount()
        assert deposit_amount == acceptable_top_up

    def test_get_top_up_amount_sequence_edit_deposit(self, monkeypatch, test_player, acceptable_top_up):
        """Test whether get_initial_deposit_amount is working for the shortest sequence of inputs"""
        other_acceptable_top_up = acceptable_top_up * 2
        input_sequence: list[str] = [f"{acceptable_top_up}", "N", f"{other_acceptable_top_up}", "Y"]
        override_input_function_with_input_sequence(monkeypatch, input_sequence=input_sequence)
        deposit_amount = test_player.get_top_up_amount()
        assert deposit_amount == other_acceptable_top_up

    #  see_if_user_wants_optional_top_up tests
    @pytest.fixture(scope="class")
    def optional_top_up_pot(self):
        return RouletteGameParameters.top_up_parameters.low_pot_forced_top_up + 1

    def test_see_if_user_wants_optional_top_up_valid_call_wanted(self, monkeypatch, test_player, optional_top_up_pot):
        test_player.set_active_pot(amount=optional_top_up_pot)
        input_sequence: list[str] = ["Y"]  # Yes they do want to top up
        override_input_function_with_input_sequence(monkeypatch, input_sequence=input_sequence)
        user_wants_top_up = test_player.see_if_user_wants_optional_top_up()
        assert user_wants_top_up

    def test_see_if_user_wants_optional_top_up_valid_call_unwanted(self, monkeypatch, test_player, optional_top_up_pot):
        test_player.set_active_pot(amount=optional_top_up_pot)
        input_sequence: list[str] = ["N"]  # No they don't want to top up
        override_input_function_with_input_sequence(monkeypatch, input_sequence=input_sequence)
        user_wants_top_up = test_player.see_if_user_wants_optional_top_up()
        assert not user_wants_top_up

    def test_see_if_user_wants_optional_top_up_invalid_call(self, test_player):
        test_player.set_active_pot(amount=RouletteGameParameters.top_up_parameters.threshold_for_top_up_prompt + 1)
        with pytest.raises(ValueError):
            test_player.see_if_user_wants_optional_top_up()

    #  see_if_user_wants_forced_top_up tests
    @pytest.fixture(scope="class")
    def forced_top_up_pot(self):
        return RouletteGameParameters.top_up_parameters.low_pot_forced_top_up - 1

    def test_see_if_user_wants_forced_top_up_valid_call_wanted(self, monkeypatch, test_player, forced_top_up_pot):
        test_player.set_active_pot(amount=forced_top_up_pot)
        input_sequence: list[str] = ["Y"]  # Yes they do want to top up
        override_input_function_with_input_sequence(monkeypatch, input_sequence=input_sequence)
        user_wants_top_up = test_player.see_if_user_wants_forced_top_up()
        assert user_wants_top_up

    def test_see_if_user_wants_forced_top_up_valid_call_unwanted(self, monkeypatch, test_player, forced_top_up_pot):
        test_player.set_active_pot(amount=forced_top_up_pot)
        input_sequence: list[str] = ["N"]  # No they don't want to top up
        override_input_function_with_input_sequence(monkeypatch, input_sequence=input_sequence)
        user_wants_top_up = test_player.see_if_user_wants_forced_top_up()
        assert not user_wants_top_up

    def test_see_if_user_wants_forced_top_up_invalid_call(self, test_player):
        test_player.set_active_pot(amount=RouletteGameParameters.top_up_parameters.low_pot_forced_top_up + 1)
        with pytest.raises(ValueError):
            test_player.see_if_user_wants_forced_top_up()