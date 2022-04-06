from Games.games_base_classes import Bet
from roulette_wheel_base_class import RouletteWheel
from Games.Roulette.definitions.wheel_defns import wheel_options
from math import floor

""" Separated this out because the RouletteBet base class uses RouletteWheel object as a class attribute,
so it felt a bit messy to have the two base class defintions in the same module.
No doubt there is a better way of doing this - in particular this class definition relies on the wheel_options 
dictionary, which we talked about getting rid of.
I think the key problems to consider are:
1) Need to be able to calculate payout for all bets, which is defined using RouletteWheel bias_wheel_size method
2) Need to be able to set the playing wheel for the net, which relies on the wheel_options dictionary"""


class RouletteBet(Bet):
    """Each bet on the Roulette wheel will be defined as a subclass of this class."""

    def __init__(self,
                 min_bet: int,
                 max_bet: int,
                 bet_type_id: str,
                 win_criteria: list,
                 payout: int,
                 playing_wheel_id: str,
                 playing_wheel: RouletteWheel):
        super().__init__(min_bet, max_bet, bet_type_id, win_criteria, payout)
        self.playing_wheel_id = playing_wheel_id
        self.playing_wheel = playing_wheel

    def determine_win_criteria(self):
        """Abstract method for calculating the win crtieria of a given bet - will be bet specific.
        The determine_win_criteria method will be used to take an input and generate a list of winning slot for a
        given bet"""
        pass

    def calculate_payout(self):
        """Calculates the payout of a £1 roulette bet, determined by using the bias_wheel_size (which ignores the
        'bias_colour') when calculating the probability of winning, so that the return always reflects a degree of
        'the house always wins."""
        win_probability_over_estimate = len(self.win_criteria) / self.playing_wheel.bias_wheel_size()
        self.payout = floor(1 / win_probability_over_estimate)

    # Methods to allow the setting and changing of the playing wheel
    def set_playing_wheel(self, wheel_id):
        """Defined so that in the game flow the playing wheel can be set.
        This method sets both the wheel_id and playing wheel"""
        self.playing_wheel_id(self, wheel_id)
        self.playing_wheel = wheel_options[self.playing_wheel_id]

    @property
    def playing_wheel_id(self):
        """Defined so that in the game flow the playing wheel can be set"""
        return self.playing_wheel_id

    @playing_wheel_id.setter
    def playing_wheel_id(self, wheel_id: str):
        """Defined so that in the game flow the playing wheel can be set"""
        self.playing_wheel_id = wheel_id
