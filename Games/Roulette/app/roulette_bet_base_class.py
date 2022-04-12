from Games.games_base_classes import Bet
from Games.Roulette.app.roulette_wheel_base_class import RouletteWheel
from math import floor

"""
Separated this out because the RouletteBet base class uses RouletteWheel object as a parameter in the calculate 
payout method. Alternatively this could be transferred into the same module as the roulette wheel base class.
"""


class RouletteBet(Bet):
    """Each bet on the Roulette wheel will be defined as a subclass of this class."""

    def __init__(self,
                 min_bet: int,
                 max_bet: int,
                 bet_type_id: str):
        super().__init__(min_bet, max_bet, bet_type_id)

    def determine_win_criteria(self, *args, **kwargs):
        """Abstract method for calculating the win criteria of a given bet - will be bet specific.
        The determine_win_criteria method will be used to take an input and generate a list of winning slot for a
        given bet"""
        pass

    def calculate_payout(self, playing_wheel: RouletteWheel, win_criteria: list) -> int:
        """Calculates the payout of a £1 roulette bet, determined by using the bias_wheel_size (which ignores the
        'bias_colour') when calculating the probability of winning, so that the return always reflects a degree of
        'the house always wins."""
        win_probability_over_estimate = len(win_criteria) / playing_wheel.bias_wheel_size()
        return floor(1 / win_probability_over_estimate)

    # TODO probably want to get rid of this - it's to avoid a pycharm error prompt where RouletteBet
    # had no method get_user_bet_choice
    def get_user_bet_choice(self, *args, **kwargs):
        pass
