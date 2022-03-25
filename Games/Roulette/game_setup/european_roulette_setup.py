from data.column_names import euro_wheel_defn_column_names
from data.data_loading_and_processing import get_wheel_defn_dict
from roulette_base_classes import RouletteWheel
from roulette_base_classes import RouletteWager


euro_wheel_defn = get_wheel_defn_dict(filename = 'euro_wheel_defn',
                                      number_column = euro_wheel_defn_column_names['NUMBER'],
                                      colour_column = euro_wheel_defn_column_names['COLOUR'])
euro_wheel = RouletteWheel(slots = euro_wheel_defn)
# maybe the above should be moved somewhere else?

class EuRouletteWheelWager(RouletteWager):
    def __init__(self, stake: float):
        super().__init__(stake)
    """
    Outside bets
    """
    def colours_bet(self, colour: str) -> float:
        """
        Allows users to bet on specific colours
        """
        spin = eu_roulette_wheel.spin()
        if spin['colour_return'] == colour:
            if spin['colour_return'] == 1: #TODO need to specify
                return stake + stake *1
        else:
            return 0


