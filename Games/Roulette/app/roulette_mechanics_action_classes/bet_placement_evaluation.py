from Games.Roulette.app.roulette_wheel_base_class import RouletteWheel
from Games.Roulette.definitions.bet_type_defns import bet_type_options
from typing import Union


class BetPlacementEvaluation:
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

        self.bet_type = bet_type_options[self.bet_type_id]  #TODO replace with data storage thing

    def evaluate_bet(self, bet_choice: Union[int, str, list]) -> (int, str, bool):
        """
        Method to determine the outcome of spinning the wheel, relative to the user's bet.
        Parameters: bet_choice - this is used to call the method 'get_winning_slots_list' of the bet subclass,
        which returns a list of integers specific to the input format of the bet placement
        Returns:
        spin_outcome_num: an integer representing the slot of the roulette wheel the ball landed on
        spin_outcome_col: a string representing the colour of the roulette wheel the ball landed on
        winnings: either 0 or x>0, depending on whether the user won their bet
        """
        winning_slots_list = self.get_winning_slots(bet_choice=bet_choice)
        spin_outcome_num, spin_outcome_col = self.playing_wheel.spin()
        if spin_outcome_num in winning_slots_list:
            winnings = self.get_winnings(winning_slots_list=winning_slots_list)
        else:
            winnings = 0
        return spin_outcome_num, spin_outcome_col, winnings

    def get_winnings(self, winning_slots_list: list[int]) -> int:
        """
        Calculates the potential winnings of the user defined bet.
        Maybe the 'winning_slots_list' parameter could instead call the get_winning_slots method
        """
        unit_payout = self.bet_type.calculate_payout(playing_wheel=self.playing_wheel, win_criteria=winning_slots_list)
        return self.stake * unit_payout

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
