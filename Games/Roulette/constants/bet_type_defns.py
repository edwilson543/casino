"""
To define a new bet type and category complete the following steps:
1) Add the bet name to a list in bet_cats_and_types dictionary under the relevant category (key).
If necessary define a new category by adding a key to the dictionary.
2) If the bet involved defining a new category, add the category to the bet_cat_options_text
3) Add the bet to the bet_type_options_text, again under the relevant key, defining a new one for the category if needed
4) Define the class method for that bet (non-triv.)
Note the bet cat/type distinction is essentially trivial, but it gives the option of not displaying
100 different bet choices in one go...
"""
bet_cats_and_types = {'I': ['C'], 'O': ['S']}

bet_cat_options_text = "[I]nside, [O]utside"
bet_type_options_text = {'I': "[C]olours", 'O': "[S]traight_up"}

# then will need a mapping of C, S to different bet method calls
