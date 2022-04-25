from games.games_base_classes import Player
from games.roulette.app.roulette_wheel_base_class import wheel_spin_return
from games.roulette.definitions.wheel_defns import WHEEL_TYPES


class RouletteGame:
    def __init__(self,
                 active_player: Player = None,
                 active_wheel_id: str = None,
                 active_wheel: WHEEL_TYPES = None,
                 active_all_bets_list: list = None,
                 active_total_stake: int = 0,
                 active_spin_outcome: wheel_spin_return = None,
                 active_bet_win_count: int = 0,
                 active_total_winnings: int = 0):
        self.active_player = active_player
        self.active_wheel_id = active_wheel_id
        self.active_wheel = active_wheel
        self.active_all_bets_list = active_all_bets_list
        self.active_total_stake = active_total_stake
        self.active_spin_outcome = active_spin_outcome
        self.active_bet_win_count = active_bet_win_count
        self.active_total_winnings = active_total_winnings

    def evaluate_all_active_bets_list(self):
        """Method to evaluate each active bet in the list"""
        for bet in self.active_all_bets_list:
            winnings = bet.evaluate_bet(spin_outcome=self.active_spin_outcome)
            if winnings > 0:
                self.active_bet_win_count += 1
                self.active_total_winnings += winnings
        self.active_player.add_winnings_to_pot(amount=self.active_total_winnings)

    def reset_game_attributes(self):
        self.active_spin_outcome = None
        self.active_bet_win_count = 0
        self.active_total_winnings = 0
