"""
Module for defining the parameters of each bet
The module is split into global parameters and wheel specific parameters.
Flexibility is there to define wheel specific parameters, but currently only default values are used.
"""
from games.roulette.app.roulette_bet_base_class import RouletteBetParameters
from enum import Enum
from dataclasses import dataclass, fields, Field
from typing import Tuple


##########
# GLOBAL parameters of each bet type - bet_type_name, id and command line prompts
##########
class BetTypeIds(str, Enum):
    """
    Class specifying the bet_type_name (the key) and ID of each bet type.
    Class is used to 1) store all bet names, and 2) look up a bet name from the ID
    """
    COLOURS_BET = "C"
    STRAIGHTUP_BET = "S"
    NEW_BET = None


class BetTypePrompts(str, Enum):
    """
    Class specifying the user prompt (that corresponds to the ID) of each bet type.
    Used so that the globally defined ID always corresponds to an appropriate command line prompt
    """
    COLOURS_BET = "[C]olours"
    STRAIGHTUP_BET = "[S]traight up"
    NEW_BET = None  # Dummy new bet prompt


#  In the future may also want a mapping of each bet to inside/outside to allow navigational hierarchy
##########
# WHEEL SPECIFIC parameters of each bet
# Note that currently only 'defaults' are defined which are then used for each wheel
##########

default_colours_bet_parameters = RouletteBetParameters(bet_type_name=BetTypeIds.COLOURS_BET.name, min_bet=5, max_bet=50)
default_straight_up_bet_parameters = RouletteBetParameters(bet_type_name=BetTypeIds.STRAIGHTUP_BET.name, min_bet=2,
                                                           max_bet=20)

default_new_bet_parameters = RouletteBetParameters(bet_type_name=BetTypeIds.NEW_BET.name, min_bet=0, max_bet=0)


@dataclass(frozen=True)
class WheelDefaultBetOptionsAndParameters:
    """
    Data class has 2 functions:
    1) To list the bet OPTIONS on each specific wheel
    2) To store the bet PARAMETERS specific to each wheel
    To restrict bets options or vary parameters on certain wheels, create a new data class with different default values
    """
    COLOURS_BET: RouletteBetParameters = default_colours_bet_parameters
    STRAIGHTUP_BET: RouletteBetParameters = default_straight_up_bet_parameters

    # new bet goes here as a class attribute

    def construct_wheel_bet_options_prompt(self) -> str:
        """
        Method to construct a command line prompt specific to the wheel, of the bet type options on that wheel
        e.g. return: [C]olours, [S]traight up
        """
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


@dataclass
class WheelBetParameters:
    EURO_WHEEL = WheelDefaultBetOptionsAndParameters()
    AMERICAN_WHEEL = WheelDefaultBetOptionsAndParameters()
    NEW_WHEEL = None
