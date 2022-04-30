from games.roulette.app.roulette_mechanics_action_classes.wheel_and_bet_type_selection import WheelAndBetTypeConstructor
from games.roulette.app.roulette_wheel_base_class import WHEEL_TYPES
from user_interface.command_line.roulette.definitions.bet_type_defns_user import USER_BET_TYPES
from games.roulette.constants.wheel_constants import WheelIds
from games.roulette.constants.bet_constants import WheelBetParameters

from user_interface.command_line.roulette.definitions.bet_type_defns_user import BetTypeOptionsUser
from user_interface.command_line.roulette.constants.wheel_constants_user import WheelParametersUser, wheel_options_text
from user_interface.command_line.roulette.app.roulette_wheel_base_class_user import RouletteWheelUser
from enum import Enum


class WheelAndBetTypeSelectorUser(WheelAndBetTypeConstructor):
    """Class to allow users to select the type of wheel they want to play on, and type of bet to place"""

    def __init__(self,
                 wheel_parameters_look_up: Enum = WheelParametersUser,
                 construction_object=RouletteWheelUser):
        super().__init__(wheel_parameters_look_up, construction_object)

    def choose_playing_wheel(self) -> WHEEL_TYPES:
        """
        Method to navigate the user through the wheel options and return a live wheel object.
        Returns: the wheel that the game will be played on
        """
        while True:
            wheel_choice_id = input("What wheel would you like to play on?\n"
                                    f"{wheel_options_text}\n--->").upper()  # upper to allow for lower case
            try:
                wheel_name = WheelIds(wheel_choice_id).name
                wheel = self.get_wheel_from_wheel_name(wheel_name=wheel_name)
                return wheel
            except ValueError:
                print("Invalid wheel choice, please try again")

    def choose_bet_type(self, wheel_name: str) -> USER_BET_TYPES:
        """
        Method that navigates the user to choose their bet, by applying the choose_playing_wheel,
        choose_bet_category and then the choose_bet_type methods below.
        """
        bet_types_text = getattr(WheelBetParameters, wheel_name).construct_wheel_bet_options_prompt()
        while True:
            bet_type_id = input("What type of bet would you like to place?\n"
                                f"{bet_types_text}\n--->").upper()
            try:
                bet_choice = self.get_bet_type_from_bet_type_id(bet_type_id=bet_type_id,
                                                                bet_type_look_up=BetTypeOptionsUser)
                return bet_choice
            except ValueError:
                print("Invalid wheel choice, please try again")
