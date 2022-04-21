from Games.Roulette.app.roulette_wheel_base_class import RouletteWheel


class RouletteWheelUser(RouletteWheel):
    def __init__(self,
                 wheel_id,
                 slots,
                 bias_colour,
                 colour_ids,
                 colour_options):
        """
        Added instance attributes:
        colour_ids: a mapping of colour id (e.g. 'R') to each colour (e.g. 'red')
        colour_options: a string used to get user input on what colour they'd like to bet on
        """
        super().__init__(wheel_id, slots, bias_colour)
        self.colour_ids = colour_ids
        self.colour_options = colour_options

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
