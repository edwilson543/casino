from dataclasses import dataclass


#################
# Game parameters
#################
@dataclass(frozen=True)
class DepositParameters:
    min_deposit = 100
    deposit_multiples = 10


@dataclass(frozen=True)
class TopUpParameters:
    min_top_up = 50
    top_up_multiples = 10
    threshold_for_top_up_prompt = 50
    low_pot_forced_top_up = 10


@dataclass(frozen=True)
class PauseDurations:  # UI focused but bit annoying to have in its own file for now
    short = 0.5
    medium = 1
    long = 2


@dataclass(frozen=True)
class AllGameParameters:
    deposit_parameters = DepositParameters
    top_up_parameters = TopUpParameters
    pause_durations = PauseDurations

##########
# Colours on the Roulette wheel/ board
##########
class Colours:
    RED = "R"  # make sure RHS is unique
    # TODO finish and implement in definitions below
