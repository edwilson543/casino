from Games.Roulette.app.roulette_wheel_base_class import RouletteWheel
from Games.Roulette.app.roulette_bet_base_class import RouletteBet

# TODO update this description
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
4) Define a subclass of the RouletteBet class as below for colours/ straight up bets. These include the win criteria
setting, and the payout calculation
5) Add the bet subclass to the bet_type_options dictionary at the bottom of this module
##### To update
5) Add the methods to the dictionary which is within the RouletteWheelWagers class definitions, with the first key
corresponding to the wheel, and the second key corresponding to the bet type.
"""
# TODO should this stay here, or go in the UI?
# Step 1 as above
bet_cat_options_text = {'E': "[I]nside, [O]utside", 'A': "[I]nside, [O]utside"}
# Step 2 as above
bet_cats_and_types = {'E': {'O': ['C'], 'I': ['S']}, 'A': {'O': ['C'], 'I': ['S']}}

# Bet type options to be displayed once the category has been selected:
bet_type_options_text = {'E': {'O': "[C]olours", 'I': "[S]traight up"}, 'A': {'O': "[C]olours", 'I': "[S]traight up"}}
# Min and max bet for each bet type:
bet_type_min_max_bet = {'E': {'C': {'min': 5, 'max': 50}, 'S': {'min': 5, 'max': 20}},
                        'A': {'C': {'min': 5, 'max': 50}, 'S': {'min': 5, 'max': 20}}}

###############################
# Create subclass of the RouletteBet base class to define each bet
###############################
"""
In the game flow, we instantiate a bet, based on the active_bet_type_id.
Then user will then input their bet choice, which will determine the win_criteria (which is consistently defined as a
list of slot numbers), and this will be used to calculate the payout, (calculated as the bias_wheel_size divided by the
length of the win_criteria list)
"""


# TODO may want to link the parameters out - could just define them above? or is it better to just define them within
#  each class. Note they are repeated in bet_type_defns_user so would need to be updated in 2 different places
class ColoursBet(RouletteBet):
    """Class for defining the win criteria of a colours bet."""

    def __init__(self,
                 min_bet: int = 5,
                 max_bet: int = 50,
                 bet_type_id: str = 'C'):
        super().__init__(min_bet, max_bet, bet_type_id)

    def get_winning_slots_list(self, playing_wheel: RouletteWheel, choice: str) -> list:
        """Returns: list of the slot numbers of the same colour as the input colour."""
        if choice in playing_wheel.slots.values():
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

    def get_winning_slots_list(self, playing_wheel: RouletteWheel, choice: int):
        if choice in playing_wheel.slots:
            return [choice]
        else:
            raise ValueError(f"{choice} is not a slot on the {playing_wheel} Roulette wheel")


###############################
# Add the newly defined bet class to the bet_type_options dictionary below
###############################
bet_type_options = {'C': ColoursBet(), 'S': StraightUpBet()}
