from Games.Roulette.app.roulette_bet_base_class import RouletteBet
from user_interface.command_line.Roulette.app.roulette_wheel_base_class_user import RouletteWheelUser
from typing import Union


class RouletteBetUser(RouletteBet):
    def __init__(self,
                 min_bet: int,
                 max_bet: int,
                 bet_type_id: str,
                 stake: int, # new attributes here down - some to be given to parent class
                 bet_choice: Union[int, str, list],
                 player_funds: int,
                 playing_wheel: RouletteWheelUser):
        super().__init__(min_bet, max_bet, bet_type_id)
        self.stake = stake
        self.bet_choice = bet_choice
        self.player_funds = player_funds
        self.playing_wheel = playing_wheel
        