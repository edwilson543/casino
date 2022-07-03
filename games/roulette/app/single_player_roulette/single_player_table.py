"""
Module defining a SinglePlayerRouletteTable object that's used to implement certain methods relevant to the core
game flow.
Note that the methods implemented in this module / the class below are restricted to those which are independent of the
UI, and as such are fairly limited in number (as most of the game flow is UI driven in this application).
"""

# Standard library imports
from typing import Tuple

# Local application imports
from games.players.player_base_class import PLAYER_TYPES
from games.players.player_database_manager import PlayerDatabaseManager
from games.roulette.app.roulette_wheel_base_class import wheel_spin_return
from games.roulette.app.roulette_wheel_base_class import WHEEL_TYPES
from games.roulette.app.single_player_roulette.wheel_and_bet_construction import \
    WheelAndBetConstructor


class SinglePlayerRouletteTable:
    def __init__(self,
                 active_player: PLAYER_TYPES = None,
                 active_wheel: WHEEL_TYPES = None,
                 constructor=WheelAndBetConstructor(),
                 player_database_manager=PlayerDatabaseManager(),
                 active_all_bets_list: list = None):
        self.active_player = active_player
        self.active_wheel = active_wheel
        self.constructor = constructor
        self.player_database_manager = player_database_manager
        self.active_all_bets_list = active_all_bets_list

    def evaluate_all_active_bets_list(self, spin_outcome: wheel_spin_return) -> Tuple[int, int]:
        """
        Method to evaluate each active bet in the list, one by one, and accumulate the winnings and number of wins.
        Returns:
        bet_win_count - the number of wins that the player achieved from an individual spin
        total_winnings - the total quantity of winnings that the player will receive from the same individual spin
        """
        bet_winnings = [bet.evaluate_bet(spin_outcome=spin_outcome) for bet in self.active_all_bets_list]
        bet_win_count = sum(winnings > 0 for winnings in bet_winnings)
        total_winnings = sum(bet_winnings)
        return bet_win_count, total_winnings

    def terminate_player_session(self) -> None:
        """
        Method to upload a player's data to the database at the end of their session
        """
        self.active_player.reset_total_active_stake()
        self.active_player.set_session_end_time_to_now()
        self.player_database_manager.upload_player(self.active_player)
