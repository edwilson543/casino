from enum import Enum
from dataclasses import dataclass

straight_up_bet_id = "S"  # TODO dynamically reference all bet type IDs. Define once then refer to variable


class BetTypeIds(str, Enum):
    COLOURSBET = 'C'
    STRAIGHTUPBET = 'S'


@dataclass
class IndividualBetParameters:
    min_bet: int
    max_bet: int


@dataclass
class BetCatTypeOptions:
    options: list
    options_text: str


@dataclass
class FullDefinitionOfWheelBets:
    bet_cats: BetCatTypeOptions
    inside_bet_types: BetCatTypeOptions  # May need more here if we want new bet cats, can just not define if irrelevant
    outside_bet_types: BetCatTypeOptions
    colours_bet_parameters: IndividualBetParameters
    straight_up_bet_parameters: IndividualBetParameters


euro_wheel_bet_cats = BetCatTypeOptions(options=['I', 'O'], options_text="[I]nside, [O]utside")
euro_wheel_inside_bet_types = BetCatTypeOptions(options=['S'], options_text="[S]traight up")
euro_wheel_outside_bet_types = BetCatTypeOptions(options=['C'], options_text="[C]olours")
euro_wheel_colours_bet_parameters = IndividualBetParameters(min_bet=5, max_bet=50)
euro_wheel_straight_up_bet_parameters = IndividualBetParameters(min_bet=2, max_bet=20)

euro_wheel_full_definition = FullDefinitionOfWheelBets(
    bet_cats=euro_wheel_bet_cats,
    inside_bet_types=euro_wheel_inside_bet_types,
    outside_bet_types=euro_wheel_outside_bet_types,
    colours_bet_parameters=euro_wheel_colours_bet_parameters,
    straight_up_bet_parameters=euro_wheel_straight_up_bet_parameters)

american_wheel_bet_cats = BetCatTypeOptions(options=['I', 'O'], options_text="[I]nside, [O]utside")
american_wheel_inside_bet_types = BetCatTypeOptions(options=['S'], options_text="[S]traight up")
american_wheel_outside_bet_types = BetCatTypeOptions(options=['C'], options_text="[C]olours")
american_wheel_colours_bet_parameters = IndividualBetParameters(min_bet=5, max_bet=50)
american_wheel_straight_up_bet_parameters = IndividualBetParameters(min_bet=2, max_bet=20)

american_wheel_full_definition = FullDefinitionOfWheelBets(
    bet_cats=american_wheel_bet_cats,
    inside_bet_types=american_wheel_inside_bet_types,
    outside_bet_types=american_wheel_outside_bet_types,
    colours_bet_parameters=american_wheel_colours_bet_parameters,
    straight_up_bet_parameters=american_wheel_straight_up_bet_parameters)


@dataclass(frozen=True)
class BetParameters:
    """
    User must have at least min_pot_to_add_more_bets to be given the option to add EXTRA bet to current spin
    This would ideally exceed all min_bets, so that user never gets asked to go all in after placing multiple bets
    """
    min_pot_to_add_more_bets = 15

    """
    Hierarchy of all bet parameters, which are specific to each wheel.
    Similarly, the wheel class names (E/A etc.) must match the WheelIds string ('E'/'A' etc.) in wheel parameters
    """
    EUROWHEEL = american_wheel_full_definition
    AMERICANWHEEL = euro_wheel_full_definition
