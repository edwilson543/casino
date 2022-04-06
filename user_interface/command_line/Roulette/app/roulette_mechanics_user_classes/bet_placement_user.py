from Games.Roulette.definitions.wheel_defns import wheel_options
from Games.Roulette.definitions.bet_type_defns import bet_type_options

from Games.Roulette.app.roulette_mechanics_action_classes.bet_placement import BetPlacement


class BetPlacementUser(BetPlacement):
    def __init__(self, bet_type_id: str, wheel_id: str, stake: int):
        super().__init__(bet_type_id, wheel_id, stake)
        self.bet_type = bet_type_options_user[self.bet_type_id]

    def get_user_bet_choice(self):
        return self.bet_type.get_user_bet_choice(self)
