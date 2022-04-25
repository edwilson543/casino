from user_interface.command_line.roulette.app.roulette_mechanics_user_classes.bet_placement_evaluation_user import BetPlacementEvaluationUser
from games.roulette.definitions.wheel_defns import EuroWheel


bet_placer = BetPlacementEvaluationUser(bet_type_id='C', stake=10, playing_wheel=EuroWheel())


class TestBetPlacementUser:
    def test_get_user_bet_choice(self):
        # requires user input - how do we test this non-manually
        pass
