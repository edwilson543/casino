"""
Module defining the WheelAndBetConstructorUser object which allows users to interact with the WheelAndBetConstructor
object, and instantiate wheels and bets for use in the Roulette game.
"""

# Standard library imports
from enum import Enum

# Local application imports
from games.roulette.app.single_player_roulette.wheel_and_bet_construction import WheelAndBetConstructor
from games.roulette.app.roulette_wheel_base_class import WHEEL_TYPES
from games.roulette.constants.wheel_constants import WheelIds, get_wheel_options_text, WheelParameters
from games.roulette.constants.bet_constants import BetTypeIds, WheelBetParameters

# Local application UI imports
from user_interface.games.roulette.app.roulette_bet_base_class_user import USER_BET_TYPES
from user_interface.games.roulette.definitions.bet_type_defns_user import BetTypeOptionsUser
from user_interface.games.roulette.app.roulette_wheel_base_class_user import RouletteWheelUser


class WheelAndBetConstructorUser(WheelAndBetConstructor):
    """Class to allow users to select the type of wheel they want to play on, and type of bet to place"""

    def __init__(self,
                 wheel_parameters_look_up: Enum = WheelParameters,
                 wheel_construction_object=RouletteWheelUser,
                 bet_parameters_look_up=WheelBetParameters,
                 bet_object_look_up=BetTypeOptionsUser):
        super().__init__(wheel_parameters_look_up, wheel_construction_object, bet_parameters_look_up, bet_object_look_up)

    def choose_playing_wheel(self) -> WHEEL_TYPES:
        """
        Method to navigate the user through the wheel options and return a live wheel object.
        Returns: the wheel that the game will be played on
        """
        while True:
            wheel_choice_id = input("What wheel would you like to play on?\n"
                                    f"{get_wheel_options_text()}\n--->").upper()  # upper to allow for lower case
            try:
                wheel_name = WheelIds(wheel_choice_id).name
                wheel = self.get_wheel_from_wheel_name(wheel_name=wheel_name)
                return wheel
            except ValueError:
                print("Invalid wheel choice, please try again")

    def choose_bet_type(self, wheel_name: str) -> USER_BET_TYPES:
        """
        Method that navigates the user to choose their bet type, and then calls super class method to instantiate it.
        """
        bet_types_text = getattr(WheelBetParameters, wheel_name).construct_wheel_bet_options_prompt()
        while True:
            bet_type_id = input("What type of bet would you like to place?\n"
                                f"{bet_types_text}\n--->").upper()
            try:
                bet_type_name = BetTypeIds(bet_type_id).name
                bet_type = self.get_bet_type_from_bet_type_name(wheel_name=wheel_name, bet_type_name=bet_type_name)
                return bet_type
            except ValueError:
                print("Invalid bet choice, please try again")
