from games.player_base_class import Player
from user_interface.command_line.roulette.definitions.navigation_defns import post_spin_navigation_text, post_spin_navigation_options
from user_interface.command_line.roulette.definitions.navigation_defns import post_spin_navigation_text_low_funds, \
    post_spin_navigation_options_low_funds
from user_interface.command_line.all_games.player_interactions_user import PlayerInteractionsUser
from games.roulette.definitions.game_parameters import deposit_parameters
from games.roulette.definitions.game_parameters import top_up_parameters


class RouletteContinuationUser(PlayerInteractionsUser):
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

    @staticmethod
    def keep_playing(active_player: Player):
        while True:
            active_player.get_active_session_report()
            proceed = input(f"Would you like to continue playing?\n[Y]es, [N]o\n--->").upper()
            if proceed == "N":
                active_player.end_session()
            elif proceed == 'Y':
                break
            else:
                print(f"{proceed} not a valid command, please try again")

    def choose_navigation(self, active_player: Player) -> str:
        if self.stake < active_player.active_pot:
            nav_text = post_spin_navigation_text
            nav_options = post_spin_navigation_options
        else:
            nav_text = post_spin_navigation_text_low_funds
            nav_options = post_spin_navigation_options_low_funds
        while True:
            next_step = input(f"What would you like to do?\n{nav_text}\n--->").upper()
            if next_step in nav_options:
                return next_step
            else:
                print(f"{next_step} not a valid command, please try again")
