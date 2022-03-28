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
        payout_scaler: payout := stake * payout_scaler / P(bet winning). So it's a number <1 assuming house always wins
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

    def user_colour_list(self):
        """
        Returns: text string the user can use to identify the colour options for betting
        Example output form: '[R]ed, [B]lack, [G]reen'
        """
        colours = list(set(self.slots.values()))
        options = list(map(lambda col: "[" + col[0].upper() + "]" + col[1:], colours))
        display_str_no_comma = " ".join(options).strip()
        return display_str_no_comma.replace(" ", ", ")


    def user_number_list(self): # to write
        """
        Returns: text string describing the numbers of the roulette wheel
        Example output form: '[0, 36] (inclusive)'
        Note this would need to change if defining a roulette wheel which skips numbers
        """
        min_number = min(list(set(self.slots.keys())))
        max_number = max(list(set(self.slots.keys())))
        return f"[{min_number}, {max_number}] (inclusive)"


class RouletteWheelWagers():
    """
    Base class for defining the different wagers on the roulette wheel.
    Not used in itself, but acts as a template for defining each individual bet.
    """

    def __init__(self, bet_id: str, min_bet: int, max_bet: float):
        self.bet_id = 'GENERIC'
        self.min_bet = 5
        self.max_bet = 50

    def set_stake(self): # unsure if there is any value if defining these here as a template
        pass

    def place_bet(self):
        pass

    def winning_set(self):
        pass

    # """Outside bets - to be expanded"""
    # def colours_bet(self, stake: float, colour: str) -> float:
    #     spin = self.spin()
    #     if spin['colour_return'] == colour:
    #         print(f"Spin outcome: colour: {spin['colour_return']}, number: {spin['number_return']}")
    #         print('you win!')
    #         return stake * self.payout_scaler / (self.colour_counts(colour) / self.wheel_size())
    #     else:
    #         print(f"Spin outcome: colour: {spin['colour_return']}, number: {spin['number_return']}")
    #         print('you lose!')
    #         return 0
    #
    # """Inside bets - to be expanded"""
    # def straight_up(self, stake: float, number: str) -> float:
    #     spin = self.spin()
    #     if spin['number_return'] == number:
    #         print(f"Spin outcome: colour: {spin['colour_return']}, number: {spin['number_return']}")
    #         print('you win!')
    #         return stake * self.payout_scaler * self.wheel_size()
    #     else:
    #         print(f"Spin outcome: colour: {spin['colour_return']}, number: {spin['number_return']}")
    #         print('you lose!')
    #         return 0