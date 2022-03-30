from Games.Roulette.app.roulette_base_classes import RouletteWheel

# TODO define relational dictionaries for the roulette boards, and add to the class attributes
"""
To define a new wheel complete the following steps:
1) Create wheel_defn as a mapping of the numbers on the wheel to the colours
2) Define a payout scaler. payout := stake * payout_scaler / P(bet winning)
3) Add some colour ids - these should be unique, using as many characters as necessary e.g. BLU and BLA if blue and
black feature on the same wheel
4) Define a colour_options_text for that wheel, which should correspond to the colour ids 
5) Instantiate the relevant wheel using the definitions
6) Add the wheel to the wheel_options dict below, using an identification key
7) Add the wheel option to the wheel_options_text so that it can be chosen in the game, with the same key
8) Add relevant bet type options to the wheel in bet_type_defns, using the wheel id key from wheel_options
9) Map relevant bet type methods for the wheel in roulette_bas_classes RouletteWheel class, defining any new methods
if necessary.
"""
#TODO add dictionaries for the boards to the definitions, maybe with supporting string rep of form "|1|2|\n-----\n|3|4|"
###############################
# Wheel definitions and payouts
###############################
euro_wheel_defn = {0: 'green', 1: 'red', 2: 'black', 3: 'red', 4: 'black', 5: 'red', 6: 'black', 7: 'red',
                   8: 'black', 9: 'red', 10: 'black', 11: 'black', 12: 'red', 13: 'black', 14: 'red', 15: 'black',
                   16: 'red', 17: 'black', 18: 'red', 19: 'red', 20: 'black', 21: 'red', 22: 'black', 23: 'red',
                   24: 'black', 25: 'red', 26: 'black', 27: 'red', 28: 'black', 29: 'black', 30: 'red', 31: 'black',
                   32: 'red', 33: 'black', 34: 'red', 35: 'black', 36: 'red'}
euro_wheel_payout_scaler = 0.95
euro_wheel_colour_ids = {'G': 'green', 'R': 'red', 'B': 'black'}
euro_wheel_colour_options_text = "[G]reen, [R]ed, [B]lack"

american_wheel_defn = {-1: 'green', 0: 'green', 1: 'red', 2: 'black', 3: 'red', 4: 'black', 5: 'red', 6: 'black',
                       7: 'red', 8: 'black', 9: 'red', 10: 'black', 11: 'black', 12: 'red', 13: 'black', 14: 'red',
                       15: 'black', 16: 'red', 17: 'black', 18: 'red', 19: 'red', 20: 'black', 21: 'red', 22: 'black',
                       23: 'red', 24: 'black', 25: 'red', 26: 'black', 27: 'red', 28: 'black', 29: 'black', 30: 'red',
                       31: 'black', 32: 'red', 33: 'black', 34: 'red', 35: 'black', 36: 'red'}
american_wheel_payout_scaler = 0.95
# note -1 corresponds to 00, which is in effect the same as 0
american_wheel_colour_ids = {'G': 'green', 'R': 'red', 'B': 'black'}
american_wheel_colour_options_text = "[G]reen, [R]ed, [B]lack"

template_wheel_defn = {0: 'black', 1: 'white'}
template_wheel_scaler = 0.95
template_wheel_colour_ids = {'B': 'black', 'W': 'white'}
template_wheel_colour_options_text = "[B]lack, [W]hite"

###############################
# Instantiate the wheel objects
###############################
euro_wheel = RouletteWheel(slots=euro_wheel_defn, payout_scaler=euro_wheel_payout_scaler,
                           colour_ids=euro_wheel_colour_ids, colour_options=euro_wheel_colour_options_text)

american_wheel = RouletteWheel(slots=american_wheel_defn, payout_scaler=american_wheel_payout_scaler,
                               colour_ids=american_wheel_colour_ids, colour_options=american_wheel_colour_options_text)
template_wheel = RouletteWheel(slots=template_wheel_defn, payout_scaler=template_wheel_scaler,
                               colour_ids=template_wheel_colour_ids, colour_options=template_wheel_colour_options_text)

##############################
# Dictionary and associated text for the different wheel options
##############################
wheel_options = {'E': euro_wheel, 'A': american_wheel}
wheel_options_text = "[E]uropean, [A]merican"
