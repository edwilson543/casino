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
class PauseDurations:
    short = 0.5
    medium = 1
    long = 2


@dataclass(frozen=True)
class AllGameParameters:
    deposit_parameters = DepositParameters
    top_up_parameters = TopUpParameters
    pause_durations = PauseDurations
