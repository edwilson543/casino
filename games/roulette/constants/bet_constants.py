"""
Module for defining the parameters of each bet
The module is split into global parameters and wheel specific parameters.
Flexibility is there to define wheel specific parameters, but currently only default values are used.
"""
from games.roulette.app.roulette_bet_base_class import RouletteBetParameters
from enum import Enum
from dataclasses import dataclass, fields, Field
from typing import Tuple


#  todo is there a way to avoid repeatedly writing "COLOURS_BET" in enum NAMES/ dataclass Fields?
##########
# GLOBAL parameters of each bet type - bet_type_name, id and command line prompts
##########
class BetTypeIds(str, Enum):
    """
    Class specifying the bet_type_name and ID of each bet type
    Note this class is used to define the bet_type_name of indivudal bets (using .bet_type_name)
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


default_colours_bet = RouletteBetParameters(bet_type_name=BetTypeIds.COLOURS_BET.name, min_bet=5, max_bet=50)
default_straight_up_bet = RouletteBetParameters(bet_type_name=BetTypeIds.STRAIGHTUP_BET.name, min_bet=2, max_bet=20)

default_new_bet = RouletteBetParameters(bet_type_name=BetTypeIds.NEW_BET.name, min_bet=0, max_bet=0)


@dataclass(frozen=True)
class IndividualWheeBetParameters:
    COLOURS_BET: RouletteBetParameters = default_colours_bet
    STRAIGHTUP_BET: RouletteBetParameters = default_straight_up_bet
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


default_wheel_bet_parameters = IndividualWheeBetParameters()

@dataclass
class WheelBetParameters:
    EURO_WHEEL = default_wheel_bet_parameters
    AMERICAN_WHEEL = default_wheel_bet_parameters
    NEW_WHEEL = None
