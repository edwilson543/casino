from datetime import datetime
from enum import Enum
from typing import TypeVar
from dataclasses import dataclass


class PlayerType(Enum):
    """Existing/guest/new players are treated differently at log-in"""
    #  TODO - should be able to get rid of this once new json storage in place
    EXISTING_PLAYER = "E"
    GUEST_PLAYER = "G"
    NEW_PLAYER = "N"


@dataclass
class PlayerData:
    """Data class for storing player parameters"""
    name: str
    username: str
    password: str
    active_pot: int
    total_active_stake: int
    last_top_up_datetime: datetime
    active_session_initial_pot: int
    active_session_start_time: datetime
    active_session_top_ups: int
    last_session_end_time: datetime


class Player:
    """Class to hold the pot and define interactions with the pot.
    Player has money taken from the pot, and added to the pot"""

    def __init__(self,
                 name: str,
                 username: str,
                 password: str,
                 active_pot: int,
                 total_active_stake: int,
                 last_top_up_datetime: datetime,
                 active_session_initial_pot: int = None,
                 active_session_start_time: datetime = None,
                 active_session_top_ups: int = 0,
                 last_session_end_time: datetime = None):
        self.name = name
        self.username = username
        self.password = password
        self.active_pot = active_pot
        self.total_active_stake = total_active_stake
        self.last_top_up_datetime = last_top_up_datetime
        self.active_session_initial_pot = active_session_initial_pot
        self.active_session_start_time = active_session_start_time
        self.active_session_top_ups = active_session_top_ups
        self.last_session_end_time = last_session_end_time

    ##########
    # Special methods
    ##########
    def __eq__(self, other):
        if isinstance(other, type(self)):
            validity = True
            self_dict = self.__dict__
            other_dict = other.__dict__
            for key, attribute_value in self_dict.items():
                attribute_comparison = attribute_value == other_dict[key]
                validity *= attribute_comparison
                return validity
        else:
            raise TypeError(f"{other} is not of tpye {type(self)}")

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

    def reset_total_active_stake(self):
        self.total_active_stake = 0

    def set_session_end_time_to_now(self):
        self.last_session_end_time = datetime.now()  # Called when a player logs out

    ##########
    # Calculation methods
    ##########

    def calculate_active_session_winnings(self) -> int:
        winnings = self.active_pot - self.active_session_initial_pot - self.active_session_top_ups
        return winnings

    def calculate_active_session_duration_minutes(self) -> int:
        duration_timedelta = datetime.now() - self.active_session_start_time
        duration_seconds = duration_timedelta.seconds
        duration_minutes = duration_seconds / 60
        return int(round(duration_minutes, 0))

    def calculate_last_login_time_minutes(self):
        duration_timedelta = datetime.now() - self.last_session_end_time
        duration_seconds = duration_timedelta.seconds
        duration_minutes = duration_seconds / 60
        return int(round(duration_minutes, 0))


##########
# Type hint to use whenever referencing a player object
##########
PLAYER_TYPES = TypeVar(name="PLAYER_TYPES", bound=Player)
