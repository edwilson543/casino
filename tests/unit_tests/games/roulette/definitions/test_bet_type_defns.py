"""Unit tests for each bet type definition"""

# Standard library imports
import pytest

# Local application imports
from games.roulette.app.roulette_wheel_base_class import RouletteWheel
from games.roulette.definitions.bet_type_defns import ColoursBet, StraightUpBet, SplitBet, HighLowBet, OddsEvensBet, \
    CornersBet
from games.roulette.constants.game_constants import Colour
from games.roulette.constants.wheel_constants import WheelParameters
from games.roulette.constants.bet_constants import WheelBetParameters, HighLowBetOptions, OddsEvensBetOptions


@pytest.fixture(scope="module")
def euro_wheel():
    """Wheel to be used throughout testing"""
    return RouletteWheel(parameters=WheelParameters.EURO_WHEEL)


##########
# Outside bets
##########
class TestColoursBet:

    @pytest.fixture(scope="function")
    def colours_bet(self, euro_wheel):
        return ColoursBet(fixed_parameters=WheelBetParameters.EURO_WHEEL.COLOURS_BET, playing_wheel=euro_wheel)

    def test_determine_valid_bet_choices(self, colours_bet):
        expected_options = {Colour.RED, Colour.BLACK}
        actual_options = colours_bet.determine_valid_bet_choices()
        assert expected_options == actual_options

    def test_determine_win_criteria_red(self, colours_bet):
        """Test whether determine_win_criteria is working for a valid slot colour."""
        colours_bet.set_bet_choice(bet_choice=Colour.RED)
        winning_slots = colours_bet.determine_win_criteria()
        red_winning_slots = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        assert winning_slots == red_winning_slots

    def test_determine_win_criteria_bias_colour(self, colours_bet):
        """Test whether the bias_colour is rejected as a colours bet colour choice and a value error is raised."""
        colours_bet.set_bet_choice(bet_choice=Colour.GREEN)
        with pytest.raises(ValueError):
            colours_bet.determine_win_criteria()

    def test_determine_win_criteria_invalid_colour(self, colours_bet):
        """Test whether invalid colours are rejected as a colours bet choice and a value error is raised."""
        colours_bet.set_bet_choice(bet_choice=Colour.BLUE)
        with pytest.raises(ValueError):
            colours_bet.determine_win_criteria()


class TestHighLowBet:

    @pytest.fixture(scope="function")
    def high_low_bet(self, euro_wheel):
        return HighLowBet(fixed_parameters=WheelBetParameters.EURO_WHEEL.HIGH_LOW_BET, playing_wheel=euro_wheel)

    def test_determine_win_criteria_low_bet(self, high_low_bet):
        high_low_bet.set_bet_choice(bet_choice=HighLowBetOptions.LOW)
        expected_slots = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        actual_slots = high_low_bet.determine_win_criteria()
        assert expected_slots == actual_slots

    def test_determine_win_criteria_high_bet(self, high_low_bet):
        high_low_bet.set_bet_choice(bet_choice=HighLowBetOptions.HIGH)
        expected_slots = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
        actual_slots = high_low_bet.determine_win_criteria()
        assert expected_slots == actual_slots

    def test_determine_win_criteria_high_low_invalid_choice(self, high_low_bet):
        high_low_bet.set_bet_choice(bet_choice="high")
        with pytest.raises(ValueError):
            high_low_bet.determine_win_criteria()


class TestOddsEvensBet:

    @pytest.fixture(scope="function")
    def odds_evens_bet(self, euro_wheel):
        return OddsEvensBet(fixed_parameters=WheelBetParameters.EURO_WHEEL.ODDS_EVENS_BET, playing_wheel=euro_wheel)

    def test_determine_win_criteria_odds_bet(self, odds_evens_bet):
        odds_evens_bet.set_bet_choice(bet_choice=OddsEvensBetOptions.ODDS)
        expected_slots = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
        actual_slots = odds_evens_bet.determine_win_criteria()
        assert expected_slots == actual_slots

    def test_determine_win_criteria_evens_bet(self, odds_evens_bet):
        odds_evens_bet.set_bet_choice(bet_choice=OddsEvensBetOptions.EVENS)
        expected_slots = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
        actual_slots = odds_evens_bet.determine_win_criteria()
        assert expected_slots == actual_slots

    def test_determine_win_criteria_odds_evens_invalid_choice(self, odds_evens_bet):
        odds_evens_bet.set_bet_choice(bet_choice="odds")
        with pytest.raises(ValueError):
            odds_evens_bet.determine_win_criteria()


##########
# Inside bets
##########
class TestBetStraightUpBet:

    @pytest.fixture(scope="function")
    def straight_up_bet(self, euro_wheel):
        return StraightUpBet(fixed_parameters=WheelBetParameters.EURO_WHEEL.STRAIGHTUP_BET, playing_wheel=euro_wheel)

    def test_determine_valid_bet_choices(self, straight_up_bet):
        expected_range = range(0, 37)
        actual_range = straight_up_bet.determine_valid_bet_choices()
        assert expected_range == actual_range

    def test_determine_win_criteria_valid_slot(self, straight_up_bet):
        """Test whether determine_win_criteria is working for a valid slot number."""
        straight_up_bet.set_bet_choice(bet_choice=1)
        winning_slots = straight_up_bet.determine_win_criteria()
        one_winning_slots = [1]
        assert winning_slots == one_winning_slots

    def test_determine_win_criteria_invalid_slot(self, straight_up_bet):
        """Test whether an invalid slot causes determine_win_criteria to raise a value error."""
        straight_up_bet.set_bet_choice(bet_choice=1000)
        with pytest.raises(ValueError):
            straight_up_bet.determine_win_criteria()


class TestSplitBet:

    @pytest.fixture(scope="class")
    def split_bet(self, euro_wheel):
        return SplitBet(fixed_parameters=WheelBetParameters.EURO_WHEEL.SPLIT_BET, playing_wheel=euro_wheel)

    def test_determine_valid_bet_choices_same_row(self, split_bet):
        int_one = 10
        int_two = 13
        assert split_bet.determine_valid_bet_choices(int_one=int_one, int_two=int_two)

    def test_determine_valid_bet_choices_same_col(self, split_bet):
        int_one = 10
        int_two = 11
        assert split_bet.determine_valid_bet_choices(int_one=int_one, int_two=int_two)

    def test_determine_valid_bet_choices_on_board_not_adjacent(self, split_bet):
        int_one = 10
        int_two = 12
        assert not split_bet.determine_valid_bet_choices(int_one=int_one, int_two=int_two)

    def test_determine_valid_bet_choices_neither_int_not_on_board(self, split_bet):
        int_one = 100
        int_two = -2  # numbers are adjacent to each other on the euro board
        with pytest.raises(ValueError):
            split_bet.determine_valid_bet_choices(int_one=int_one, int_two=int_two)

    def test_determine_valid_bet_choices_one_int_not_on_board(self, split_bet):
        int_one = 100
        int_two = 12  # numbers are adjacent to each other on the euro board
        with pytest.raises(ValueError):
            split_bet.determine_valid_bet_choices(int_one=int_one, int_two=int_two)

    # noinspection PyTypeChecker
    def test_determine_valid_bet_choices_one_int_not_a_valid_type_float(self, split_bet):
        int_one = 10.1
        int_two = 12
        with pytest.raises(TypeError):
            split_bet.determine_valid_bet_choices(int_one=int_one, int_two=int_two)

    # noinspection PyTypeChecker
    def test_determine_valid_bet_choices_one_int_not_a_valid_type_str(self, split_bet):
        int_one = "string"
        int_two = 12
        with pytest.raises(TypeError):
            split_bet.determine_valid_bet_choices(int_one=int_one, int_two=int_two)


class TestCornersBet:

    @pytest.fixture(scope="class")
    def corners_bet(self, euro_wheel):
        return CornersBet(fixed_parameters=WheelBetParameters.EURO_WHEEL.CORNERS_BET, playing_wheel=euro_wheel)

    def test_determine_valid_bet_choices_valid_bet(self, corners_bet):
        bet_choice = [1, 2, 4, 5]
        assert corners_bet.determine_valid_bet_choices(int_list=bet_choice)

    def test_determine_valid_bet_choices_unordered_valid_bet(self, corners_bet):
        bet_choice = [18, 15, 17, 14]
        assert corners_bet.determine_valid_bet_choices(int_list=bet_choice)

    def test_determine_valid_bet_choices_valid_tiles_invalid_bet(self, corners_bet):
        bet_choice = [1, 2, 3, 4]
        assert not corners_bet.determine_valid_bet_choices(int_list=bet_choice)

    def test_determine_valid_bet_choices_valid_type_invalid_tiles(self, corners_bet):
        bet_choice = [1, 2, 3, 400]
        with pytest.raises(ValueError):
            corners_bet.determine_valid_bet_choices(int_list=bet_choice)

    def test_determine_valid_bet_choices_invalid_type_str(self, corners_bet):
        bet_choice = [1, 2, "invalid", 4]
        with pytest.raises(TypeError):
            corners_bet.determine_valid_bet_choices(int_list=bet_choice)

    def test_determine_valid_bet_choices_invalid_type_float(self, corners_bet):
        bet_choice = [1, 2.5, 3, 4]
        with pytest.raises(TypeError):
            corners_bet.determine_valid_bet_choices(int_list=bet_choice)
