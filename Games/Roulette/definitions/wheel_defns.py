from Games.Roulette.app.roulette_base_classes import RouletteWheel

# TODO define relational dictionaries for the roulette boards, and add to the class attributes
"""
To define a new wheel complete the following steps:
1) create wheel_defn as a mapping of the numbers on the wheel to the colours
2) define a payout scaler. payout := stake * payout_scaler / P(bet winning)
3) Instantiate the relevant wheel using the definitions
3) Add the wheel to the wheel_options dict below, using an identification key
4) Add the wheel option to the wheel_options_text so that it can be chosen in the game, with the same key
5) Add relevant bet type options to the wheel in bet_type_defns, using the wheel id key from wheel_options
6) Map relevant bet type methods for the wheel in roulette_bas_classes RouletteWheel class, defining any new methods
if necessary.
"""
###############################
# Wheel definitions and payouts
###############################
euro_wheel_defn = {0: 'green', 1: 'red', 2: 'black', 3: 'red', 4: 'black', 5: 'red', 6: 'black', 7: 'red',
                   8: 'black', 9: 'red', 10: 'black', 11: 'black', 12: 'red', 13: 'black', 14: 'red', 15: 'black',
                   16: 'red', 17: 'black', 18: 'red', 19: 'red', 20: 'black', 21: 'red', 22: 'black', 23: 'red',
                   24: 'black', 25: 'red', 26: 'black', 27: 'red', 28: 'black', 29: 'black', 30: 'red', 31: 'black',
                   32: 'red', 33: 'black', 34: 'red', 35: 'black', 36: 'red'}
euro_wheel_payout_scaler = 0.95

american_wheel_defn = {-1: 'green', 0: 'green', 1: 'red', 2: 'black', 3: 'red', 4: 'black', 5: 'red', 6: 'black',
                       7: 'red', 8: 'black', 9: 'red', 10: 'black', 11: 'black', 12: 'red', 13: 'black', 14: 'red',
                       15: 'black', 16: 'red', 17: 'black', 18: 'red', 19: 'red', 20: 'black', 21: 'red', 22: 'black',
                       23: 'red', 24: 'black', 25: 'red', 26: 'black', 27: 'red', 28: 'black', 29: 'black', 30: 'red',
                       31: 'black', 32: 'red', 33: 'black', 34: 'red', 35: 'black', 36: 'red'}
american_wheel_payout_scaler = 0.95
# note -1 corresponds to 00, which is in effect the same as 0

template_wheel_defn = {0: 'black', 1: 'white'}
template_wheel_scaler = 0.95

###############################
# Instantiate the wheel objects
###############################
euro_wheel = RouletteWheel(slots=euro_wheel_defn, payout_scaler=euro_wheel_payout_scaler)
american_wheel = RouletteWheel(slots=american_wheel_defn, payout_scaler=american_wheel_payout_scaler)
template_wheel = RouletteWheel(slots=template_wheel_defn, payout_scaler=template_wheel_scaler)

##############################
# Dictionary and associated text for the different wheel options
##############################
wheel_options = {'E': euro_wheel, 'A': american_wheel}
wheel_options_text = "[E]uropean, [A]merican"
