from Games.games_base_classes import Player
from Games.Roulette.definitions.navigation_defns import navigation_text, navigation_options
from Games.Roulette.definitions.navigation_defns import navigation_text_low_funds, navigation_options_low_funds
from user_interface.command_line.all_games.player_interactions_user import PlayerUserInteractions
from Games.Roulette.definitions.game_parameters import deposit_parameters
from Games.Roulette.definitions.game_parameters import top_up_parameters
import sys


class RouletteContinuationUser(PlayerUserInteractions):
    """
    Class to keep the game going until the user runs out of money or quits.
    We'll need to expand to include play on same wheel, new bet type.
    The purpose will be to map users to where they need to be within the existing mechanics.
    """

    def __init__(self,
                 stake: int,
                 min_deposit: int = deposit_parameters['min_deposit'],
                 deposit_multiples: int = deposit_parameters['deposit_multiples'],
                 min_top_up: int = top_up_parameters['min_top_up'],
                 top_up_multiples: int = top_up_parameters['top_up_multiples']):
        super().__init__(min_deposit, deposit_multiples, min_top_up, top_up_multiples)
        self.stake = stake

    def keep_playing(self, active_player: Player):
        while True:
            active_player.get_profit_report()  # to be updated with more relavant method
            proceed = input(f"Would you like to continue playing?\n[Y]es, [N]o\n--->").upper()
            if proceed == "N":
                sys.exit(f"Game over.\nYour final pot is £{active_player.active_pot}\n")  # make more relevant
            elif proceed == 'Y':
                break
            else:
                print(f"{proceed} not a valid command, please try again")

    def choose_navigation(self, active_player: Player) -> str:
        if self.stake <= active_player.active_pot:
            nav_text = navigation_text
            nav_options = navigation_options
        else:
            nav_text = navigation_text_low_funds
            nav_options = navigation_options_low_funds
        while True:
            next_step = input(f"What would you like to do?\n{nav_text}\n--->").upper()
            if next_step in nav_options:
                return next_step
            else:
                print(f"{next_step} not a valid command, please try again")
