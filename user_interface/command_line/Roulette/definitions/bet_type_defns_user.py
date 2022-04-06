from Games.Roulette.app.roulette_bet_base_class import RouletteWheel
from Games.Roulette.definitions.bet_type_defns import ColoursBet, StraightUpBet

"""Monologue"""


class ColoursBetUser(ColoursBet):
    def __init__(self,
                 min_bet: int = 5,
                 max_bet: int = 50,
                 bet_type_id: str = 'C',
                 win_criteria: list = None,
                 payout: int = None,
                 playing_wheel_id: str = None,
                 playing_wheel: RouletteWheel = None):
        super().__init__(min_bet, max_bet, bet_type_id, win_criteria, payout, playing_wheel_id, playing_wheel)

    def get_user_bet_choice(self):
        pass


class StraightUpBetUser(StraightUpBet):
    """Class for defining win criteria and payout for a straight up bet"""

    def __init__(self,
                 min_bet: int = 10,
                 max_bet: int = 20,
                 bet_type_id: str = 'S',
                 win_criteria: list = None,
                 payout: int = None,
                 playing_wheel_id: str = None,
                 playing_wheel: RouletteWheel = None):
        super().__init__(min_bet, max_bet, bet_type_id, win_criteria, payout, playing_wheel_id, playing_wheel)

    def get_user_bet_choice(self):
        pass


###################
# Add the newly defined user bet class to the bet_type_options dictionary below
###################
bet_type_options_user = {'C': ColoursBetUser(), 'S': StraightUpBetUser()}
