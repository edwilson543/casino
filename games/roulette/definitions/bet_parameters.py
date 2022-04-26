"""
Hierarchy of all the min/max bet parameters, which are specific to each wheel
"""


class BetParameters:
    min_pot_to_add_more_bets = 15
    # This would ideally exceed all min_bets, so that user never gets asked to go all in after placing multiple bets

    class ColoursBet:
        bet_type_id = 'C'

        class EuroWheel:
            min_bet = 5
            max_bet = 50

        class AmericanWheel:
            min_bet = 5
            max_bet = 50

    class StraightUpBet:
        bet_type_id = 'S'

        class EuroWheel:
            min_bet = 2
            max_bet = 20

        class AmericanWheel:
            min_bet = 2
            max_bet = 20
