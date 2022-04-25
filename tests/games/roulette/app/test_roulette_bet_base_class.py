from games.roulette.app.roulette_bet_base_class import RouletteBet
from games.roulette.definitions.wheel_defns import EuroWheel
from games.roulette.app.roulette_wheel_base_class import wheel_spin_return

test_roulette_bet = RouletteBet(min_bet=5, max_bet=20, bet_type_id='T', stake=20,
                                bet_choice=1, win_criteria=[1], payout=720, playing_wheel=EuroWheel())

class TestRouletteBet:
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
