from Games.Roulette.app.roulette_base_classes import RouletteWheelWagers  # to use to define each bet

"""
Interested to know whether it's better to employ the method below, or something else. An alternative I thought
of was to define all the different types of bet within one class in roulette_base_classes, and then intialise a 
mapping in the class of bet_id onto which methods to call.
"""

"""
To define a new bet type and category complete the following steps:
1) Add the bet name to a list in bet_cats_and_types dictionary under the relevant category (key).
If necessary define a new category by adding a key to the dictionary.
2) If the bet involved defining a new category, add the category to the bet_cat_options_text
3) Add the bet to the bet_type_options_text, again under the relevant key, defining a new one for the category if needed
Note the bet cat/type distinction is essentially trivial, but it gives the option of not displaying
100 different bet choices in one go...
4) In the class RouletteWheelWagers in roulette base classes,
define the class methods: place_bet_new_bet_type() and get_winning_set_new_bet_type() for the new bet
5) Add the methods to the dictionary which is within the RouletteWheelWagers intialisation
"""

# Bet types and categories mapping - essentially useless, but to avoid giving user 10 bet options at once
bet_cats_and_types = {'O': ['C'], 'I': ['S']}
bet_cat_options_text = "[I]nside, [O]utside"
bet_type_options_text = {'O': "[C]olours", 'I': "[S]traight_up"}
bet_type_min_max_bet = {'C': {'min': 5, 'max': 50}, 'S': {'min': 5, 'max': 20}}
