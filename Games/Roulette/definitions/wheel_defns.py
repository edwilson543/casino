from Games.Roulette.app.roulette_base_classes import RouletteWheel

"""
To define a new wheel complete the following steps:
1) create wheel_defn as a mapping of the numbers on the wheel to the colours
2) define a payout scaler. payout := stake * payout_scaler / P(bet winning)
3) Instantiate the relevant wheel using the definitions
3) Add the wheel to the wheel_options dict below, using an identification key
4) Add the wheel option to the wheel_options_text so that it can be chosen in the game, with the same key
"""
# Wheel definitions and payouts
euro_wheel_defn = {0: 'green', 1: 'red', 2: 'black', 3: 'red', 4: 'black', 5: 'red', 6: 'black', 7: 'red',
                   8: 'black', 9: 'red', 10: 'black', 11: 'black', 12: 'red', 13: 'black', 14: 'red', 15: 'black',
                   16: 'red', 17: 'black', 18: 'red', 19: 'red', 20: 'black', 21: 'red', 22: 'black', 23: 'red',
                   24: 'black', 25: 'red', 26: 'black', 27: 'red', 28: 'black', 29: 'black', 30: 'red', 31: 'black',
                   32: 'red', 33: 'black', 34: 'red', 35: 'black', 36: 'red'}
euro_wheel_payout_scaler = 0.95

american_wheel_defn = {00: 'green', 0: 'green', 1: 'red', 2: 'black', 3: 'red',4: 'black', 5: 'red', 6: 'black',
                       7: 'red', 8: 'black',9: 'red',10: 'black',11: 'black',12: 'red', 13: 'black', 14: 'red',
                       15: 'black'}

dummy_second_wheel_defn = {0: 'black', 1: 'white'}
dummy_second_wheel_scaler = 0.95

# Instantiate the wheel objects
euro_wheel = RouletteWheel(slots=euro_wheel_defn, payout_scaler=euro_wheel_payout_scaler)
dummy_wheel = RouletteWheel(slots=dummy_second_wheel_defn, payout_scaler=dummy_second_wheel_scaler)

# Dictionary and associated text for the different wheel options
wheel_options = {'E': euro_wheel,'D': dummy_wheel}
wheel_options_text = "[E]uropean, [D]ummy"
