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
place_bet_new_bet_type() and get_winning_set_new_bet_type() for the new bet.
If the bet type is wheel specific, add a suffix for the wheel name, otherwise no need.
5) Add the methods to the dictionary which is within the RouletteWheelWagers class definitions, with key 'WB', where
'W' is the wheel that the bet corresponds to and 'B' the bet type.
If the bet is not wheel specific, we still need to map each wheel x bet pair onto the bet method, so include as many
'WB's as there are methods
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
