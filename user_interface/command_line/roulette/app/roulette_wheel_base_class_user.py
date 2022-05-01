from games.roulette.app.roulette_wheel_base_class import RouletteWheel, wheel_spin_return, RouletteWheelParameters
from games.roulette.constants.game_constants import AllGameParameters, Colour
from dataclasses import dataclass
from time import sleep
from numpy import array, array2string


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
                 wheel_name: str,
                 slots: dict,
                 bias_colour: Colour,
                 board: array):
        """
        Added instance attributes:
        colour_options_text: a mapping of colour id (e.g. 'R') to each colour (e.g. 'red')
        colour_options_text: a string used to get user input on what colour they'd like to bet on
        """
        super().__init__(wheel_name, slots, bias_colour, board)

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
                print(f"Ball has landed on {spin_outcome.number_return}, ({spin_outcome.colour_return.name})!")
                sleep(AllGameParameters.pause_durations.short)
                return spin_outcome

    def generate_board_string_rep(self) -> str:
        """Method to give a human comprehensible string representation of the Roulette board"""
        board_string_rep = ""
        for row in range(0, board.shape[0]):  # iterate over number of array rows
            row_rep = array2string(board[row], separator="|")[2:][:-1].strip(" ")
            board_string_rep += row_rep
        return board_string_rep
