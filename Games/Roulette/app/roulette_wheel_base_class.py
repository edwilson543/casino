import numpy as np


class RouletteWheel:
    """Base class for the roulette wheel - from which we can define different wheel configurations"""

    def __init__(self,
                 slots: dict,
                 bias_colour: str,
                 colour_ids: dict,
                 colour_options: str):
        """
        Parameters
        __________
        slots: slot of the roulette wheel -
        should be passed as a dictionary, with the numbers as keys and the colours as the values
        colour_ids: a mapping of colour id (e.g. 'R') to each colour (e.g. 'red')
        colour_options: a string used to get user input on what colour they'd like to bet on
        bias_colour: the colour whose counts are ignored when calculating stake returns. e.g. if you have a 37 slot
        wheel and one slot is green, then stakes are calculated from probabilities as 1/(x/36).
        """
        self.slots = slots
        self.colour_ids = colour_ids
        self.colour_options = colour_options
        self.bias_colour = bias_colour

    def spin(self):
        """Returns: One random spin of the wheel as a dictionary, with number and colour as the key/value pairs"""
        min_slot = min(self.slots.keys())
        max_slot = max(self.slots.keys())
        number_return = np.random.randint(low=min_slot, high=max_slot + 1)
        # note the randint interval is half-open hence need of the + 1
        colour_return = self.slots[number_return]
        return number_return, colour_return

    def bias_wheel_size(self) -> int:
        """
        Returns: The number of slots on the wheel, minus a count of the number of slots of biased colours.
        The purpose is so that when calculating the return for a bet, the bias wheel size is used to calculate the
        probability of winning so that the house always wins."""
        return self.wheel_size() - self.colour_counts(colour=self.bias_colour)

    def colour_counts(self, colour: str) -> int:
        """Returns: the number of slots on the wheel of the specified colour"""
        return sum(map(colour.__eq__, self.slots.values()))

    def wheel_size(self) -> int:
        """Returns: The number of slots on the wheel as an int, for calculating probabilities within wager defns"""
        return len(self.slots)

    # UI methods - will need to be moved elsewhere

    def user_number_options_text(self):
        """
        Returns: text string describing the numbers of the roulette wheel
        Example output form: '0 to 36 (inclusive)'
        Note this would need to change if defining a roulette wheel which skips numbers
        """
        min_number = min(list(set(self.slots.keys())))
        max_number = max(list(set(self.slots.keys())))
        return f"{min_number} to {max_number} (inclusive)"

    def user_number_options_range(self):
        """Returns a range which specifies the valid number choices"""
        min_number = min(list(set(self.slots.keys())))
        max_number = max(list(set(self.slots.keys())))
        return range(min_number, max_number + 1)
