"""
To define a new wheel complete the following steps:
1) create wheel_defn as a mapping of the numbers on the wheel to the colours
2) define a payout scaler. payout := stake * payout_scaler / P(bet winning)
3) Add to the wheel_options dict below, using an identification key (probably just first letter unless repeats)
4) Add the wheel option to the wheel_options_text so that it can be chosen in the game
"""

euro_wheel_defn = {0: 'green', 1: 'red', 2: 'black', 3: 'red', 4: 'black', 5: 'red', 6: 'black', 7: 'red',
                   8: 'black', 9: 'red', 10: 'black', 11: 'black', 12: 'red', 13: 'black', 14: 'red', 15: 'black',
                   16: 'red', 17: 'black', 18: 'red', 19: 'red', 20: 'black', 21: 'red', 22: 'black', 23: 'red',
                   24: 'black', 25: 'red', 26: 'black', 27: 'red', 28: 'black', 29: 'black', 30: 'red', 31: 'black',
                   32: 'red', 33: 'black', 34: 'red', 35: 'black', 36: 'red'}
euro_wheel_payout_scaler = 0.95

dummy_second_wheel_defn = {0: 'black', 1: 'white'}
dummy_second_wheel_scaler = 0.95

"""
Choices for the different wheels to play on.
Once a new wheel has been defined, it must be added to the dictionary below, and included in the string
wheel_options_text so that it can be accessed.
"""
wheel_options = {'E': [euro_wheel_defn, euro_wheel_payout_scaler],
                 'D': [dummy_second_wheel_defn, dummy_second_wheel_scaler]}
wheel_options_text = "[E]uropean, [D]ummy"
