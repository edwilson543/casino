from games.roulette.app.roulette_wheel_base_class import RouletteWheel, wheel_spin_return, RouletteWheelParameters
from games.roulette.constants.game_constants import AllGameParameters
from dataclasses import dataclass
from time import sleep

##########
# Data class for defining the RouletteWheelUser Parameters
# i.e. the new instance attributes added to the RouletteWheelUser class
##########
@dataclass
class RouletteWheelParametersUser(RouletteWheelParameters):
    colour_ids: dict
    colour_options: str

##########
# Base class for defining the command line UI Roulette wheel
##########

class RouletteWheelUser(RouletteWheel):
    def __init__(self,
                 wheel_name: str,
                 slots: dict,
                 bias_colour: str,
                 colour_ids: dict,
                 colour_options: str):
        """
        Added instance attributes:
        colour_ids: a mapping of colour id (e.g. 'R') to each colour (e.g. 'red')
        colour_options: a string used to get user input on what colour they'd like to bet on
        """
        super().__init__(wheel_name, slots, bias_colour)
        self.colour_ids = colour_ids
        self.colour_options = colour_options

    def user_number_options_text(self):
        """
        Returns: text string describing the numbers of the roulette wheel
        Example output form: '0 to 36 (inclusive)'
        Note this would need to change if defining a roulette wheel which skips numbers
        """
        min_number = min(list(set(self.slots.keys())))
        max_number = max(list(set(self.slots.keys())))
        return f"{min_number} to {max_number} (inclusive)"

    def user_number_options_range(self):
        """Returns a range which specifies the valid number choices"""
        min_number = min(list(set(self.slots.keys())))
        max_number = max(list(set(self.slots.keys())))
        return range(min_number, max_number + 1)

    ##########
    # Lower level methods called in evaluate_user_bet
    ##########
    def user_spin(self) -> wheel_spin_return:
        """Low level method just to get the user to type spin in the game flow"""
        while True:
            user_ready = input("Type 'SPIN' to spin the wheel!\n--->").upper()
            if user_ready != "SPIN":
                print("Please try spinning the wheel again.")
                continue
            else:
                spin_outcome = self.spin()
                sleep(AllGameParameters.pause_durations.short)
                print("Wheel spinning...")
                sleep(AllGameParameters.pause_durations.medium)
                print(f"Ball has landed on {spin_outcome.number_return}, ({spin_outcome.colour_return})!")
                sleep(AllGameParameters.pause_durations.short)
                return spin_outcome


