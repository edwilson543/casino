from Games.Roulette.app.roulette_base_classes import RouletteWheel
from Games.Roulette.definitions.wheel_defns import euro_wheel_defn, euro_wheel_payout_scaler

euro_wheel = RouletteWheel(slots=euro_wheel_defn, payout_scaler=euro_wheel_payout_scaler)


# TODO change this so that we use some test wheel which is defined in the wheel defn.s page

class TestRouletteWheel:
    def test_wheel_size_euro_wheel(self):
        assert euro_wheel.wheel_size() == 37

    def test_wheel_colour_counts_red(self):
        assert euro_wheel.colour_counts(colour = 'red') == 18
