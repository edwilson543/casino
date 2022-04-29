from games.roulette.definitions.bet_type_defns import ColoursBet
from games.roulette.app.roulette_wheel_base_class import wheel_spin_return
from games.roulette.definitions.bet_parameters import WheelBetParameters
from games.roulette.definitions.wheel_parameters_and_defns import euro_wheel

#  TODO how to structure these?
# Note that ColoursBet used throughout testing, but it's tests are for RouletteBet methods


class TestRouletteBet:
    def test_set_min_max_bet(self):
        """Test to check if the look up and setting of min/max bet parameters is working"""
        test_bet_one = ColoursBet(playing_wheel=euro_wheel)
        expected_min_bet = WheelBetParameters.EURO_WHEEL.COLOURS_BET.min_bet
        expected_max_bet = WheelBetParameters.EURO_WHEEL.COLOURS_BET.max_bet
        test_bet_one.set_min_max_bet()
        actual_min_bet = test_bet_one.min_bet
        actual_max_bet = test_bet_one.max_bet
        assert expected_min_bet == actual_min_bet and expected_max_bet == actual_max_bet

    def test_calculate_payout(self):
        test_bet = ColoursBet(min_bet=5, max_bet=20, stake=20,
                              bet_choice=1, win_criteria=[1], payout=720, playing_wheel=euro_wheel)
        expected_payout = 720  # as the euro wheel has 36 unbiased slots, bet choice covers 1 slot, stake is 20
        calculated_payout = test_bet.calculate_payout()
        assert calculated_payout == expected_payout

    def test_evaluate_bet_winning(self):
        test_bet = ColoursBet(min_bet=5, max_bet=20, stake=20,
                              bet_choice=1, win_criteria=[1], payout=720, playing_wheel=euro_wheel)
        expected_winnings = 720  # as payout is set to 36 (which is derived from calculate_payout)
        spin_outcome = wheel_spin_return(number_return=1, colour_return="")
        calculated_winnings = test_bet.evaluate_bet(spin_outcome)
        assert calculated_winnings == expected_winnings

    def test_evaluate_bet_losing(self):
        test_bet = ColoursBet(min_bet=5, max_bet=20, stake=20,
                              bet_choice=1, win_criteria=[1], payout=720, playing_wheel=euro_wheel)
        expected_winnings = 0  # as bet has lost
        spin_outcome = wheel_spin_return(number_return=2, colour_return="")
        calculated_winnings = test_bet.evaluate_bet(spin_outcome)
        assert calculated_winnings == expected_winnings


class TestRouletteBetIntegration:
    pass
