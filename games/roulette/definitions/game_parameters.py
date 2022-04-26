#################
# Game parameters
#################

class DepositParameters:
    min_deposit = 100
    deposit_multiples = 10


class TopUpParameters:
    min_top_up = 50
    top_up_multiples = 10
    threshold_for_top_up_prompt = 50
    low_pot_forced_top_up = 10


class PauseDurations:
    short = 0.5
    medium = 1
    long = 2


class AllGameParameters:
    deposit_parameters = DepositParameters
    top_up_parameters = TopUpParameters
    pause_durations = PauseDurations


deposit_parameters = {'min_deposit': 100, 'deposit_multiples': 10}  # min % multiples must be 0
threshold_for_top_up_prompt = 10
low_pot_forced_top_up = 10
top_up_parameters = {'min_top_up': 50, 'top_up_multiples': 10}  # min % multiples must be 0

pause_durations = {'short': 0.5, 'medium': 1, 'long': 2}  # durations for how long to wait at certain parts of the game.

min_pot_to_add_more_bets = 15
# This must exceed min bet, so that user never goes in after placing multiple bets


##########
# TODO - find some way of defining bet parameters to be looked up from, so can be wheel specific -
# This'll probably involve adding a wheel_id to RouletteBet and subclass as an instance attribute,
# and then some kind of setter that uses a look up in the RouletteBet base class,
# Which is only called after setting the wheel - think this is problem solved.
##########
# Min and max bet for each bet type - not currently used
##########
bet_type_min_max_bet = {'E': {'C': {'min': 5, 'max': 50}, 'S': {'min': 5, 'max': 20}},
                        'A': {'C': {'min': 5, 'max': 50}, 'S': {'min': 5, 'max': 20}}}
