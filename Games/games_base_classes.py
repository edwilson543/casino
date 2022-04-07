from datetime import datetime


class Player:
    """Class to hold the pot and define interactions with the pot.
    Player has money taken from the pot, and added to the pot"""

    def __init__(self,
                 name: str,
                 username: str,
                 password: str,
                 initial_pot: int,
                 initial_pot_datetime: datetime,
                 active_pot: int):
        self.name = name
        self.username = username
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


class Bet:
    def __init__(self,
                 min_bet: int,
                 max_bet: int,
                 bet_type_id: str):
        self.min_bet = min_bet
        self.max_bet = max_bet
        self.bet_type_id = bet_type_id

    def determine_win_criteria(self, *args):
        """Abstract method for calculating the win criteria of a given bet - will be game and bet specific"""
        pass

    def calculate_payout(self, *args):
        """Abstract method for calculating the payout for a £1 bet - will be game and bet specific,
        in particular we will need"""
        pass
