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
from Games.Roulette.app.roulette_wheel_base_class import RouletteWheel
from Games.Roulette.app.roulette_bet_base_class import RouletteBet
from typing import Union

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
                 bet_type_id: str = 'C',
                 stake: int = None,
                 bet_choice: Union[int, str, list] = None,
                 win_criteria: list[int] = None,
                 payout: int = None,
                 playing_wheel: RouletteWheel = None):
        super().__init__(min_bet, max_bet, bet_type_id, stake, bet_choice,
                         win_criteria, payout, playing_wheel)

    def determine_win_criteria(self) -> list[int]:
        """Returns: list of the slot numbers of the same colour as the input colour."""
        allowed_colours = set(self.playing_wheel.slots.values()).difference({self.playing_wheel.bias_colour})
        if self.bet_choice in allowed_colours:
            return [slot_num for slot_num in self.playing_wheel.slots if
                    self.playing_wheel.slots[slot_num] == self.bet_choice]
        else:
            raise ValueError(f"{self.bet_choice} is not a colour on the {self.playing_wheel.wheel_id} Roulette wheel")


class StraightUpBet(RouletteBet):
    """Class for defining the win criteria for a straight up bet"""

    def __init__(self,
                 min_bet: int = 10,
                 max_bet: int = 20,
                 bet_type_id: str = 'S',
                 stake: int = None,
                 bet_choice: Union[int, str, list] = None,
                 win_criteria: list[int] = None,
                 payout: int = None,
                 playing_wheel: RouletteWheel = None):
        super().__init__(min_bet, max_bet, bet_type_id, stake, bet_choice,
                         win_criteria, payout, playing_wheel)

    def determine_win_criteria(self) -> list[int]:
        """Returns: the bet_choice as a list (which for a colours bet will be an int)"""
        bet_choice = self.bet_choice
        if bet_choice in self.playing_wheel.slots:
            return [bet_choice]
        else:
            raise ValueError(f"{self.bet_choice} is not a slot on the {self.playing_wheel.wheel_id} Roulette wheel")


##########
# Add the newly defined bet class to the bet_type_options dictionary below
##########
bet_type_options = {'C': ColoursBet(), 'S': StraightUpBet()}
