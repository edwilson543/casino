from games.roulette.app.roulette_wheel_base_class import RouletteWheel
from games.roulette.definitions.bet_type_defns import ColoursBet, StraightUpBet, SplitBet
from games.roulette.constants.game_constants import Colour
from games.roulette.constants.wheel_constants import WheelParameters
from games.roulette.constants.bet_constants import WheelBetParameters
from dataclasses import asdict
import pytest


#  TODO include testing of payout calculation of specific bets
#  Also, how to reject error when intentionally testing an error is thrown for an invalid type?
##########
# Objects to be used to test the relevant methods
##########
euro_wheel = RouletteWheel(**asdict(WheelParameters.EURO_WHEEL))

colours_bet = ColoursBet(**asdict(WheelBetParameters.EURO_WHEEL.COLOURS_BET))
colours_bet.set_playing_wheel(wheel=euro_wheel)

straight_up_bet = StraightUpBet(**asdict(WheelBetParameters.EURO_WHEEL.STRAIGHTUP_BET))
straight_up_bet.set_playing_wheel(wheel=euro_wheel)

split_bet = SplitBet(**asdict(WheelBetParameters.EURO_WHEEL.SPLIT_BET))
split_bet.set_playing_wheel(wheel=euro_wheel)


class TestBetPlacementColours:
    def test_determine_valid_bet_choices(self):
        expected_options = {Colour.RED, Colour.BLACK}
        actual_options = colours_bet.determine_valid_bet_choices()
        assert expected_options == actual_options

    def test_determine_win_criteria_red(self):
        """Test whether determine_win_criteria is working for a valid slot colour."""
        colours_bet.set_bet_choice(bet_choice=Colour.RED)
        winning_slots = colours_bet.determine_win_criteria()
        red_winning_slots = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        assert winning_slots == red_winning_slots

    def test_determine_win_criteria_bias_colour(self):
        """Test whether the bias_colour is rejected as a colours bet colour choice and a value error is raised."""
        colours_bet.set_bet_choice(bet_choice=euro_wheel.bias_colour)
        with pytest.raises(ValueError):
            colours_bet.determine_win_criteria()

    def test_determine_win_criteria_invalid_colour(self):
        """Test whether invalid colours are rejected as a colours bet choice and a value error is raised."""
        colours_bet.set_bet_choice(bet_choice=Colour.BLUE)
        with pytest.raises(ValueError):
            colours_bet.determine_win_criteria()


class TestBetPlacementStraightUp:
    def test_determine_valid_bet_choices(self):
        expcted_range = range(0, 37)
        actual_range = straight_up_bet.determine_valid_bet_choices()
        assert expcted_range == actual_range

    def test_determine_win_criteria_valid_slot(self):
        """Test whether determine_win_criteria is working for a valid slot number."""
        straight_up_bet.set_bet_choice(bet_choice=1)
        winning_slots = straight_up_bet.determine_win_criteria()
        one_winning_slots = [1]
        assert winning_slots == one_winning_slots

    def test_determine_win_criteria_invalid_slot(self):
        """Test whether an invalid slot causes determine_win_criteria to raise a value error."""
        straight_up_bet.set_bet_choice(bet_choice=1000)
        with pytest.raises(ValueError):
            straight_up_bet.determine_win_criteria()


class TestBetPlacementSplitBet:
    def test_determine_valid_bet_choices_same_row(self):
        int_one = 10
        int_two = 13  # numbers are adjacent to each other on the euro board
        assert split_bet.determine_valid_bet_choices(int_one=int_one, int_two=int_two)

    def test_determine_valid_bet_choices_same_col(self):
        int_one = 10
        int_two = 11  # numbers are adjacent to each other on the euro board
        assert split_bet.determine_valid_bet_choices(int_one=int_one, int_two=int_two)

    def test_determine_valid_bet_choices_on_board_not_adjacent(self):
        int_one = 10
        int_two = 12  # numbers are adjacent to each other on the euro board
        assert not split_bet.determine_valid_bet_choices(int_one=int_one, int_two=int_two)

    def test_determine_valid_bet_choices_int_not_on_board(self):
        int_one = 100
        int_two = 12  # numbers are adjacent to each other on the euro board
        assert not split_bet.determine_valid_bet_choices(int_one=int_one, int_two=int_two)

    def test_determine_valid_bet_choices_invalid_type(self):
        int_one = "string"
        int_two = 12  # numbers are adjacent to each other on the euro board
        with pytest.raises(ValueError):
            split_bet.determine_valid_bet_choices(int_one=int_one, int_two=int_two)
