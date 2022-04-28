"""
Module for defining the parameters of each bet
The module is split into global parameters and wheel specific parameters.
Flexibility is there to define wheel specific parameters, but currently only default values are used.
"""

from enum import Enum
from dataclasses import dataclass, fields, Field
from typing import Tuple


##########
# GLOBAL parameters of each bet type - name, id and command line prompts
##########
class BetTypeIds(str, Enum):
    """
    Class specifying the name and ID of each bet type
    Note this class is used to define the name of indivudal bets (using .name)
    And is then used by named bets to look up their own ID.
    """
    COLOURS_BET = "C"
    STRAIGHTUP_BET = "S"
    NEW_BET = None


class BetTypePrompts(str, Enum):
    """
    Class specifying the user prompt (that corresponds to the ID) of each bet type (UI focused)
    Note this class is used so that the globally defined ID always corresponds to an appropriate command line prompt
    """
    COLOURS_BET = "[C]olours"
    STRAIGHTUP_BET = "[S]traight up"
    NEW_BET = None  # Dummy new bet prompt


@dataclass(frozen=True)
class MinMaxBetParameters:
    """Class to specify the min/max bet parameters of a given bet.
    To define some wheel specific parameters, define a new instance of the class for that bet"""
    min_bet: int
    max_bet: int


default_colours_bet = MinMaxBetParameters(min_bet=5, max_bet=50)
default_straight_up_bet = MinMaxBetParameters(min_bet=2, max_bet=20)

default_new_bet = MinMaxBetParameters(min_bet=0, max_bet=0)


@dataclass(frozen=True)
class IndividualWheelMinMaxBetParameters:
    COLOURS_BET: MinMaxBetParameters = default_colours_bet
    STRAIGHTUP_BET: MinMaxBetParameters = default_straight_up_bet

    # new bet goes here but will raise an error if included in the prompt

    def get_wheel_bet_type_ids(self) -> list[str]:
        """Method to return a list of bet types valid on the wheel (listed by their IDs)"""
        bet_types_tuple = fields(self.__class__)  # creates a tuple of the data class fields
        bet_type_ids_list = []
        for bet_type in bet_types_tuple:
            bet_type_id = getattr(BetTypeIds, bet_type.name).value
            bet_type_ids_list.append(bet_type_id)
        return bet_type_ids_list

    def construct_wheel_bet_options_prompt(self) -> str:
        """Method to construct a command line prompt specific to the wheel, of the bet type options on that wheel"""
        bet_types_tuple: Tuple[Field, ...] = fields(self.__class__)  # creates a tuple of the data class fields
        number_of_bet_options: int = len(bet_types_tuple)
        bet_type_options_prompt: str = ""
        for n in range(number_of_bet_options):
            bet_type = bet_types_tuple[n]
            individual_bet_type_prompt = getattr(BetTypePrompts, bet_type.name).value
            if n < number_of_bet_options - 1:  # i.e. if this isn't the last element of the tuple:
                bet_type_options_prompt += individual_bet_type_prompt + ", "
            else:
                bet_type_options_prompt += individual_bet_type_prompt
        return bet_type_options_prompt


default_wheel_min_max_bet_data = IndividualWheelMinMaxBetParameters()


@dataclass(frozen=True)
class WheelMinMaxBetParameters:
    EUROWHEEL = default_wheel_min_max_bet_data
    AMERICANWHEEL = default_wheel_min_max_bet_data
    NEW_WHEEL = None

print(default_wheel_min_max_bet_data)
print(default_wheel_min_max_bet_data.construct_wheel_bet_options_prompt())
