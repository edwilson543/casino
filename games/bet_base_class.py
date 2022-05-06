from abc import abstractmethod
from typing import Any


class Bet:
    def __init__(self,
                 bet_type: str,
                 min_bet: int,
                 max_bet: int,
                 stake: int,
                 bet_choice: Any,
                 win_criteria: Any,
                 payout: int):
        self.bet_type = bet_type
        self.min_bet = min_bet
        self.max_bet = max_bet
        self.stake = stake
        self.bet_choice = bet_choice
        self.win_criteria = win_criteria
        self.payout = payout

    ##########
    # Abstract methods
    ##########

    @abstractmethod
    def determine_win_criteria(self, *args, **kwargs):
        """
        Abstract method for calculating the win criteria of a given bet.
        Defined differently for each specific roulette bet (e.g. ColoursBet) in bet_type_defns.
        """
        raise NotImplementedError("Call to determine_win_criteria has referred to Bet super class")

    @abstractmethod
    def calculate_payout(self, *args, **kwargs):
        """
        Abstract method for calculating the payout for the bet
        Defined in the RouletteBet class for all roulette bets.
        """
        raise NotImplementedError("Call to calculate_payout has referred to Bet super class")

    @abstractmethod
    def evaluate_bet(self, *args, **kwargs):
        """
        Abstract method for evaluating the outcome of the bet
        Defined in the RouletteBet class for all roulette bets.
        """
        raise NotImplementedError("Call to evaluate_bet has referred to Bet super class")

    ##########
    # Setter methods for the bet attributes attributes
    ##########

    def set_min_bet(self, amount: int):
        """Sets the min_bet of the bet"""
        self.min_bet = amount

    def set_max_bet(self, amount: int):
        """Sets the max_bet of the bet"""
        self.max_bet = amount

    def set_stake_amount(self, amount: int):
        """Sets the stake attribute of the bet"""
        self.stake = amount

    def set_bet_choice(self, bet_choice: Any):
        """Sets the bet choice attribute of the bet"""
        self.bet_choice = bet_choice

    def set_win_criteria(self, win_criteria: Any):
        # Could instead call get_win_criteria here, rather than taking a parameter?
        """
        Sets the win_criteria attribute of the bet, by calling the determine_win_criteria method.
        Note the determine_win_criteria method is defined downstream (in RouletteBet), and the MRO ensures this
        downstream version of the method is called here.
        """
        self.win_criteria = win_criteria

    def set_payout(self, amount: int):
        # Could instead call calculate_payout here, rather than taking a parameter?
        """
        Sets the payout attribute of the bet, by calling the calculate_payout method.
        Note the calculate_payout method is defined downstream (in each subclass of RouletteBet defining a specific bet,
        and the MRO ensures this downstream version of the method is called here.
        """
        self.payout = amount
