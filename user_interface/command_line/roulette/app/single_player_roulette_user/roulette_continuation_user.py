from user_interface.command_line.games.player_base_class_user import PlayerUser
from enum import Enum


##########
# Data class to store the different navigation options
##########

class NavigationOptionIDs(Enum):
    CHANGE_WHEEL = "W"
    CHANGE_BETS = "B"
    REPEAT_BETS = "R"


class NavigationOptionsPrompt(Enum):
    REPEAT_BETS = "[R]epeat bets"
    CHANGE_BETS = "[B]ets change"
    CHANGE_WHEEL = "[W]heel change"


class NavigationOptionRank(Enum):
    CHANGE_WHEEL = 0
    CHANGE_BETS = 1
    REPEAT_BETS = 2


class RouletteContinuationUser:
    """
    Class to keep the game going until the user runs out of money or quits.
    We'll need to expand to include play on same wheel, new bet type.
    The purpose will be to map users to where they need to be within the existing mechanics.
    """

    def __init__(self, stake: int):
        self.stake = stake

    @staticmethod
    def keep_playing(active_player: PlayerUser):
        while True:
            active_player.get_active_session_report()
            proceed = input(f"Would you like to continue playing?\n[Y]es, [N]o\n--->").upper()
            if proceed == "N":
                active_player.end_session_user()
            elif proceed == 'Y':
                break
            else:
                print(f"{proceed} not a valid command, please try again")

    def choose_navigation(self, active_player: PlayerUser) -> int:
        if self.stake < active_player.active_pot:
            navigation_text = "What would you like to do?\n" + \
                              ", ".join([prompt.value for prompt in NavigationOptionsPrompt])  # allow all options
            navigation_options = [ID.value for ID in NavigationOptionIDs]
        else:  # i.e. user can't afford to repeat the given bets
            navigation_text = "What would you like to do?\n" + \
                              NavigationOptionsPrompt.CHANGE_BETS.value + ", " + \
                              NavigationOptionsPrompt.CHANGE_WHEEL.value
            navigation_options = [NavigationOptionIDs.CHANGE_BETS.value, NavigationOptionIDs.CHANGE_WHEEL.value]
        while True:
            next_step = input(f"{navigation_text}\n--->").upper()
            if next_step in navigation_options:
                next_step_name = NavigationOptionIDs(next_step).name
                next_step_value = getattr(NavigationOptionRank, next_step_name).value
                return next_step_value
            else:
                print(f"{next_step} not a valid command, please try again")
