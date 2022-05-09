from games.roulette.app.roulette_wheel_base_class import wheel_spin_return
from games.roulette.app.roulette_wheel_base_class import RouletteWheel
from games.roulette.definitions.bet_type_defns import ColoursBet, StraightUpBet, SplitBet
from games.roulette.app.single_player_roulette.single_player_table import SinglePlayerRouletteTable
from games.roulette.constants.wheel_constants import WheelParameters
from games.roulette.constants.bet_constants import WheelBetParameters

# Wheel to be used throughout testing
euro_wheel = RouletteWheel(parameters=WheelParameters.EURO_WHEEL)

# Bets to be used throughout testing
colours_bet = ColoursBet(fixed_parameters=WheelBetParameters.EURO_WHEEL.COLOURS_BET, playing_wheel=euro_wheel)
straight_up_bet = StraightUpBet(fixed_parameters=WheelBetParameters.EURO_WHEEL.STRAIGHTUP_BET, playing_wheel=euro_wheel)
split_bet = SplitBet(fixed_parameters=WheelBetParameters.EURO_WHEEL.SPLIT_BET, playing_wheel=euro_wheel)

##########
# Table object ot be tested
##########
table = SinglePlayerRouletteTable()


class TestSinglePlayerRouletteTable:
    def test_evaluate_all_active_bets_list_three_different_bets_all_winners(self):
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


    def test_evaluate_all_active_bets_list_three_different_bets_one_winner(self):
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

    def test_evaluate_all_active_bets_list_three_different_bets_no_winners(self):
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
