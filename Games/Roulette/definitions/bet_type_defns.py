from Games.Roulette.app.roulette_base_classes import RouletteBet
from Games.Roulette.definitions.wheel_defns import wheel_options
from math import floor

# general q - should we have the _text strings in the UI folder - seems like it could get a bit messy if separated?

"""
To define a new bet type and category complete the following steps:
1) If the bet involves defining a new category, add the category to the bet_cat_options_text, for each of the relevant
wheels. If the bet falls within an existing category, bet_cat_options_text does not need updating.
2) Add the bet name to the lists in the bet_cats_and_types dictionary under for the relevant wheels (first key) and for
the relevant bet category. The wheels are the first keys, the bet categories the second keys.
If necessary define a new category by adding a key to the dictionary.
3) Add the bet to the bet_type_options_text, again firstly under the relevant wheel keys (first keys), and secondly
under the relevant bet category keys (second keys) defining a new one for the category if needed.
Note that the bet cat/type distinction is essentially trivial, but it gives the option of not displaying
100 different bet choices in one go...
4) In the class RouletteWheelWagers in roulette base classes,define the class methods:
place_bet_new_bet_type() and get_winning_slots_new_bet_type() for the new bet.
If the bet type is wheel specific, add a suffix for the wheel name, otherwise no need.
5) Add the methods to the dictionary which is within the RouletteWheelWagers class definitions, with the first key
corresponding to the wheel, and the second key corresponding to the bet type.
"""

# Step 1 as above
bet_cat_options_text = {'E': "[I]nside, [O]utside", 'A': "[I]nside, [O]utside"}
# Step 2 as above
bet_cats_and_types = {'E': {'O': ['C'], 'I': ['S']}, 'A': {'O': ['C'], 'I': ['S']}}

# Bet type options to be displayed once the category has been selected:
bet_type_options_text = {'E': {'O': "[C]olours", 'I': "[S]traight_up"}, 'A': {'O': "[C]olours", 'I': "[S]traight_up"}}
# Min and max bet for each bet type:
bet_type_min_max_bet = {'E': {'C': {'min': 5, 'max': 50}, 'S': {'min': 5, 'max': 20}},
                        'A': {'C': {'min': 5, 'max': 50}, 'S': {'min': 5, 'max': 20}}}

###############################
# Create subclass of the RouletteBet base class for each defined bet
###############################
"""
In the game flow, we'll instantiate a bet, based on the active_wheel_id and active_bet_type_id.
Then will use user input to determine the win_criteria (which is consistently defined as a list of slot numbers),
and this will be used to automatically calculate the payout, as the bias_wheel_size divided by the length of the
win_criteria list
"""


# TODO may want to link the default parameters to some central dictionary/enum?
# TODO should we have none as the default playing wheel id?
# TODO should we be including the wheel/bias_wheel_size within the attributes - maybe covered in data storage approach?
# I guess ideally we wouldn't have to restate the payout method for every subclass
class ColoursBet(RouletteBet):
    """Class for defining win criteria and payout of a colours bet"""

    def __init__(self,
                 min_bet: int = 5,
                 max_bet: int = 50,
                 bet_type_id: str = 'C',
                 win_criteria: list = None,
                 payout: int = None,
                 playing_wheel_id: str = None):
        super().__init__(min_bet, max_bet, bet_type_id, win_criteria, payout, playing_wheel_id)
        self.playing_wheel = wheel_options[playing_wheel_id]

    @property
    def win_criteria(self):
        return self.win_criteria

    @win_criteria.setter
    def win_criteria(self, colour: str):
        self.win_criteria = [slot_num for slot_num in self.playing_wheel.slots if
                             self.playing_wheel.slots[slot_num] == colour]

    def calculate_payout(self):
        win_probability_over_estimate = len(self.win_criteria) / self.playing_wheel.bias_wheel_size()
        self.payout = floor(1 / win_probability_over_estimate)


class StraightUpBet(RouletteBet):
    """Class for defining win criteria and payout for a straight up bet"""

    def __init__(self,
                 min_bet: int = 10,
                 max_bet: int = 20,
                 bet_type_id: str = 'S',
                 win_criteria: list = None,
                 payout: int = None,
                 playing_wheel_id: str = None):
        super().__init__(min_bet, max_bet, bet_type_id, win_criteria, payout, playing_wheel_id)
        self.playing_wheel = wheel_options[playing_wheel_id]

    @property
    def win_criteria(self):
        return self.win_criteria

    @win_criteria.setter
    def win_criteria(self, number: int):
        self.win_criteria = [number]

    def calculate_payout(self):
        win_probability_over_estimate = len(self.win_criteria) / self.playing_wheel.bias_wheel_size()
        self.payout = floor(1 / win_probability_over_estimate)
