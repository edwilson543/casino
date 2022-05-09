from games.roulette.app.roulette_wheel_base_class import RouletteWheel, wheel_spin_return, RouletteWheelParameters
from games.roulette.constants.game_constants import RouletteGameParameters
from dataclasses import dataclass
from time import sleep
from numpy import array2string


##########
# Data class for defining the RouletteWheelUser Parameters
# i.e. the new instance attributes added to the RouletteWheelUser class
##########
@dataclass
class RouletteWheelParametersUser(RouletteWheelParameters):
    board_string_rep: str


##########
# Base class for defining the command line UI Roulette wheel
##########

class RouletteWheelUser(RouletteWheel):
    def __init__(self,
                 parameters: RouletteWheelParameters):
        """
        Added instance attributes:
        colour_options_text: a mapping of colour id (e.g. 'R') to each colour (e.g. 'red')
        colour_options_text: a string used to get user input on what colour they'd like to bet on
        """
        super().__init__(parameters)

    def user_spin(self) -> wheel_spin_return:
        """Low level method just to get the user to type spin in the game flow"""
        while True:
            user_ready = input("Type 'SPIN' to spin the wheel!\n--->").upper()
            if user_ready != "SPIN":
                print("Please try spinning the wheel again.")
                continue
            else:
                spin_outcome = self.spin()
                sleep(RouletteGameParameters.pause_durations.short)
                print("Wheel spinning...")
                sleep(RouletteGameParameters.pause_durations.medium)
                print(f"Ball has landed on {spin_outcome.number_return}, ({spin_outcome.colour_return.name})!")
                sleep(RouletteGameParameters.pause_durations.short)
                return spin_outcome

    def generate_board_string_rep(self) -> str:
        """Method to give a human comprehensible string representation of the Roulette board"""
        board_string_rep = "The board shape is as follows:\n"
        for row in range(0, self.parameters.board.shape[0]):  # iterate over number of array rows
            row_rep = array2string(self.parameters.board[row], separator="|")[2:][:-1].strip(" ") + "\n"
            board_string_rep += row_rep
        return board_string_rep[:-1]  # Remove the final extra line of the board representation
