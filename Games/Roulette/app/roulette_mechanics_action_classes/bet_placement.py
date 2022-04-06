from Games.Roulette.definitions.bet_type_defns import bet_type_options
from typing import Union


class BetPlacement:
    """
    Class to generate the winning criteria and potential payout of a given bet
    """

    def __init__(self, bet_type_id: str, wheel_id: str, stake: int):  # Note mappings not initialised
        self.bet_type_id = bet_type_id
        self.wheel_id = wheel_id
        self.stake = stake
        self.bet_type = bet_type_options[self.bet_type_id]

    def set_bet_type_wheel(self):
        """Sets the playing_wheel_id and playing_wheel attributes of the bet class"""
        self.bet_type.set_playing_wheel(self.wheel_id)

    def get_win_criteria(self, bet_choice: Union[int, str, list]) -> list:  # input list could be specified as list[int]
        """
        Finds winning list based on the user bet_choice. The bet_type attribute 'win_criteria' is set based on the
        bet choice, and then returned.
        Parameters: bet_choice. bet_choice may be: an int (user bet on a specific slot), a str (user bet on a specific
        colour), or a list (user bet on a list of slots).
        Returns: a list of the slots which would result in the user winning their bet
        """
        self.bet_type.win_criteria(bet_choice)
        return self.bet_type.win_criteria

    def get_potential_winnings(self):
        """Calculates the potential winnings of the user defined bet"""
        return self.stake * self.bet_type.calculate_payout()
