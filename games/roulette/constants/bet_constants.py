"""
Module contents:

BET PARAMETERS GENERIC TO ALL WHEELS:
1) The BetTypeIds, these are used to map each bet to a specific key in a wheel agnostic fashion;
2) Inside/OutsideBetTypePrompts, these are used to categorise bets into inside/outside bets, and also to create a
command line prompt telling the user which key to press to access each bet;

BET PARAMETERS (WHICH CAN BE) SPECIFIC TO EACH WHEEL:
3) The parameters of each inside/outside bet, as instances of the RouletteBetParameters dataclass;
4) WheelDefaultBetOptionsAndParameters, the dataclass used to store all the default bet options and bet parameters on
every roulette wheel by default
5) WheelBetParameters,a dataclass specifying which bet parameters apply to which wheels (by default all wheels are
given the default bet parameters)
6) Other lower level enums for specific bets

Note that this data structure gives the flexibility define wheel specific bet parameters, (although currently only
default values are used).
To create bet parameters unique to a given wheel:
- Crete new instances of the RouletteBetParameters dataclass for the bets that have wheel specific parameters
- Create an instance of WheelDefaultBetOptionsAndParameters and specify non-default parameters for each bet as relevant
To restrict which bets can be placed on a given wheel:
- Create an instance of WheelBetParameters and specify the bets that should not be included as None
"""

# Standard library imports
from dataclasses import dataclass, fields, Field
from enum import Enum
from typing import Tuple

# Local application imports
from games.roulette.app.roulette_bet_base_class import RouletteBetParameters


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
    SPLIT_BET = "P"
    HIGH_LOW_BET = "H"
    ODDS_EVENS_BET = "O"
    CORNERS_BET = "N"


class OutsideBetTypePrompts(str, Enum):
    """
    Class specifying the user prompt (that corresponds to the ID) of each bet type.
    Used so that the globally defined ID always corresponds to an appropriate command line prompt
    """
    COLOURS_BET = "[C]-Colours"
    HIGH_LOW_BET = "[H] - High / Low"
    ODDS_EVENS_BET = "[O] - Odds / Evens"


class InsideBetTypePrompts(str, Enum):
    """
    Class specifying the user prompt (that corresponds to the ID) of each bet type.
    Used so that the globally defined ID always corresponds to an appropriate command line prompt
    """
    STRAIGHTUP_BET = "[S]-Straight Up"
    SPLIT_BET = "[P]-Split"
    CORNERS_BET = "[N] - Corners"


##########
# WHEEL SPECIFIC parameters of each bet
# Note that currently only 'defaults' are defined which are then used for each wheel
##########

# Outside bets

default_colours_bet_parameters = RouletteBetParameters(bet_type_name=BetTypeIds.COLOURS_BET.name,
                                                       min_bet=5,
                                                       max_bet=50)
default_high_low_bet_parameters = RouletteBetParameters(bet_type_name=BetTypeIds.HIGH_LOW_BET.name,
                                                        min_bet=5,
                                                        max_bet=50)
default_odds_evens_parameters = RouletteBetParameters(bet_type_name=BetTypeIds.ODDS_EVENS_BET.name,
                                                      min_bet=5,
                                                      max_bet=50)

# Inside bets

default_straight_up_bet_parameters = RouletteBetParameters(bet_type_name=BetTypeIds.STRAIGHTUP_BET.name,
                                                           min_bet=2,
                                                           max_bet=20)
default_split_bet_parameters = RouletteBetParameters(bet_type_name=BetTypeIds.SPLIT_BET.name,
                                                     min_bet=2,
                                                     max_bet=20)
default_corners_bet_parameters = RouletteBetParameters(bet_type_name=BetTypeIds.CORNERS_BET.name,
                                                       min_bet=2,
                                                       max_bet=20)


# Mapping of bet options to specific wheels

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
    SPLIT_BET: RouletteBetParameters = default_split_bet_parameters
    HIGH_LOW_BET: RouletteBetParameters = default_high_low_bet_parameters
    ODDS_EVENS_BET: RouletteBetParameters = default_odds_evens_parameters
    CORNERS_BET: RouletteBetParameters = default_corners_bet_parameters

    # new bet goes here as a class attribute

    def construct_wheel_bet_options_prompt(self) -> str:
        """
        Method to construct a command line prompt specific to the wheel, of the bet type options on that wheel
        Returns: string prompt.
        """
        """
        Method to construct a command line prompt specific to the wheel, of the bet type options on that wheel
        Returns: string prompt.
        """
        bet_types_tuple: Tuple[Field, ...] = fields(self.__class__)
        inside_bet_options_prompt: str = ""
        outside_bet_options_prompt: str = ""
        for bet_type in bet_types_tuple:
            if bet_type is None:
                # This bet is not defined for the given wheel
                continue
            if hasattr(OutsideBetTypePrompts, bet_type.name):
                individual_bet_type_prompt = getattr(OutsideBetTypePrompts, bet_type.name).value
                outside_bet_options_prompt += individual_bet_type_prompt + ", "
            elif hasattr(InsideBetTypePrompts, bet_type.name):
                individual_bet_type_prompt = getattr(InsideBetTypePrompts, bet_type.name).value
                inside_bet_options_prompt += individual_bet_type_prompt + ", "
            else:
                raise ValueError("WheelDefaultBetOptionsAndParameters was given a bet that has not been categorised"
                                 "as either an inside or outside bet, per the Enums Inside/OutsideBetType Options")
        bet_options_prompt = "Outside: " + outside_bet_options_prompt[:-2] + "\n" + \
                             "Inside: " + inside_bet_options_prompt[:-2]
        return bet_options_prompt


##########
# Data class storing all bet parameters for all wheels
##########
@dataclass
class WheelBetParameters:
    EURO_WHEEL = WheelDefaultBetOptionsAndParameters()
    AMERICAN_WHEEL = WheelDefaultBetOptionsAndParameters()
    NEW_WHEEL = None


##########
# Individual bet specific Enums - maybe this is a bit overkill...
##########
class HighLowBetOptions(Enum):
    HIGH = "H"
    LOW = "L"
    PROMPT = "[H] - High, [L] - Low"


class OddsEvensBetOptions(Enum):
    ODDS = "O"
    EVENS = "E"
    PROMPT = "[O] - Odds, [E] - Evens"
