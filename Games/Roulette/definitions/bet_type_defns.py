from Games.Roulette.app.roulette_base_classes import RouletteWheelWagers

"""
To define a new bet type and category complete the following steps:
1) Add the bet name to a list in bet_cats_and_types dictionary under the relevant category (key).
If necessary define a new category by adding a key to the dictionary.
2) If the bet involved defining a new category, add the category to the bet_cat_options_text
3) Add the bet to the bet_type_options_text, again under the relevant key, defining a new one for the category if needed
4) Define the class for that bet - copy and paste from one of the existing ones, and edit as relevant
Note the bet cat/type distinction is essentially trivial, but it gives the option of not displaying
100 different bet choices in one go...
"""
from Games.Roulette.app.roulette_base_classes import RouletteWheelWagers # so we can define each bet

# Bet types and categories mapping - essentially useless, but to avoid giving user 10 bet options at once
bet_cats_and_types = {'O': ['C'], 'I': ['S']}
bet_cat_options_text = "[I]nside, [O]utside"
bet_type_options_text = {'O': "[C]olours", 'I': "[S]traight_up"}

# Class definitions for each bet
class ColoursBet(RouletteWheelWagers):
    """Class definition for the colours bet"""
    def __init__(self, bet_id: str, min_bet: int, max_bet: float):
        bet_id = 'C'
        min_bet = 5
        max_bet = 50
        super().__init__(bet_id, min_bet, max_bet) # need to consider if all attributes need to be specified

    def set_stake(self):
        """Note this is define here as much of it depends on the min and max bet"""
        pass

    def place_bet(self):
        pass

    def winning_set(self):
        pass

# Mapping of bet type options to bet classes
bet_type_options = {'C': ColoursBet(bet_id='C', min_bet=5, max_bet=50)}