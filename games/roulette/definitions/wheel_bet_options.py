"""
Module for defining the bets that can be played on each wheel.
Note that the bets themselves + parameters are defined elsewhere.
Also note only default parameters are used currently, although adding a wheel specific parameter is
straight forward - details below
"""
from games.roulette.definitions.bet_parameters import BetTypeIds, BetTypePrompts
from enum import Enum
from dataclasses import dataclass


##########
# Bet category IDs to be used for each bet category - UI focused
##########
class BetCategoryIdsPrompts(str, Enum):
    """
    Class specifying the IDs and prompts of each bet category
    Note that this is used to look up the bet category name from the bet category ID,
    and to construct the bet category command line navigation prompt.
    Note also there's benefit above to splitting out IDs/prompts, but can't see any here.
    """
    INSIDEBETS = "I"
    OUTSIDEBETS = "O"
    INSIDEBETS_PROMPT = "[I]nside"  # key prompt should corresponds to id above
    OUTSIDEBETS_PROMPT = "[O]utside"  # key prompt should corresponds to id above


##########
# WHEEL SPECIFIC parameters of each bet type
##########
# Note that while below only default options are used, to create parameters specific to each wheel, just
# create a new variable(s) for the given wheel, e.g. euro_wheel_inside_bet_options

default_bet_cat_options = [BetCategoryIdsPrompts.INSIDEBETS.value,
                           BetCategoryIdsPrompts.OUTSIDEBETS.value]
default_bet_cats_prompt = BetCategoryIdsPrompts.INSIDEBETS_PROMPT.value + ", " + \
                          BetCategoryIdsPrompts.OUTSIDEBETS_PROMPT.value

"""These are the only variables requiring updating to add a new bet option to an existing category,
if a new category is created, more work is required"""
default_inside_bet_options = [BetTypeIds.COLOURSBET.value]  # list of inside bet ids
default_inside_bets_prompt = BetTypePrompts.COLOURSBET.value

default_outside_bet_options = [BetTypeIds.STRAIGHTUPBET.value]  # list of outside bet ids
default_outside_bets_prompt = BetTypePrompts.STRAIGHTUPBET.value


##########
# Definition of data classes to be used when pulling together above bet parameters and defining on each wheel
##########
@dataclass
class BetCatTypeOptions:
    """
    List of the category/bet type options, and text string to display this list.
    Used to list/ prompt both bet CATEGORY and bet TYPES, as it's an identical structure.
    Note separate instances can be created for individual wheels.
    """
    options: list
    options_text: str


@dataclass
class BetOptions:
    """Class containing all the individual parameters that need to be defined for a given wheel"""
    BET_CATS: BetCatTypeOptions
    INSIDEBETS: BetCatTypeOptions
    OUTSIDEBETS: BetCatTypeOptions
    NEW_BET_CAT: BetCatTypeOptions = None  # Dummy new bet category on the wheel


##########
# Default instances of the data classes carrying the default parameters
##########

default_bet_cats = BetCatTypeOptions(options=default_bet_cat_options,
                                     options_text=default_bet_cats_prompt)
default_inside_bet_types = BetCatTypeOptions(options=default_inside_bet_options,
                                             options_text=default_inside_bets_prompt)
default_outside_bet_types = BetCatTypeOptions(options=default_outside_bet_options,
                                              options_text=default_outside_bets_prompt)

##########
# Definitions of the bet options on each wheel
##########
euro_wheel_bet_options = BetOptions(
    BET_CATS=default_bet_cats,
    INSIDEBETS=default_inside_bet_types,
    OUTSIDEBETS=default_outside_bet_types)

american_wheel_bet_options = BetOptions(
    BET_CATS=default_bet_cats,
    INSIDEBETS=default_inside_bet_types,
    OUTSIDEBETS=default_outside_bet_types)


##########
# Data class carrying ALL WHEEL SPECIFIC bet parameters
##########
@dataclass(frozen=True)
class WheelBetOptions:
    """
    Hierarchy of all bet options, which are specific to each wheel.
    """
    EUROWHEEL = american_wheel_bet_options
    AMERICANWHEEL = euro_wheel_bet_options
