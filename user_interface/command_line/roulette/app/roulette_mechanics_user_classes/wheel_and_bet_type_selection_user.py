from games.roulette.app.roulette_mechanics_action_classes.wheel_and_bet_type_selection import WheelAndBetTypeSelector
from user_interface.command_line.roulette.definitions.wheel_defns_user import wheel_options_text
from user_interface.command_line.roulette.definitions.bet_type_defns_user import bet_cats_and_types, \
    bet_cat_options_text, bet_type_options_text
from user_interface.command_line.roulette.definitions.bet_type_defns_user import USER_BET_TYPES
from user_interface.command_line.roulette.definitions.wheel_defns_user import USER_WHEEL_TYPES
from user_interface.command_line.roulette.definitions.bet_type_defns_user import BetTypeOptionsUser


class WheelAndBetTypeSelectorUser(WheelAndBetTypeSelector):
    """class to allow users to select the type of bet to place
    note note yet to place the bet"""

    def __init__(self,
                 wheel_look_up: dict,
                 bet_type_look_up=BetTypeOptionsUser):
        super().__init__(wheel_look_up, bet_type_look_up)

    def choose_playing_wheel(self) -> (str, USER_WHEEL_TYPES):
        """
        Method to navigate the user through the wheel options and return a live wheel object.
        Returns: the wheel_id, and the associated relevant subclass of RouletteWheel defining that wheel
        """
        while True:
            wheel_choice_id = input("What wheel would you like to play on?\n"
                                    f"{wheel_options_text}\n--->").upper()  # upper to allow for lower case
            if wheel_choice_id in list(self.wheel_look_up):
                wheel_choice_object = self.get_wheel_from_wheel_id(wheel_choice_id)
                return wheel_choice_id, wheel_choice_object
            else:
                print("Invalid wheel choice, please try again")

    def choose_bet(self, wheel_id: str) -> USER_BET_TYPES:
        """
        Method that navigates the user to choose their bet, by applying the choose_playing_wheel,
        choose_bet_category and then the choose_bet_type methods below.
        """
        bet_cat = self.choose_bet_category(wheel_id=wheel_id)
        bet_type = self.choose_bet_type(wheel_id=wheel_id, bet_cat=bet_cat)
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

    def choose_bet_type(self, wheel_id: str, bet_cat: str) -> USER_BET_TYPES:
        while True:
            bet_type_id = input("What type of bet would you like to place?"
                                f"\n{bet_type_options_text[wheel_id][bet_cat]}\n--->").upper()
            if bet_type_id in bet_cats_and_types[wheel_id][bet_cat]:
                bet_type = self.get_bet_type_from_bet_type_id(bet_type_id)
                return bet_type
            else:
                print("Not a valid bet type, try again")
