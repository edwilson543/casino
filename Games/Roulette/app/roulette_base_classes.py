import numpy as np


class RouletteWheel:
    """
    Base class for the roulette wheel - from which we can define different wheel configurations
    """

    def __init__(self,
                 slots: dict,
                 payout_scaler: float):
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

    def spin(self):
        """Returns: One random spin of the wheel as a dictionary, with number and colour as the key/value pairs"""
        number_return = np.random.randint(low=0, high=len(self.slots))
        # note the randint interval is half-open so wheel size itself will never be selected (which would be invalid)
        colour_return = list(self.slots.values())[number_return]
        return {"number_return": number_return, "colour_return": colour_return}

    def wheel_size(self) -> int:
        """Returns: The number of slots on the wheel as a float, for calculating probabilities within wager defns"""
        return len(self.slots)

    def colour_counts(self, colour: str) -> int:
        """Returns: the number of slots on the wheel of the specified colour"""
        return sum(map(colour.__eq__, self.slots.values()))

    def generate_colour_ids(self):

        """
        Method to identify user colour selection based on their input.
        Returns: a dictionary in the form {'R': 'red', 'B': 'black', 'G': green}
        The for loop will normally end after the 1st iteration. It is there to catch the instance where 2 colours start
        with the same letters. The loop keeps going until we have unique IDs.
        Note that there shouldn't be an error of indexing out of range when slicing.
        """
        for i in range(0, 25): #25 assuming no colours have more than 20 letters
            def col_id(colour):
                return colour[i].upper()
            colours = sorted(list(set(self.slots.values())))  # get the unique wheel colours in an alphabetical list
            col_id_list = [col_id(colour) for colour in colours]
            if len(col_id_list) != len(list(set(col_id_list))):
                continue
                # e.g. if [B] is used to identify 2 different colours, try again using [BL]
            return dict(zip(col_id_list, colours))

    def user_colour_options(self):
        """
        Returns: text string the user can use to identify the colour options for betting
        Example output form: '[R]ed, [B]lack, [G]reen'
        Analogous to generate_colour_ids - written separately though - maybe should combine??
        """
        for i in range(0, 25): #25 assuming no colours have more than 20 letters
            def col_str_rep(colour):
                return "[" + colour[i].upper() + "]" + colour[i+1:]
            colours = sorted(list(set(self.slots.values())))  # get the unique wheel colours in an alphabetical list
            str_rep_list = [col_str_rep(colour) for colour in colours]
            if len(str_rep_list) != len(list(set(str_rep_list))):
                continue
                # e.g. if [B] is used to identify 2 different colours, try again using [BL]
            display_str_no_comma = " ".join(str_rep_list).strip()
            return display_str_no_comma.replace(" ", ", ")

    def user_number_list(self):  # to write
        """
        Returns: text string describing the numbers of the roulette wheel
        Example output form: '[0, 36] (inclusive)'
        Note this would need to change if defining a roulette wheel which skips numbers
        """
        min_number = min(list(set(self.slots.keys())))
        max_number = max(list(set(self.slots.keys())))
        return f"[{min_number}, {max_number}] (inclusive)"