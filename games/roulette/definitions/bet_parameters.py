from enum import Enum
from dataclasses import dataclass


class BetTypeIds(str, Enum):
    COLOURSBET = 'C'
    STRAIGHTUPBET = 'S'


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

    #  TODO give roulette wheel a name and use it here

    class E:  # EuroWheel
        """Parameters for the different bet categories available on the given wheel"""
        bet_cat_options = ['I', 'O']
        bet_cat_options_text = "[I]nside, [O]utside"

        class I:
            """Parameters for the different bet types within the category, on the given wheel"""
            bet_type_options = ['S']
            bet_type_options_text = "[S]traight up"

        class O:
            """Parameters for the different bet types within the category, on the given wheel"""
            bet_type_options = ['C']
            bet_type_options_text = "[C]olours"

        class COLOURSBET:
            """Parameters for the colours bet on the given wheel"""
            min_bet = 5
            max_bet = 50

        class STRAIGHTUPBET:
            """Parameters for the straight up bet on the given wheel"""
            min_bet = 2
            max_bet = 20

    class A:  # AmericanWheel
        bet_cat_options = ['I', 'O']
        bet_cat_options_text = "[I]nside, [O]utside"

        class I:
            bet_type_options = ['S']
            bet_type_options_text = "[S]traight up"

        class O:
            bet_type_options = ['C']
            bet_type_options_text = "[C]olours"

        class COLOURSBET:
            min_bet = 5
            max_bet = 50

        class STRAIGHTUPBET:
            min_bet = 2
            max_bet = 20
