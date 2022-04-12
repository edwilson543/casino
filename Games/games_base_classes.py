from datetime import datetime


class Player:
    """Class to hold the pot and define interactions with the pot.
    Player has money taken from the pot, and added to the pot"""

    # TODO add an attribute along the lines of 'last played time'
    # and when the player starts the game, update it to datetime.now()
    # then add a method in_game_profit_report, to be used at game continuation
    def __init__(self,
                 player_type: str,  # restrict to 'E', 'G', 'N'
                 name: str,
                 username: str,
                 password: str,
                 initial_pot: int,
                 initial_pot_datetime: datetime,
                 active_pot: int,
                 last_top_up_datetime: datetime):
        self.player_type = player_type
        self.name = name
        self.username = username
        self.password = password
        self.initial_pot = initial_pot
        self.initial_pot_datetime = initial_pot_datetime
        self.active_pot = active_pot
        self.last_top_up_datetime = last_top_up_datetime

    def set_initial_pot(self, amount: int):
        self.initial_pot = amount
        self.active_pot = amount
        self.initial_pot_datetime = datetime.now()

    def add_top_up_to_pot(self, amount: int):
        self.active_pot += amount
        self.last_top_up_datetime = datetime.now()

    def add_winnings_to_pot(self, amount: int):
        self.active_pot += amount

    def take_stake_from_pot(self, amount: int):
        self.active_pot -= amount

    def set_name(self, name: str):
        self.name = name

    def set_username(self, username: str):
        self.username = username

    def set_password(self, password: str):
        if len(password) >= 5:
            self.password = password
        else:
            raise ValueError("Password attempted to be set at insufficient length")

    # more UI focused - could go into the UI somehow

    def get_full_status_report(self):
        print(f"You are playing as: {self.name}.\n"
              f"Your current pot is £{self.active_pot}.\n"
              f"You last topped up at {self.last_top_up_datetime}.\n"
              f"Since {str(self.initial_pot_datetime)}, you have {self.won_or_lost()}:"
              f"£{abs(self.active_pot - self.initial_pot)}")

    def get_profit_report(self):
        print(f"Your current pot is £{self.active_pot}.\n"
              f"Since {str(self.initial_pot_datetime)}, you have {self.won_or_lost()}:"
              f"£{abs(self.active_pot - self.initial_pot)}.")

    # lower level UI methods

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

    def determine_win_criteria(self, *args, **kwargs):
        """Abstract method for calculating the win criteria of a given bet - will be game and bet specific"""
        pass

    def calculate_payout(self, *args, **kwargs):
        """Abstract method for calculating the payout for a £1 bet - will be game and bet specific,
        in particular we will need"""
        pass
