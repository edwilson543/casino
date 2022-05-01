from games.player_base_class import PLAYER_TYPES
from games.roulette.app.roulette_wheel_base_class import wheel_spin_return
from games.roulette.app.roulette_wheel_base_class import WHEEL_TYPES
from games.roulette.app.single_player_roulette.wheel_and_bet_type_selection import \
    WheelBoardBetConstructor


class SinglePlayerRouletteTable:
    def __init__(self,
                 active_player: PLAYER_TYPES = None,
                 active_wheel: WHEEL_TYPES = None,
                 constructor=WheelBoardBetConstructor(),
                 active_all_bets_list: list = None):
        self.active_player = active_player
        self.active_wheel = active_wheel
        self.constructor = constructor
        self.active_all_bets_list = active_all_bets_list


    def evaluate_all_active_bets_list(self, spin_outcome: wheel_spin_return):
        """
        Method to evaluate each active bet in the list
        Returns:
        total_win_count
        total_winnings
        """
        bet_win_count = 0
        total_winnings = 0
        for bet in self.active_all_bets_list:
            winnings = bet.evaluate_bet(spin_outcome=spin_outcome)
            if winnings > 0:
                bet_win_count += 1
                total_winnings += winnings
        return bet_win_count, total_winnings
