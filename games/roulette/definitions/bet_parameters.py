"""
Module for defining the parameters of each bet
The module is split into global parameters and wheel specific parameters.
Flexibility is there to define wheel specific parameters, but currently only default values are used.
"""

from enum import Enum
from dataclasses import dataclass

##########
# GLOBAL parameters of each bet type
##########
class BetTypeIds(str, Enum):
    """
    Class specifying the ID of each bet type
    Note this class is used by individual bets to look up their own ID.
    """
    COLOURSBET = "C"
    STRAIGHTUPBET = "S"
    NEWBET = None

# default_colours_bet = RouletteBetData(XYZ) - defined using BetTypeIds
# default_straight_up = StraightUpBetData(XYZ) - defined using BetTypeIds

# @dataclass
# WheelBetData:
#   COLOURSBET = colours_bet
#   STRAIGHTUPBET = straight_up_bet

# default_wheel_bet_data = RouletteBetData(COLOURSBET=colours_bet)

# @dataclass
# class WheelBetParameters:
#   EUROWHEEL = default_wheel_bet_data
#   AMERICANWHEEL = default_wheel_bet_data



@dataclass()
class RouletteBetData:
     bet_type: str
     bet_type_id: str
     min_bet: int
     max_bet: int
     prompt: str


class BetTypeNames(str, Enum):
    """
    Class specifying the name of each bet type
    Note this class is used by individual bets to look up their own name.
    """
    COLOURSBET = "COLOURSBET"
    STRAIGHTUPBET = "STRAIGHTUPBET"
    NEWBET = None


class BetTypePrompts(str, Enum):
    """
    Class specifying the user prompt (that corresponds to the ID) of each bet type (UI focused)
    Note this class is used so that the globally defined ID always corresponds to an appropriate command line prompt
    """
    COLOURSBET = "[C]olours"
    STRAIGHTUPBET = "[S]traight up"
    NEWBET = None  # Dummy new bet prompt


##########
# WHEEL SPECIFIC parameters of each bet type
##########
# Note that while below only default options are used, to create parameters specific to each wheel, just
# create a new variable(s) for the given wheel, e.g. euro_wheel_min_colours_bet


default_min_colours_bet = 5
default_max_colours_bet = 50

default_min_straight_up_bet = 2
default_max_straight_up_bet = 20

default_min_new_bet = None  # Dummy new min/max bet parameters
default_max_new_bet = None

default_min_pot_to_add_more_bets = 10


# User must have at least min_pot_to_add_more_bets to be given the option to add an EXTRA bet to current spin
# This would ideally exceed all min_bets, so that user never gets asked to go all in after placing multiple bets


##########
# Definition of data classes to be used when pulling together above bet parameters and defining on each wheel
##########
@dataclass
class IndividualBetParameters:
    """
    Min/max bet parameters for a bet
    Note separate instances can be created for individual wheels.
    """
    min_bet: int
    max_bet: int


@dataclass
class BetParameters:
    """Class containing all the individual parameters that need to be defined for a given wheel"""
    MIN_POT_FOR_MORE_BETS: int
    COLOURSBET: IndividualBetParameters
    STRAIGHTUPBET: IndividualBetParameters
    NEWBET: IndividualBetParameters = None  # Dummy new attribute for new bet type


##########
# Default instances of the data classes carrying the default parameters
##########
default_colours_bet_parameters = IndividualBetParameters(min_bet=default_min_colours_bet,
                                                         max_bet=default_max_colours_bet)
default_straight_up_bet_parameters = IndividualBetParameters(min_bet=default_min_straight_up_bet,
                                                             max_bet=default_max_straight_up_bet)

# default_new_bet_parameters = IndividualBetParameters(min_bet=default_min_new_bet,
#                                                      max_bet=default_max_new_bet)
##########
# Definitions of the bet parameters on each wheel
##########
euro_wheel_parameters = BetParameters(
    MIN_POT_FOR_MORE_BETS=default_min_pot_to_add_more_bets,
    COLOURSBET=default_colours_bet_parameters,
    STRAIGHTUPBET=default_straight_up_bet_parameters)

american_wheel_parameters = BetParameters(
    MIN_POT_FOR_MORE_BETS=default_min_pot_to_add_more_bets,
    COLOURSBET=default_colours_bet_parameters,
    STRAIGHTUPBET=default_straight_up_bet_parameters)

new_wheel_parameters = BetParameters(
    MIN_POT_FOR_MORE_BETS=default_min_pot_to_add_more_bets,
    COLOURSBET=default_colours_bet_parameters,
    STRAIGHTUPBET=default_straight_up_bet_parameters)


##########
# Data class carrying WHEEL SPECIFIC min_bet, max_bet, and_min_pot_for_more_bet parameters
##########
@dataclass(frozen=True)
class WheelBetParameters:
    """Hierarchy of all bet parameters, which are specific to each wheel."""
    EUROWHEEL = euro_wheel_parameters
    AMERICANWHEEL = american_wheel_parameters
