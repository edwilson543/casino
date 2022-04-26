from games.roulette.app.roulette_bet_base_class import RouletteBet
from games.roulette.definitions.bet_type_defns import ColoursBet
from games.roulette.definitions.wheel_defns import EuroWheel
from games.roulette.app.roulette_wheel_base_class import wheel_spin_return
from games.roulette.definitions.bet_parameters import BetParameters

#  TODO maybe these should be instances of the TestRoulleteBet class?
test_roulette_bet_no_min_max_bet = ColoursBet(playing_wheel=EuroWheel())

test_roulette_bet = RouletteBet(min_bet=5, max_bet=20, bet_type_id='T', stake=20,
                                bet_choice=1, win_criteria=[1], payout=720, playing_wheel=EuroWheel())

class TestRouletteBet:
    def test_set_min_max_bet(self):
        """Test to check if the look up and setting of min/max bet parameters is working"""
        expected_min_bet = BetParameters.ColoursBet.EuroWheel.min_bet
        expected_max_bet = BetParameters.ColoursBet.EuroWheel.max_bet
        test_roulette_bet_no_min_max_bet.set_min_max_bet()
        actual_min_bet = test_roulette_bet_no_min_max_bet.min_bet
        actual_max_bet = test_roulette_bet_no_min_max_bet.max_bet
        assert expected_min_bet == actual_min_bet and expected_max_bet == actual_max_bet

    def test_calculate_payout(self):
        expected_payout = 720  # as the euro wheel has 36 unbiased slots, bet choice covers 1 slot, stake is 20
        calculated_payout = test_roulette_bet.calculate_payout()
        assert calculated_payout == expected_payout

    def test_evaluate_bet_winning(self):
        expected_winnings = 720  # as payout is set to 36 (which is derived from calculate_payout)
        spin_outcome = wheel_spin_return(number_return=1, colour_return="")
        calculated_winnings = test_roulette_bet.evaluate_bet(spin_outcome)
        assert calculated_winnings == expected_winnings

    def test_evaluate_bet_losing(self):
        expected_winnings = 0  # as bet has lost
        spin_outcome = wheel_spin_return(number_return=2, colour_return="")
        calculated_winnings = test_roulette_bet.evaluate_bet(spin_outcome)
        assert calculated_winnings == expected_winnings
