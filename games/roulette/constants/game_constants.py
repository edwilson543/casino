from dataclasses import dataclass
from enum import Enum


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
class RouletteGameParameters:
    deposit_parameters = DepositParameters
    top_up_parameters = TopUpParameters
    pause_durations = PauseDurations


##########
# Colours on the Roulette wheel/ board
##########
class Colour(Enum):  # make sure RHS is unique
    RED = "R"
    BLACK = "B"
    GREEN = "G"
    BLUE = "BL"


class ColourPrompts(Enum):  # make sure matches ID above
    RED = "[R]ed"
    BLACK = "[B]lack"
    GREEN = "[G]reen"
    BLUE = "[BL]ue"
