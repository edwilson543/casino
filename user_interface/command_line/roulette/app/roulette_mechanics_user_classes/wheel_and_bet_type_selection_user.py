from games.roulette.app.roulette_mechanics_action_classes.wheel_and_bet_type_selection import WheelAndBetTypeSelector
from user_interface.command_line.roulette.definitions.wheel_defns_user import wheel_options_text
from user_interface.command_line.roulette.definitions.bet_type_defns_user import USER_BET_TYPES
from user_interface.command_line.roulette.definitions.wheel_defns_user import USER_WHEEL_TYPES
from user_interface.command_line.roulette.definitions.bet_type_defns_user import BetTypeOptionsUser
from user_interface.command_line.roulette.definitions.wheel_defns_user import WheelOptionsUser
from games.roulette.constants.bet_constants import WheelBetParameters


class WheelAndBetTypeSelectorUser(WheelAndBetTypeSelector):
    """class to allow users to select the type of bet to place
    note note yet to place the bet"""

    def choose_playing_wheel(self, wheel_look_up=WheelOptionsUser) -> USER_WHEEL_TYPES:
        """
        Method to navigate the user through the wheel options and return a live wheel object.
        Returns: the wheel_id, and the associated relevant subclass of RouletteWheel defining that wheel
        """
        while True:
            wheel_choice_id = input("What wheel would you like to play on?\n"
                                    f"{wheel_options_text}\n--->").upper()  # upper to allow for lower case
            try:
                wheel_choice = self.get_wheel_from_wheel_id(wheel_id=wheel_choice_id, wheel_look_up=wheel_look_up)
                return wheel_choice
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
