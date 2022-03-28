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
        pass

    def user_number_list(self):
        pass


class RouletteWheelWagers(RouletteWheel):
    """
    Base class for defining the different wagers on the roulette wheel.
    Not actually sure if it counts as a base class given its a subclass.
    """

    def __init__(self,
                 slots: dict,
                 payout_scaler: float,
                 min_bet: int,
                 max_bet: float):
        super().__init__(slots, payout_scaler)

    def set_stake(self):
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