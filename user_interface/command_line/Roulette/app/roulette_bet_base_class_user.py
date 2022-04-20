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
                 playing_wheel: RouletteWheelUser,
                 player_funds: int):
        super().__init__(min_bet, max_bet, bet_type_id)
        self.stake = stake
        self.bet_choice = bet_choice
        self.playing_wheel = playing_wheel
        self.player_funds = player_funds

    def