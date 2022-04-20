from Games.games_base_classes import Bet
from Games.Roulette.app.roulette_wheel_base_class import RouletteWheel
from math import floor
from typing import Union


class RouletteBet(Bet):
    """
    Each bet on the Roulette wheel will be defined as a subclass of this class.
    RouletteBet <- RouletteBetUser | +
    RouletteBet <- ColoursBet, StraightUpBet, ... | + determine_win_criteria
    ColoursBetUser,... -< ColoursBet & RouletteBetUser
    """

    # maybe we want winning slots to be a set of lists, for multiple bets, likewise with payout
    # really it could be a mapping too
    def __init__(self,
                 min_bet: int,
                 max_bet: int,
                 bet_type_id: str,
                 stake: int,
                 bet_choice: Union[int, str, list],
                 win_criteria: list[int],
                 payout: int,
                 playing_wheel: RouletteWheel):
        super().__init__(min_bet, max_bet, bet_type_id, stake, bet_choice, win_criteria, payout)
        self.playing_wheel = playing_wheel

    def calculate_payout(self):
        """
        Calculates the payout of a £1 roulette bet, (unit_payout) and multiplies this by the stake.
        This is determined by using the bias_wheel_size (which ignores the 'bias_colour') when calculating the
        probability of winning, so that the return always reflects a degree of the house always wins.
        """
        win_probability_over_estimate = len(self.win_criteria) / self.playing_wheel.bias_wheel_size()
        unit_payout = floor(1 / win_probability_over_estimate)
        return unit_payout * self.stake

    def evaluate_bet(self):
        """
        Method to determine the outcome of spinning the wheel, relative to the bet_choice.
        Parameters: bet_choice - this is used to call the method 'determine_win_criteria' of the bet subclass,
        which returns a list of integers specific to the input format of the bet placement
        Returns:
        spin_outcome_num: an integer representing the slot of the roulette wheel the ball landed on
        spin_outcome_col: a string representing the colour of the roulette wheel the ball landed on
        winnings: either 0 or x>0, depending on whether the user won their bet
        """
        spin_outcome_num, spin_outcome_col = self.playing_wheel.spin()
        if spin_outcome_num in self.win_criteria:
            winnings = self.calculate_payout()
        else:
            winnings = 0
        return spin_outcome_num, spin_outcome_col, winnings
