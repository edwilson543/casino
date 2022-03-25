import numpy as np


class RouletteWheel:
    """
    Base class for the roulette wheel - from which we can define different wheel configurations
    """
    def __init__(self, slots):
        """
        Parameters
        __________
        slots: slot of the roulette wheel -
        should be passed as a dictionary, with the numbers as keys and the colours as the values
        """
        self.slots = slots

    def spin(self):
        """
        Returns
        --------
        A One random spin of the wheel as a dictionary
        """
        number_return = np.random.randint(low=0, high=len(self.slots))
        # note the randint interval is half-open so wheel size itself will never be selected (which would be invalid)
        colour_return = list(self.slots.values())[number_return]
        return {"number_return": number_return, "colour_return": colour_return}

class RouletteWager:
    "Base class for different wagers on the roulette wheel"
    def __init__(self, stake: float):
        self.stake = stake


