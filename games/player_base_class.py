"""
Contents:
Player (base class)
Bet (base class)
"""
from datetime import datetime
from sys import exit


class Player:
    """Class to hold the pot and define interactions with the pot.
    Player has money taken from the pot, and added to the pot"""

    # TODO add an attribute along the lines of 'last login time'
    # and when the player starts the game, update it to datetime.now()
    def __init__(self,
                 player_type: str,  # restrict to 'E', 'G', 'N'
                 name: str,
                 username: str,
                 password: str,
                 initial_pot: int,
                 initial_pot_datetime: datetime,
                 active_pot: int,
                 last_top_up_datetime: datetime,
                 active_session_initial_pot: int = None,
                 active_session_start_time: datetime = None,
                 active_session_top_ups: int = 0,
                 all_in_status: bool = False):
        self.player_type = player_type
        self.name = name
        self.username = username
        self.password = password
        self.initial_pot = initial_pot
        self.initial_pot_datetime = initial_pot_datetime
        self.active_pot = active_pot
        self.last_top_up_datetime = last_top_up_datetime
        self.active_session_initial_pot = active_session_initial_pot
        self.active_session_start_time = active_session_start_time
        self.active_session_top_ups = active_session_top_ups
        self.all_in_status = all_in_status

    ##########
    # Setter methods
    ##########
    def set_initial_pot(self, amount: int):
        self.initial_pot = amount
        self.active_pot = amount
        self.initial_pot_datetime = datetime.now()

    def add_top_up_to_pot(self, amount: int):
        self.active_pot += amount
        self.active_session_top_ups += amount
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

    def set_active_session_initial_pot_and_time(self):
        self.active_session_initial_pot = self.active_pot
        self.active_session_start_time = datetime.now()

    def set_all_in_status(self, true_or_false: bool):
        self.all_in_status = true_or_false

    ##########
    # Calculation methods
    ##########

    def calculate_active_session_duration_minutes(self) -> int:
        duration_timedelta = datetime.now() - self.active_session_start_time
        duration_seconds = duration_timedelta.seconds
        duration_minutes = duration_seconds / 60
        return int(round(duration_minutes, 0))

    def calculate_active_session_winnings(self) -> int:
        if self.player_type == 'E':
            return self.active_pot - self.active_session_initial_pot - self.active_session_top_ups
        elif self.player_type in ['G', 'N']:
            return self.active_pot - self.active_session_initial_pot - \
                   self.active_session_top_ups - self.initial_pot

    ##########
    # more UI focused - could separate into UI at some point
    ##########

    def get_active_session_report(self):
        print(f"Your current pot is £{self.active_pot}.\n"
              f"You have been playing for {self.calculate_active_session_duration_minutes()} minute(s), "
              f"during which time you have {self.won_or_lost()}: "
              f"£{abs(self.calculate_active_session_winnings())}.")

    def end_session(self):
        print(f"Thanks for playing {self.name}!\n"
              f"Your final pot is £{self.active_pot}.")
        exit()

    # lower level UI methods

    def won_or_lost(self):
        if self.calculate_active_session_winnings() > 0:
            return "won"
        else:
            return "lost"
