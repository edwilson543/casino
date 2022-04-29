from games.player_base_class import PlayerType
from user_interface.command_line.games.player_base_class_user import PlayerUser
from user_interface.command_line.games.players.existing_players_user import ExistingPlayersUser
import sys
import functools


##########
# Functions to access players, requiring user input of password
##########

def password_protected(n_attempts):
    def decorator_password_protected(func):
        @functools.wraps(func)
        def wrapper_password_protected(*args, **kwargs):
            desired_player = func(*args, **kwargs)
            for k in range(n_attempts):
                password = input(f"Please enter your password.\n--->")
                if password == desired_player.password:
                    print(f"Welcome back, {desired_player.name}!")
                    return desired_player
                elif k == n_attempts - 1:
                    sys.exit("Too many invalid attempts, your session has been terminated.")
                else:
                    attempts_remaining = n_attempts - k - 1
                    print(f"Incorrect password - please try again.\nYou have {attempts_remaining} attempts remaining")
            return desired_player

        return wrapper_password_protected

    return decorator_password_protected


@password_protected(n_attempts=5)
def access_player():
    """Method to set the active_player within the game"""
    while True:
        username = input(f"What is your username?\n--->").lower()
        try:
            existing_player = getattr(ExistingPlayersUser, username).value
            return existing_player
        except AttributeError or ValueError:
            print(f"No user with username: {username} found. Please try again.")


class PlayerInteractionsUser:  # TODO make this a subclass of PlayerInteractions
    """
    Class to initiate the roulette game.
    Methods to get the user to initiate the game, set their initial deposit, and choose the wheel they want to play on
    """

    def all_games_set_up(self) -> PlayerUser:
        active_player = self.access_existing_or_new_player()
        active_player.set_active_session_initial_pot_and_time()
        active_player.make_initial_deposit_or_top_up()
        return active_player

    @staticmethod
    def access_existing_or_new_player() -> PlayerUser:
        """Method to determine whether the user wants to access an existing player, or create a new player"""
        print("Welcome to Balint and Ed's online casino!")
        # and allow functionality choose what game they'd like to play
        while True:
            player_type_id = input(
                "Would you like to play as a new or as an existing player?\n"
                "[G]uest, [E]xisting, [N]ew\n--->").upper()
            try:
                player_type = PlayerType(player_type_id)
                if player_type == PlayerType.GUEST_PLAYER:
                    return ExistingPlayersUser.guest.value
                elif player_type == PlayerType.EXISTING_PLAYER:
                    return access_player()
                elif player_type == PlayerType.NEW_PLAYER:
                    print("New player functionality not built yet")
                    continue
            except ValueError and AttributeError:
                print(f"{player_type_id} not a valid option, please try again")

    @staticmethod
    def create_player_user(self) -> PlayerUser:  # TODO define this, using super class method
        # maybe also we want want the creation and the return all in one method
        pass
