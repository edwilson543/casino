from Games.Roulette.app.game_setup.roulette_mechanics import RouletteWheelWagers
from Games.Roulette.definitions.wheel_defns import wheel_options

test_bet_placer_colours = RouletteWheelWagers(bet_type_id = 'C', wheel_id='E', stake=10)

class TestRouletteWheelWagers:
    def test_get_winning_slots_colours(self, ['red']):
        assert False
