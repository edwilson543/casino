from games.players.player_interactions import PlayerInteractions
from games.player_base_class import PlayerType
from games.roulette.constants.game_constants import AllGameParameters
from user_interface.command_line.games.player_base_class_user import PlayerUser
import sys
import functools


##########
# Password protection decorator to be called when accessing players
##########
def password_protected(access_player_func):
    n_attempts = AllGameParameters.allowed_password_attempts

    @functools.wraps(access_player_func)
    def wrapper_password_protected(*args, **kwargs):
        player: PlayerUser = access_player_func(*args, **kwargs)  # this will be a call to access a player
        for k in range(n_attempts):
            password = input(f"Please enter your password.\n--->")
            if password == player.password:
                return player
            elif k == n_attempts - 1:
                sys.exit("Too many invalid attempts, your session has been terminated.")
            else:
                attempts_remaining = n_attempts - k - 1
                print(f"Incorrect password - please try again.\nYou have {attempts_remaining} attempts remaining")
        return player

    return wrapper_password_protected


class PlayerInteractionsUser(PlayerInteractions):
    """
    Class to initiate the roulette game.
    Methods to get the user to initiate the game, set their initial deposit, and choose the wheel they want to play on
    """

    def __init__(self,
                 player_object=PlayerUser,
                 player_datafile: str = "player_data.json"):  # TODO find a better way of doing this
        super().__init__(player_object, player_datafile)

    def all_games_set_up(self) -> PlayerUser:
        active_player, player_type = self.access_existing_or_new_player()
        active_player.make_initial_deposit_or_top_up(player_type=player_type)
        active_player.set_active_session_initial_pot_and_time()
        return active_player

    def access_existing_or_new_player(self) -> (PlayerUser, PlayerType):
        """
        Method to determine whether the user wants to access an existing player, or create a new player
        Returns:
        PlayerUser - an instantiated PlayerUser based on the player data
        PlayerType - a member of the PlayerType Enum, determining whether this is a new, existing or guest player - this
        affects some of the initial game flow.
        """
        print("Welcome to Balint and Ed's online casino!")
        # and allow functionality choose what game they'd like to play
        while True:
            player_type_id = input(
                "Would you like to play as a new or as an existing player?\n"
                "[G]uest, [E]xisting, [N]ew\n--->").upper()
            try:
                player_type = PlayerType(player_type_id)
                if player_type == PlayerType.GUEST_PLAYER:
                    guest_player = super().load_player(player_username="guest")
                    return guest_player, player_type
                elif player_type == PlayerType.EXISTING_PLAYER:
                    existing_player = self.access_player(desired_player_object=PlayerUser)
                    existing_player.login_message()
                    existing_player.set_session_end_time_to_now()
                    return existing_player, player_type
                elif player_type == PlayerType.NEW_PLAYER:
                    print("New player functionality not built yet")  # TODO update when ready
                    continue
            except ValueError and AttributeError:
                print(f"{player_type_id} not a valid option, please try again")

    @staticmethod
    def create_player_user(self) -> PlayerUser:  # TODO define this, using super class method
        # need to keep the step of forcing the player to top up within player creation
        pass

    ##########
    # Lower level method called during the access existing or new player
    ##########
    @password_protected
    def access_player(self) -> PlayerUser:
        """Method to set the active_player within the game"""
        while True:
            username = input(f"What is your username?\n--->").lower()
            try:
                existing_player = super().load_player(player_username=username)
                return existing_player
            except KeyError:
                print(f"No user with username: {username} found. Please try again.")
