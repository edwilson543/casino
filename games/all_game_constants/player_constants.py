"""Module to specify restrictions on the definition of player-defined player parameters"""

# Local application imports
from dataclasses import dataclass


@dataclass(frozen=True)
class PasswordParameters:
    allowed_password_attempts = 5
    minimum_length = 5


@dataclass(frozen=True)
class UsernameParameters:
    disallowed_characters = [" ", "!", ".", "/"]
    minimum_length = 5


@dataclass(frozen=True)
class NameParameters:
    disallowed_characters = ["!", ".", "/"]


@dataclass(frozen=True)
class PlayerParameterRestrictions:
    password_parameters = PasswordParameters
    username_parameters = UsernameParameters
    name_parameters = NameParameters
