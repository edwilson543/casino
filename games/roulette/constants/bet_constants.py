"""
Module for defining and storing the parameters of each bet, specific to each wheel.
The module is split into global parameters and wheel specific parameters.
Flexibility is there to define wheel specific parameters, but currently only default values are used.

At the bottom, there is also a list of individual bet-specific enums (e.g. for high/low and odds/evens bets)
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
    SPLIT_BET = "P"
    HIGH_LOW_BET = "H"
    ODDS_EVENS_BET = "O"
    CORNERS_BET = "N"


class BetTypePrompts(str, Enum):
    """
    Class specifying the user prompt (that corresponds to the ID) of each bet type.
    Used so that the globally defined ID always corresponds to an appropriate command line prompt
    """
    COLOURS_BET = "[C]-Colours"
    STRAIGHTUP_BET = "[S]-Straight Up"
    SPLIT_BET = "[P]-Split"
    HIGH_LOW_BET = "[H] - High / Low"
    ODDS_EVENS_BET = "[O] - Odds / Evens"
    CORNERS_BET = "[N] - Corners"


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


#  In the future may also want a mapping of each bet to inside/outside to allow navigational hierarchy
##########
# WHEEL SPECIFIC parameters of each bet
# Note that currently only 'defaults' are defined which are then used for each wheel
##########
##########
# Outside bets
##########
default_colours_bet_parameters = RouletteBetParameters(bet_type_name=BetTypeIds.COLOURS_BET.name,
                                                       min_bet=5,
                                                       max_bet=50)
default_high_low_bet_parameters = RouletteBetParameters(bet_type_name=BetTypeIds.HIGH_LOW_BET.name,
                                                        min_bet=5,
                                                        max_bet=50)
default_odds_evens_parameters = RouletteBetParameters(bet_type_name=BetTypeIds.ODDS_EVENS_BET.name,
                                                      min_bet=5,
                                                      max_bet=50)
##########
# Inside bets
##########
default_straight_up_bet_parameters = RouletteBetParameters(bet_type_name=BetTypeIds.STRAIGHTUP_BET.name,
                                                           min_bet=2,
                                                           max_bet=20)
default_split_bet_parameters = RouletteBetParameters(bet_type_name=BetTypeIds.SPLIT_BET.name,
                                                     min_bet=2,
                                                     max_bet=20)
default_corners_bet_parameters = RouletteBetParameters(bet_type_name=BetTypeIds.CORNERS_BET.name,
                                                       min_bet=2,
                                                       max_bet=20)


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
