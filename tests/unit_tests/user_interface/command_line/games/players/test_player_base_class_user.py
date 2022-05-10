from games.roulette.constants.game_constants import RouletteGameParameters
from user_interface.command_line.games.player_base_class_user import PlayerUser
import pytest
from tests.utils_command_line_testing import override_input_function_with_input_sequence


class TestPlayerUser:

    @pytest.fixture(scope="function")
    def test_player(self):
        """Player to be tested with the minimum number of parameters defined."""
        return PlayerUser(name="Testee", username="testee123", password="testee321")

    @pytest.fixture(scope="class")
    def acceptable_deposit(self) -> int:
        """Acceptable deposit object to be used when testing deposits"""
        return RouletteGameParameters.deposit_parameters.min_deposit + \
               RouletteGameParameters.deposit_parameters.deposit_multiples

    def test_get_initial_deposit_amount(self, monkeypatch, test_player, acceptable_deposit):
        auto_input_list = [f"{acceptable_deposit}", "Y"]
        override_input_function_with_input_sequence(monkeypatch, input_sequence=auto_input_list)
        deposit_amount = test_player.get_initial_deposit_amount()
        assert deposit_amount == acceptable_deposit
