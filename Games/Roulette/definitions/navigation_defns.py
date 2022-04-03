"""
ID codes to allow the user to loop the game to the relevant point after bet evaluation
To add a new navigation (obviously first need a new step/aspect of the game):
1) Add the relevant text below - note the text is ended as the order of likeliness of that user will select it
2) Add a label for where in the for loop the navigation is, with a corresponding list for all the subsequent steps
which must also be taken
3) Add it to the list of navigation_options
3) Add a relevant if statement in roulette_mechanics
4) Initialise a parameter for the new navigation in the RouletteGame class
"""

#########
# Navigation options in the for loop in the roulette_mechanics module
#########
navigation_text = "[R]epeat bet; change bet: [C]hoice, [S]take, [T]ype, [W]heel"
navigation_dict = {'from_wheel_selection': ['W'],
                   'from_bet_selection': ['T', 'W'],
                   'from_stake_quantification': ['S', 'T', 'W'],
                   'from_bet_choice': ['C', 'S', 'T', 'W'],
                   'from_bet_evaluation': ['R', 'C', 'S', 'T', 'W']}
navigation_options = ['R', 'C', 'S', 'T', 'W']

