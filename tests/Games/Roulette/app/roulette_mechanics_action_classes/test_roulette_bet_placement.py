from Games.Roulette.app.roulette_mechanics_action_classes.bet_placement_evaluation import BetPlacementEvaluation
from Games.Roulette.definitions.wheel_defns import EuroWheel
import pytest

test_bet_placer_colours = BetPlacementEvaluation(bet_type_id='C', stake=10, playing_wheel=EuroWheel())


class TestBetPlacementColours:
    def test_get_winning_slots_colours_red(self):
        """Test to see if get_winning_slots correctly calls the bet_type's get_winning_slots_list method"""
        winning_set = test_bet_placer_colours.determine_win_criteria(bet_choice='red')  # test for colour red
        red_winning_slots = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        assert winning_set == red_winning_slots

    def test_get_winning_slots_colours_green(self):
        winning_set = test_bet_placer_colours.determine_win_criteria(bet_choice='green') # test for colour green
        assert winning_set == [0]

    def test_get_winning_slots_invalid_colour(self):
        """Test to see if the error in the bet_type's get_winning_slots_list is working"""
        with pytest.raises(ValueError):
            test_bet_placer_colours.determine_win_criteria(bet_choice='orange')

    def test_get_potential_winnings_red_bet(self):
        red_winning_slots = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        calculated_red_payout = test_bet_placer_colours.get_winnings(winning_slots_list=red_winning_slots)
        expected_red_payout = 2 * test_bet_placer_colours.stake
        assert calculated_red_payout == expected_red_payout



test_bet_placer_straight_up = BetPlacementEvaluation(bet_type_id='S', stake=10, playing_wheel=EuroWheel())

class TestBetPlacementStraightUp:
    pass
