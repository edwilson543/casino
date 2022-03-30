import numpy as np


class RouletteWheel:
    """
    Base class for the roulette wheel - from which we can define different wheel configurations
    """

    def __init__(self,
                 slots: dict,
                 payout_scaler: float,
                 colour_ids: dict,
                 colour_options: str):
        """
        Parameters
        __________
        slots: slot of the roulette wheel -
        should be passed as a dictionary, with the numbers as keys and the colours as the values
        payout_scaler: payout := floor(stake * payout_scaler / P(bet winning)).
        So it's a number <1 assuming house always wins
        """
        self.slots = slots
        self.payout_scaler = payout_scaler
        self.colour_ids = colour_ids
        self.colour_options = colour_options

    def spin(self):
        """Returns: One random spin of the wheel as a dictionary, with number and colour as the key/value pairs"""
        min_slot = min(self.slots.keys())
        max_slot = max(self.slots.keys())
        number_return = np.random.randint(low=min_slot, high=max_slot + 1)
        # note the randint interval is half-open hence need of the + 1
        colour_return = self.slots[number_return]
        return number_return, colour_return

    def wheel_size(self) -> int:
        """Returns: The number of slots on the wheel as a float, for calculating probabilities within wager defns"""
        return len(self.slots)

    def colour_counts(self, colour: str) -> int:
        """Returns: the number of slots on the wheel of the specified colour"""
        return sum(map(colour.__eq__, self.slots.values()))

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
