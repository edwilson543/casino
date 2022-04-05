from Games.Roulette.app.roulette_base_classes import RouletteBet
from Games.Roulette.definitions.wheel_defns import wheel_options

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
# TODO may want to link the default parameters to some central dictionary
# TODO should we restate the payout method here?
# TODO should we have none as the default
# TODO should we be including the wheel within the attributes
class ColoursBet(RouletteBet):
    """In the game flow, we'll instantiate a bet, and then the user inputs will be used to define:
    first, the playing wheel_id
    second, the colour
    third (and automatically, the win_criteria and payout)"""
    def __init__(self,
                 payout: int = None,
                 win_criteria: list = None,  # resolution?
                 min_bet: int = 5,
                 max_bet: int = 50,
                 bet_type_id: str = 'C',
                 playing_wheel_id: str = None,
                 colour: str = None):
        super().__init__(payout, win_criteria, min_bet, max_bet, bet_type_id, playing_wheel_id)
        self.bet_type_id = bet_type_id
        self.playing_wheel_id = playing_wheel_id
        self.playing_wheel = wheel_options[playing_wheel_id]
        self.colour = colour

    def determine_win_criteria(self):
        """Abstract method for calculating the win crtieria of a given bet - will be bet specific"""
        self.win_criteria = [slot_num for slot_num in self.playing_wheel.slots if
                             self.playing_wheel.slots[slot_num] == self.colour]

    def determine_colour(self, colour: str):
        self.colour = colour
