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

    def get_profit_report(self):
        print(f"Your current pot is £{self.active_pot}.\n"
              f"Since {str(self.initial_pot_datetime)}, you have {self.won_or_lost()}:"
              f"{abs(self.active_pot - self.initial_pot)}")

    def won_or_lost(self):
        if self.initial_pot > self.active_pot:
            return "lost"
        else:
            return "won"
