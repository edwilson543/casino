from games.roulette.app.roulette_bet_base_class import RouletteBet
from games.roulette.definitions.bet_type_defns import ColoursBet
from games.roulette.definitions.wheel_defns import EuroWheel
from games.roulette.app.roulette_wheel_base_class import wheel_spin_return
from games.roulette.definitions.bet_parameters import BetParameters


#  TODO how to structure these?


class TestRouletteBet:
    def test_set_bet_type_id(self):
        """Test to check if the look up and setting of bet_type_id is working"""
        test_bet = ColoursBet(playing_wheel=EuroWheel())
        expected_id = 'C'
        test_bet.set_bet_type_id()
        actual_id = test_bet.bet_type_id
        assert expected_id == actual_id

    def test_set_min_max_bet(self):
        """Test to check if the look up and setting of min/max bet parameters is working"""
        test_bet_one = ColoursBet(playing_wheel=EuroWheel(), bet_type_id='C')
        expected_min_bet = BetParameters.E.ColoursBet.min_bet  # C.E. => ColoursBetEuroWheel
        expected_max_bet = BetParameters.E.ColoursBet.max_bet
        test_bet_one.set_min_max_bet()
        actual_min_bet = test_bet_one.min_bet
        actual_max_bet = test_bet_one.max_bet
        assert expected_min_bet == actual_min_bet and expected_max_bet == actual_max_bet

    def test_calculate_payout(self):
        test_bet = RouletteBet(min_bet=5, max_bet=20, bet_type_id='S', stake=20,
                               bet_choice=1, win_criteria=[1], payout=720, playing_wheel=EuroWheel())
        expected_payout = 720  # as the euro wheel has 36 unbiased slots, bet choice covers 1 slot, stake is 20
        calculated_payout = test_bet.calculate_payout()
        assert calculated_payout == expected_payout

    def test_evaluate_bet_winning(self):
        test_bet_two = RouletteBet(min_bet=5, max_bet=20, bet_type_id='S', stake=20,
                                   bet_choice=1, win_criteria=[1], payout=720, playing_wheel=EuroWheel())
        expected_winnings = 720  # as payout is set to 36 (which is derived from calculate_payout)
        spin_outcome = wheel_spin_return(number_return=1, colour_return="")
        calculated_winnings = test_bet_two.evaluate_bet(spin_outcome)
        assert calculated_winnings == expected_winnings

    def test_evaluate_bet_losing(self):
        test_bet = RouletteBet(min_bet=5, max_bet=20, bet_type_id='S', stake=20,
                               bet_choice=1, win_criteria=[1], payout=720, playing_wheel=EuroWheel())
        expected_winnings = 0  # as bet has lost
        spin_outcome = wheel_spin_return(number_return=2, colour_return="")
        calculated_winnings = test_bet.evaluate_bet(spin_outcome)
        assert calculated_winnings == expected_winnings


class TestRouletteBetIntegration:
    pass
