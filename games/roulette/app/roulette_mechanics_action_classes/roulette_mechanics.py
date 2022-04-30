from games.player_base_class import PLAYER_TYPES
from games.roulette.app.roulette_wheel_base_class import wheel_spin_return
from games.roulette.app.roulette_wheel_base_class import WHEEL_TYPES
from games.roulette.app.roulette_mechanics_action_classes.wheel_and_bet_type_selection import \
    WheelBoardBetConstructor


class RouletteGame:
    def __init__(self,
                 active_player: PLAYER_TYPES = None,
                 active_wheel: WHEEL_TYPES = None,
                 active_board=None,  # TODO implement this
                 constructor=WheelBoardBetConstructor(),
                 active_all_bets_list: list = None,
                 active_spin_outcome: wheel_spin_return = None,
                 active_bet_win_count: int = 0,
                 active_total_winnings: int = 0):
        self.active_player = active_player
        self.active_wheel = active_wheel
        self.active_board = active_board
        self.constructor = constructor
        self.active_all_bets_list = active_all_bets_list
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
