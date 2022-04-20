from Games.Roulette.app.roulette_wheel_base_class import RouletteWheel
from Games.Roulette.app.roulette_bet_base_class import RouletteBet

"""
To define a new bet type and category complete the following steps:
1) Think how to store all parameters, and make wheel relevant
2) Create a subclass of RouletteBet base class (below) to define each bet's 'determine_win_criteria' method, which
is used as a polymorphic method
3) Add the subclass to the bet_type_options below
4) Go to command_line -> Roulette -> definitions -> bet_type_defns_user
5) Add the new bet to bet_cat_options_text, bet_cats_and_types, bet_type_options_text where relevant
6) Define a subclass of the class defined at 3), to define the UI polymorphic method 'get_user_bet_choice'
7) Add the newly defined user bet class to the bet_type_options_user dictionary  
"""

# TODO - find some way of defining bet parameters to be looked up from, so can be wheel specific -
# This'll probably involve adding a wheel_id to RouletteBet and subclass as an instance attribute
##########
# Min and max bet for each bet type - not currently used
##########
bet_type_min_max_bet = {'E': {'C': {'min': 5, 'max': 50}, 'S': {'min': 5, 'max': 20}},
                        'A': {'C': {'min': 5, 'max': 50}, 'S': {'min': 5, 'max': 20}}}


##########
# Create subclass of RouletteBet base class to define each bet's 'determine_win_criteria' method
##########
#  TODO may want to link the parameters out - could just define them above? or is it better to just define them within
#  each class. Note they are repeated in bet_type_defns_user so would need to be updated in 2 different places

class ColoursBet(RouletteBet):
    """Class for defining the win criteria of a colours bet."""

    def __init__(self,
                 min_bet: int = 5,
                 max_bet: int = 50,
                 bet_type_id: str = 'C'):
        super().__init__(min_bet, max_bet, bet_type_id)

    def determine_win_criteria(self, playing_wheel: RouletteWheel, choice: str) -> list[int]:
        """
        Parameters: choice - string of the form 'red'
        Returns: list of the slot numbers of the same colour as the input colour.
        """
        allowed_colours = set(playing_wheel.slots.values()).difference({playing_wheel.bias_colour})
        if choice in allowed_colours:
            return [slot_num for slot_num in playing_wheel.slots if playing_wheel.slots[slot_num] == choice]
        else:
            raise ValueError(f"{choice} is not a colour on the {playing_wheel} Roulette wheel")


class StraightUpBet(RouletteBet):
    """Class for defining the win criteria and payout for a straight up bet"""

    def __init__(self,
                 min_bet: int = 10,
                 max_bet: int = 20,
                 bet_type_id: str = 'S'):
        super().__init__(min_bet, max_bet, bet_type_id)

    def determine_win_criteria(self, playing_wheel: RouletteWheel, choice: int) -> list[int]:
        if choice in playing_wheel.slots:
            return [choice]
        else:
            raise ValueError(f"{choice} is not a slot on the {playing_wheel} Roulette wheel")


##########
# Add the newly defined bet class to the bet_type_options dictionary below
##########
bet_type_options = {'C': ColoursBet(), 'S': StraightUpBet()}
