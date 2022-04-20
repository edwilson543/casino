from Games.Roulette.app.roulette_bet_base_class import RouletteBet
from user_interface.command_line.Roulette.app.roulette_wheel_base_class_user import RouletteWheelUser
from typing import Union


class RouletteBetUser(RouletteBet):
    def __init__(self,
                 min_bet: int,
                 max_bet: int,
                 bet_type_id: str,
                 stake: int,
                 bet_choice: Union[int, str, list],
                 payout: int,
                 playing_wheel: RouletteWheelUser,
                 winning_slots: list,
                 player_funds: int):
        super().__init__(min_bet, max_bet, bet_type_id, stake, bet_choice,
                         payout, playing_wheel, winning_slots)
        self.player_funds = player_funds

    def get_user_bet_choice_decorator(self):
        """
        get_user_bet_choice is defined specifically for each user bet.
        This method is the generic part of the definition
        """

        def wrapper_get_user_bet_choice_decorator(func):
            while True:
                bet_choice = func()
                confirmation = input(f"Confirm £{self.stake} stake on {bet_choice}?\n"
                                     f"[Y]es or [N]o\n--->").upper()
                # TODO make so it show the bet potential winnings here
                if confirmation != 'Y':
                    continue
                else:
                    print(f"£{self.stake} placed on {bet_choice}!")
                    return bet_choice

            return wrapper_get_user_bet_choice_decorator

    def choose_stake_amount(self):

        pass

    def evaluate_user_bet(self):
        pass

    ##########
    # Lower level methods
    ##########
