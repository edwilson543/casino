"""Integration tests for the check_top_up_scenario method"""
from games.roulette.constants.game_constants import RouletteGameParameters
from user_interface.command_line.games.players.player_base_class_user import PlayerUser
import pytest
from tests.utils_command_line_testing import override_input_function_with_input_sequence


class TestPlayerUserIntegration:

    @pytest.fixture(scope="function")
    def test_player(self):
        """Player to be tested with the minimum number of parameters defined."""
        return PlayerUser(name="Testee", username="testee123", password="testee321")

    def test_check_top_up_scenario_pot_exceeds_all_thresholds(self, test_player):
        """Test that essentially nothing happens when player's pot exceeeds threshold for top up prompt"""
        test_player.set_active_pot(amount=RouletteGameParameters.top_up_parameters.threshold_for_top_up_prompt + 1)
        top_up, game_continues = test_player.check_top_up_scenario()
        assert top_up == 0
        assert game_continues

    @pytest.fixture(scope="class")
    def acceptable_top_up(self) -> int:
        """Acceptable top up amount to be used when testing deposits"""
        return RouletteGameParameters.top_up_parameters.min_top_up + \
               RouletteGameParameters.top_up_parameters.top_up_multiples


    def test_check_top_up_scenario_pot_between_thresholds_accepted(self, monkeypatch, test_player, acceptable_top_up):
        test_player.set_active_pot(amount=RouletteGameParameters.top_up_parameters.low_pot_forced_top_up + 1)
        input_sequence: list[str] = ["Y", f"{acceptable_top_up}", "Y"]  # Yes top up, valid amount, yes confirm
        override_input_function_with_input_sequence(monkeypatch, input_sequence=input_sequence)
        top_up, game_continues = test_player.check_top_up_scenario()
        assert top_up == acceptable_top_up
        assert game_continues

    def test_check_top_up_scenario_pot_between_thresholds_rejected(self, monkeypatch, test_player):
        test_player.set_active_pot(amount=RouletteGameParameters.top_up_parameters.low_pot_forced_top_up + 1)
        input_sequence: list[str] = ["N"]  # No don't top up
        override_input_function_with_input_sequence(monkeypatch, input_sequence=input_sequence)
        top_up, game_continues = test_player.check_top_up_scenario()
        assert top_up == 0
        assert game_continues

    def test_check_top_up_scenario_pot_below_both_thresholds_accepted(self, monkeypatch, test_player, acceptable_top_up):
        test_player.set_active_pot(amount=RouletteGameParameters.top_up_parameters.low_pot_forced_top_up - 1)
        input_sequence: list[str] = ["Y", f"{acceptable_top_up}", "Y"]  # Yes top up, valid amount, yes confirm
        override_input_function_with_input_sequence(monkeypatch, input_sequence=input_sequence)
        top_up, game_continues = test_player.check_top_up_scenario()
        assert top_up == acceptable_top_up
        assert game_continues

    def test_check_top_up_scenario_pot_below_both_thresholds_rejected(self, monkeypatch, test_player):
        test_player.set_active_pot(amount=RouletteGameParameters.top_up_parameters.low_pot_forced_top_up - 1)
        input_sequence: list[str] = ["N"]  # No don't top up
        override_input_function_with_input_sequence(monkeypatch, input_sequence=input_sequence)
        top_up, game_continues = test_player.check_top_up_scenario()
        assert top_up == 0
        assert not game_continues
