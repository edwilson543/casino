from enum import Enum
from dataclasses import dataclass


class BetTypeIds(str, Enum):
    ColoursBet = 'C'
    StraightUpBet = 'S'


@dataclass(frozen=True)
class BetParameters:
    """
    # user must have at least min_pot_to_add_more_bets to be given the option to add EXTRA bet to current spin
    # This would ideally exceed all min_bets, so that user never gets asked to go all in after placing multiple bets
    """
    min_pot_to_add_more_bets = 15

    """
    Hierarchy of all the min/max bet parameters, which are specific to each wheel.
    Note that the bet class names (C/S etc.) must match the BetTypeIds string ('C'/'S' etc.)
    Similarly, the wheel class names (E/A etc.) must match the WheelIds string ('E'/'A' etc.) in wheel parameters
    """

    #  TODO double check there isn't a way of getting the C/E/A to be dynamically defined
    #  TODO give roulette wheel a name and use it here

    class E:  # EuroWheel

        class ColoursBet:
            min_bet = 5
            max_bet = 50

        class StraightUpBet:
            min_bet = 2
            max_bet = 20

    class A:  # AmericanWheel

        class ColoursBet:
            min_bet = 5
            max_bet = 50

        class StraightUpBet:
            min_bet = 2
            max_bet = 20
