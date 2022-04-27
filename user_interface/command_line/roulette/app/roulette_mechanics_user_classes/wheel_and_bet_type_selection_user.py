from games.roulette.app.roulette_mechanics_action_classes.wheel_and_bet_type_selection import WheelAndBetTypeSelector
from user_interface.command_line.roulette.definitions.wheel_parameters_and_defns_user import wheel_options_text
from user_interface.command_line.roulette.definitions.bet_type_defns_user import bet_cats_and_types, \
    bet_cat_options_text, bet_type_options_text
from user_interface.command_line.roulette.definitions.bet_type_defns_user import USER_BET_TYPES
from user_interface.command_line.roulette.definitions.wheel_parameters_and_defns_user import USER_WHEEL_TYPES
from user_interface.command_line.roulette.definitions.bet_type_defns_user import BetTypeOptionsUser
from user_interface.command_line.roulette.definitions.wheel_parameters_and_defns_user import WheelOptionsUser
from games.roulette.definitions.bet_parameters import BetParameters

class WheelAndBetTypeSelectorUser(WheelAndBetTypeSelector):
    """class to allow users to select the type of bet to place
    note note yet to place the bet"""

    def choose_playing_wheel(self, wheel_look_up=WheelOptionsUser) -> (str, USER_WHEEL_TYPES):
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
            except AttributeError:
                print("Invalid wheel choice, please try again")


    def choose_bet(self, wheel_id: str) -> USER_BET_TYPES:
        """
        Method that navigates the user to choose their bet, by applying the choose_playing_wheel,
        choose_bet_category and then the choose_bet_type methods below.
        """
        bet_cat = self.choose_bet_category(wheel_id=wheel_id)
        bet_type = self.choose_bet_type(wheel_name=wheel_id, bet_cat=bet_cat)
        return bet_type

    # Lower level methods called during the choose_bet method
    @staticmethod
    def choose_bet_category(wheel_id: str) -> str:
        while True:
            bet_cat = input("What category of bet would you like to place?"
                            f"\n{bet_cat_options_text[wheel_id]}\n--->").upper()
            if bet_cat in list(bet_cats_and_types[wheel_id].keys()):
                return bet_cat
            else:
                print("Not a valid bet category, try again")

    def choose_bet_type(self, wheel_name: str, bet_cat: str) -> USER_BET_TYPES:
        bet_type_text = getattr(getattr(getattr(BetParameters, wheel_name), bet_cat), bet_cat_options_text)
        while True:
            bet_type_id = input("What type of bet would you like to place?"
                                f"\n{bet_type_options_text[wheel_name][bet_cat]}\n--->").upper()
            if bet_type_id in bet_cats_and_types[wheel_name][bet_cat]:
                bet_type = self.get_bet_type_from_bet_type_id(bet_type_id)
                return bet_type
            else:
                print("Not a valid bet type, try again")
