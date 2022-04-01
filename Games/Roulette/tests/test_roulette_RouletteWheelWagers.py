from Games.Roulette.app.roulette_mechanics_classes.roulette_continuation import RouletteWheelWagers

test_bet_placer_colours = RouletteWheelWagers(bet_type_id='C', wheel_id='E', stake=10)


class TestRouletteWheelWagers:
    def test_get_winning_slots_colours(self):
        winning_set = test_bet_placer_colours.get_winning_slots_colours(player_bet=['R'])  # test for colour red
        assert winning_set == [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
