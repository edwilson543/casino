#################
# Game parameters
#################
#TODO could swap these all for Enums or something??
deposit_parameters = {'min_deposit': 100, 'deposit_multiples': 10} # min % multiples must be 0
threshold_for_top_up_prompt = 50
top_up_parameters = {'min_top_up': 50, 'top_up_multiples': 10} # min % multiples must be 0

pause_durations = {'short': 0.5, 'medium': 1, 'long': 2} # durations for how long to wait at certain parts of the game.
# Currently only used in bet_evaluation, could get rid if this is a dodgy idea
