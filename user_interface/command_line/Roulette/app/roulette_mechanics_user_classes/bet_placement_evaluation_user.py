from Games.Roulette.app.roulette_wheel_base_class import RouletteWheel
from Games.Roulette.app.roulette_mechanics_action_classes.bet_placement_evaluation import BetPlacementEvaluation
from user_interface.command_line.Roulette.definitions.bet_type_defns_user import bet_type_options_user
from Games.Roulette.definitions.game_parameters import pause_durations

from typing import Union
from time import sleep


class BetPlacementEvaluationUser(BetPlacementEvaluation):
    """Purpose of this subclass is to inherit the get_winning_slots and get_potential_winnings
    methods from the BetPlacement class, and
    to add the get_user_bet_choice method which is shown below"""

    def __init__(self,
                 bet_type_id: str,
                 stake: int,
                 playing_wheel: RouletteWheel):
        super().__init__(bet_type_id, stake, playing_wheel)
        self.bet_type = bet_type_options_user[self.bet_type_id]
        # TODO make bet_type a parameter

    def get_user_bet_choice(self) -> Union[int, str, list]:
        """gets user to specify their bet (navigation unique to the bet type)
        then uses generic confirmation by displaying potential payout.
        If confirmation is no, they can place a new bet choice."""
        while True:
            bet_choice = self.bet_type.get_user_bet_choice(playing_wheel=self.playing_wheel)
            confirmation = input(f"Confirm £{self.stake} stake on {bet_choice}?\n"
                                 f"Winning this bet would return: £"
                                 f"{self.get_winnings(self.get_winning_slots(bet_choice))}\n"
                                 f"[Y]es or [N]o\n--->").upper()
            if confirmation != 'Y':
                continue
            else:
                print(f"£{self.stake} placed on {bet_choice}!")
                return bet_choice

    def evaluate_user_bet(self, bet_choice: Union[int, str, list]) -> int:
        """
        Method to give the user the outcome of their bet based on a spin of the wheel, using the evaluate_bet
        method from the parent class BetPlacementEvaluation
        """
        spin_outcome_num, spin_outcome_col, winnings = self.evaluate_bet(bet_choice=bet_choice)
        self.get_user_to_spin_wheel()
        print("Wheel spinning...")
        sleep(pause_durations['medium'])
        print(f"Ball has landed on {spin_outcome_num}, ({spin_outcome_col.upper()})!")
        if winnings > 0:
            sleep(pause_durations['medium'])
            print(f"Congratulations! You have won £{winnings}!\n")
        elif winnings == 0:
            sleep(pause_durations['medium'])
            print("Better luck next time, your bet did not win.")
        else:
            raise ValueError("Invalid winnings amount encountered in evaluate_user_bet.")
        return winnings


    @staticmethod
    def get_user_to_spin_wheel():
        """Low level method just to get the user to type spin in the game flow above"""
        while True:
            user_ready = input("Type 'SPIN' to spin the wheel!\n--->").upper()
            if user_ready != "SPIN":
                print("Please try spinning the wheel again.")
                continue
            else:
                break
