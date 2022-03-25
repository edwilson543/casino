from Games.Roulette.app.roulette_base_classes import RouletteWager
from Games.Roulette.app.roulette_base_classes import RouletteWheel
from Games.Roulette.constants.wheel_defns import euro_wheel_defn

euro_wheel = RouletteWheel(euro_wheel_defn)


class EuWheelWager(RouletteWager):
    def __init__(self, stake: float):
        super().__init__(stake)

    """
    Outside bets
    """

    def colours_bet(self, colour: str) -> float:
        """
        Allows users to bet on specific colours
        """
        spin = euro_wheel.spin()
        if spin['colour_return'] == colour:
            if spin['colour_return'] == 1:  # TODO need to specify
                return self.stake + self.stake * 1
        else:
            return 0