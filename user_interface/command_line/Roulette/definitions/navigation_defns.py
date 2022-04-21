"""
ID codes to allow the user to loop the game to the relevant point after bet evaluation
The first set of options corresponds to the case where the user has sufficient funds to continue using the same stake
amount.
The second set of 'low_funds' options restricts the navigation options so that the user will have to
change their stake amount, which is required in the case that insufficient funds remain to repeat the bet.
"""

#########
# Navigation options in the for loop in the roulette_mechanics module, if active stake does not exceed min bet
#########
navigation_text = "[R]epeat bet; change bet: [C]hoice, [S]take, [T]ype, [W]heel"
navigation_dict = {'from_wheel_selection': ['W'],
                   'from_individual_bet_selection': ['T', 'W'],
                   'from_stake_quantification': ['S', 'T', 'W'],
                   'from_bet_choice': ['C', 'S', 'T', 'W'],
                   'from_bet_evaluation': ['R', 'C', 'S', 'T', 'W']}
navigation_options = ['R', 'C', 'S', 'T', 'W']

#########
# Navigation options in the for loop in the roulette_mechanics module, if active stake does exceed min bet
#########
navigation_text_low_funds = "Change bet: [S]take, [T]ype, [W]heel"
navigation_options_low_funds = ['S', 'T', 'W']
