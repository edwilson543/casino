from datetime import datetime
from enum import Enum
from typing import TypeVar


class PlayerType(Enum):
    """Existing/guest/new players are treated differently at log-in"""
    EXISTING_PLAYER = "E"
    GUEST_PLAYER = "G"
    NEW_PLAYER = "N"


class Player:
    """Class to hold the pot and define interactions with the pot.
    Player has money taken from the pot, and added to the pot"""

    # TODO add an attribute along the lines of 'last login time'
    # and when the player starts the game, update it to datetime.now()
    def __init__(self,
                 player_type: PlayerType,
                 name: str,
                 username: str,
                 password: str,
                 active_pot: int,
                 last_top_up_datetime: datetime,
                 active_session_initial_pot: int = None,
                 active_session_start_time: datetime = None,
                 active_session_top_ups: int = 0):
        self.player_type = player_type
        self.name = name
        self.username = username
        self.password = password
        self.active_pot = active_pot
        self.last_top_up_datetime = last_top_up_datetime
        self.active_session_initial_pot = active_session_initial_pot
        self.active_session_start_time = active_session_start_time
        self.active_session_top_ups = active_session_top_ups

    ##########
    # Setter methods
    ##########
    def set_active_pot(self, amount: int):
        self.active_pot = amount

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

    ##########
    # Calculation methods
    ##########

    def calculate_active_session_duration_minutes(self) -> int:
        duration_timedelta = datetime.now() - self.active_session_start_time
        duration_seconds = duration_timedelta.seconds
        duration_minutes = duration_seconds / 60
        return int(round(duration_minutes, 0))

    def calculate_active_session_winnings(self) -> int:
        if self.player_type == PlayerType.EXISTING_PLAYER:
            return self.active_pot - self.active_session_initial_pot - self.active_session_top_ups
        elif self.player_type in [PlayerType.EXISTING_PLAYER, PlayerType.GUEST_PLAYER]:
            return self.active_pot - self.active_session_initial_pot - \
                   self.active_session_top_ups


##########
# Type hint to use whenever referencing a player object
##########
PLAYER_TYPES = TypeVar(name="PLAYER_TYPES", bound=Player)
