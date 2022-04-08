from Games.Roulette.app.roulette_wheel_base_class import RouletteWheel
from Games.Roulette.definitions.bet_type_defns import bet_type_options
from typing import Union


class BetPlacement:
    """
    Class to generate the winning criteria and potential payout of a given bet
    """

    def __init__(self,
                 bet_type_id: str,
                 stake: int,
                 playing_wheel: RouletteWheel):
        self.bet_type_id = bet_type_id
        self.stake = stake
        self.playing_wheel = playing_wheel

        self.bet_type = bet_type_options[self.bet_type_id]

    def get_winning_slots(self, bet_choice: Union[int, str, list]) -> list[int]:
        """
        Finds winning list based on the user bet_choice. The bet_type attribute 'win_criteria' is set based on the
        bet choice, and then returned.
        Parameters: bet_choice - may be: an int (user bet on a specific slot), a str (user bet on a specific
        colour), or a list (user bet on a list of slots).
        Returns: a list of the slots which would result in the user winning their bet. This is done by accessing the
        'get_winning_slots_list' method of the specific bet class.
        """
        return self.bet_type.get_winning_slots_list(playing_wheel=self.playing_wheel, choice=bet_choice)

    def get_potential_winnings(self, winning_slots_list):
        """Calculates the potential winnings of the user defined bet.
        Maybe the 'winning_slots_list' parameter could instead call the get_winning_slots method"""
        unit_payout = self.bet_type.calculate_payout(playing_wheel=self.playing_wheel, win_criteria=winning_slots_list)
        return self.stake * unit_payout
