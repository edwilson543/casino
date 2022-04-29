from games.roulette.definitions.wheel_defns import euro_wheel
from games.roulette.definitions.bet_type_defns import ColoursBet, StraightUpBet
import pytest



class TestBetPlacementColours:
    def test_determine_win_criteria_red(self):
        """Test whether determine_win_criteria is working for a valid slot colour."""
        test_colours_bet = ColoursBet(bet_choice='red', playing_wheel=euro_wheel)  # test for colour red
        winning_set = test_colours_bet.determine_win_criteria()
        red_winning_slots = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        assert winning_set == red_winning_slots

    def test_determine_win_criteria_bias_colour(self):
        """Test whether the bias_colour is rejected as a colours bet colour choice and a value error is raised."""
        test_colours_bet = ColoursBet(bet_choice='green', playing_wheel=euro_wheel)
        with pytest.raises(ValueError):
            test_colours_bet.determine_win_criteria()

    def test_determine_win_criteria_invalid_colour(self):
        """Test whether invalid colours are rejected as a colours bet choice and a value error is raised."""
        test_colours_bet = ColoursBet(bet_choice='orange', playing_wheel=euro_wheel)
        with pytest.raises(ValueError):
            test_colours_bet.determine_win_criteria()


class TestBetPlacementStraightUp:
    def test_determine_win_criteria_valid_slot(self):
        """Test whether determine_win_criteria is working for a valid slot number."""
        test_straight_up_bet = StraightUpBet(bet_choice=1, playing_wheel=euro_wheel)  # test for slot 1
        winning_set = test_straight_up_bet.determine_win_criteria()
        one_winning_slots = [1]
        assert winning_set == one_winning_slots

    def test_determine_win_criteria_invalid_slot(self):
        """Test whether an invalid slot causes determine_win_criteria to raise a value error."""
        test_straight_up_bet = StraightUpBet(bet_choice=100, playing_wheel=euro_wheel)
        with pytest.raises(ValueError):
            test_straight_up_bet.determine_win_criteria()
