from user_interface.command_line.Roulette.app.roulette_mechanics_user_classes.bet_placement_user import BetPlacementUser
from Games.Roulette.definitions.wheel_defns import EuroWheel


bet_placer = BetPlacementUser(bet_type_id='C', stake=10, playing_wheel=EuroWheel())


class TestBetPlacementUser:
    def test_get_user_bet_choice(self):
        # requires user input - how do we test this non-manually
        pass
