from datetime import datetime


class Player:
    """Class to hold the pot and define interactions with the pot.
    Player has money taken from the pot, and added to the pot"""

    def __init__(self,
                 name: str,
                 password: str,
                 initial_pot: int,
                 initial_pot_datetime: datetime,
                 active_pot: int):
        self.name = name
        self.password = password
        self.initial_pot = initial_pot
        self.initial_pot_datetime = initial_pot_datetime
        self.active_pot = active_pot

    def set_initial_pot(self, amount: int):
        self.initial_pot = amount
        self.active_pot = amount

    def add_to_pot(self, amount: int):
        self.active_pot += amount

    def take_from_pot(self, amount: int):
        self.active_pot -= amount

    # more UI focused - probably to go into the UI

    def get_profit_report(self):
        print(f"Your current pot is £{self.active_pot}.\n"
              f"Since {str(self.initial_pot_datetime)}, you have {self.won_or_lost()}:"
              f"{abs(self.active_pot - self.initial_pot)}")

    def won_or_lost(self):
        if self.initial_pot > self.active_pot:
            return "lost"
        else:
            return "won"


# TODO maybe we do / don't want payout and win criteria (and stake) as attributes here
class Bet:
    def __init__(self, payout: int,
                 win_criteria: list,
                 min_bet: int,
                 max_bet: int):
        self.payout = payout
        self.win_criteria = win_criteria
        self.min_bet = min_bet
        self.max_bet = max_bet

    def calculate_payout(self):
        """Abstract method for calculating the payout for a £1 bet - will be game specific"""
        pass

    def determine_win_criteria(self):
        """Abstract method for calculating the win crtieria of a given bet - will be game and bet specific"""
        pass
