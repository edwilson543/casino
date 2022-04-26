"""
Hierarchy of all the min/max bet parameters, which are specific to each wheel
"""
#  Todo make it so that the wheel type IDs are dynamically defined
# e.g. ColoursBet.bet_type_id in place of C, EuroWheel.wheel_id in place of E

class BetParameters:
    min_pot_to_add_more_bets = 15
    # This would ideally exceed all min_bets, so that user never gets asked to go all in after placing multiple bets

    class C:  # ColoursBet
        bet_type_id = 'C'

        class E:  # EuroWheel
            min_bet = 5
            max_bet = 50

        class A:  # AmericanWheel
            min_bet = 5
            max_bet = 50

    class S:  # StraightUpBet
        bet_type_id = 'S'

        class E:  # EuroWheel
            min_bet = 2
            max_bet = 20

        class A:  # AmericanWheel
            min_bet = 2
            max_bet = 20
