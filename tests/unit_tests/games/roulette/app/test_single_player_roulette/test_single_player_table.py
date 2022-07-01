"""Module containing unit tests for the SinglePlayerRouletteTable class."""

# Standard library imports
import pytest

# Local application imports
from games.roulette.app.roulette_wheel_base_class import wheel_spin_return
from games.roulette.app.roulette_wheel_base_class import RouletteWheel
from games.roulette.definitions.bet_type_defns import ColoursBet, StraightUpBet, SplitBet
from games.roulette.app.single_player_roulette.single_player_table import SinglePlayerRouletteTable
from games.roulette.constants.wheel_constants import WheelParameters
from games.roulette.constants.bet_constants import WheelBetParameters


class TestSinglePlayerRouletteTable:
    """Class for testing that the methods on the SinglePlayerRouletteTable are working."""

    @pytest.fixture(scope="function")
    def table(self):
        """Table object that will be tested throughout this class"""
        return SinglePlayerRouletteTable()

    # Secondary test fixtures
    @pytest.fixture(scope="class")
    def euro_wheel(self):
        """Wheel that the table is being tested on"""
        return RouletteWheel(parameters=WheelParameters.EURO_WHEEL)

    @pytest.fixture(scope="function")
    def colours_bet(self, euro_wheel):
        """First generic bet used to test the table"""
        return ColoursBet(fixed_parameters=WheelBetParameters.EURO_WHEEL.COLOURS_BET, playing_wheel=euro_wheel)

    @pytest.fixture(scope="function")
    def straight_up_bet(self, euro_wheel):
        """Second generic bet used to test the table"""
        return StraightUpBet(fixed_parameters=WheelBetParameters.EURO_WHEEL.STRAIGHTUP_BET, playing_wheel=euro_wheel)

    @pytest.fixture(scope="function")
    def split_bet(self, euro_wheel):
        """Third generic bet used to test the table"""
        return SplitBet(fixed_parameters=WheelBetParameters.EURO_WHEEL.SPLIT_BET, playing_wheel=euro_wheel)

    # Test methods
    def test_evaluate_all_active_bets_list_three_different_bets_all_winners(self,
                                                                            table, colours_bet, straight_up_bet,
                                                                            split_bet):
        colours_bet.set_payout(amount=50)
        colours_bet.set_win_criteria(win_criteria=[1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36])
        straight_up_bet.set_payout(amount=720)
        straight_up_bet.set_win_criteria(win_criteria=[1])
        split_bet.set_payout(amount=360)
        split_bet.set_win_criteria(win_criteria=[1, 2])

        table.active_all_bets_list = [colours_bet, straight_up_bet, split_bet]

        spin_outcome = wheel_spin_return(number_return=1, colour_return="")
        bet_win_count, total_winnings = table.evaluate_all_active_bets_list(spin_outcome=spin_outcome)
        assert bet_win_count == 3
        assert total_winnings == 1130

    def test_evaluate_all_active_bets_list_three_different_bets_one_winner(self,
                                                                           table, colours_bet, straight_up_bet,
                                                                           split_bet):
        colours_bet.set_payout(amount=50)
        colours_bet.set_win_criteria(win_criteria=[1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36])
        straight_up_bet.set_payout(amount=720)
        straight_up_bet.set_win_criteria(win_criteria=[1])
        split_bet.set_payout(amount=360)
        split_bet.set_win_criteria(win_criteria=[1, 2])

        table.active_all_bets_list = [colours_bet, straight_up_bet, split_bet]

        spin_outcome = wheel_spin_return(number_return=23, colour_return="")
        bet_win_count, total_winnings = table.evaluate_all_active_bets_list(spin_outcome=spin_outcome)
        assert bet_win_count == 1
        assert total_winnings == 50

    def test_evaluate_all_active_bets_list_three_different_bets_no_winners(self,
                                                                           table, colours_bet, straight_up_bet,
                                                                           split_bet):
        colours_bet.set_payout(amount=50)
        colours_bet.set_win_criteria(win_criteria=[1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36])
        straight_up_bet.set_payout(amount=720)
        straight_up_bet.set_win_criteria(win_criteria=[1])
        split_bet.set_payout(amount=360)
        split_bet.set_win_criteria(win_criteria=[1, 2])

        table.active_all_bets_list = [colours_bet, straight_up_bet, split_bet]

        spin_outcome = wheel_spin_return(number_return=33, colour_return="")
        bet_win_count, total_winnings = table.evaluate_all_active_bets_list(spin_outcome=spin_outcome)
        assert bet_win_count == 0
        assert total_winnings == 0
