from games.players.player_database_manager import PlayerDatabaseManager
from games.player_base_class import PlayerType, PLAYER_TYPES
from games.all_game_constants.player_constants import PlayerParameterRestrictions
from user_interface.command_line.games.player_base_class_user import PlayerUser
import sys
import functools
from root_directory import ROOT_DIRECTORY
from pathlib import Path


##########
# Password protection decorator to be called when accessing players
##########
def password_protected(access_player_func):
    n_attempts: int = PlayerParameterRestrictions.password_parameters.allowed_password_attempts

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


class PlayerDatabaseInteractionsUser(PlayerDatabaseManager):
    """
    Class to initiate the roulette game.
    Methods to get the user to initiate the game, set their initial deposit, and choose the wheel they want to play on
    """

    def __init__(self,
                 player_object: PLAYER_TYPES = PlayerUser,
                 player_data_directory_path: Path = ROOT_DIRECTORY / "games" / "players" / "player_data",
                 player_datafile_name: str = "player_data.json",
                 guest_datafile_name: str = "guest_data.json"):
        super().__init__(player_object,
                         player_data_directory_path,
                         player_datafile_name,
                         guest_datafile_name)

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
                    guest_player: PlayerUser = self.load_player(player_username="guest")
                    return guest_player, PlayerType.GUEST_PLAYER
                elif player_type == PlayerType.EXISTING_PLAYER:
                    existing_player: PlayerUser = self.access_player()
                    existing_player.login_message()
                    existing_player.set_session_end_time_to_now()
                    return existing_player, PlayerType.EXISTING_PLAYER
                elif player_type == PlayerType.NEW_PLAYER:
                    new_player: PlayerUser = self.create_player_user()
                    return new_player, PlayerType.NEW_PLAYER
            except ValueError and AttributeError:
                print(f"{player_type_id} not a valid option, please try again")

    ##########
    # Lower level method called during the access_existing_or_new_player method
    ##########
    @password_protected
    def access_player(self) -> PlayerUser:
        """Method to set the active_player within the game"""
        while True:
            username = input(f"What is your username?\n--->").lower()
            try:
                existing_player = self.load_player(player_username=username)
                return existing_player
            except KeyError:
                print(f"No user with username: {username} found. Please try again.")

    def create_player_user(self) -> PlayerUser:
        name = self.create_name()
        username = self.create_username()
        password = self.create_password()
        print(f"Welcome, {name}! Your account has been created!")
        self.create_player(name=name, player_username=username, password=password)
        created_player = self.load_player(player_username=username)
        return created_player

    ##########
    # Lower level method called during the create_player_user method
    ##########
    def create_name(self) -> str:
        """
        Method to get the user to enter their name and check that it meets the criteria.
        Returns: The player's name, as long as it's legit
        """
        while True:
            proposed_name = input(f"Please enter your name\n--->")
            if self.name_meets_criteria_check(proposed_name=proposed_name):
                return proposed_name
            else:
                print(f"{proposed_name} name not a valid name choice, please try again.\n"
                      f"Names may not contain the following characters: "
                      f"{PlayerParameterRestrictions.name_parameters.disallowed_characters}")

    def create_username(self) -> str:
        """
        Method to get the user to enter a desired username and check that it meets the criteria.
        Returns: the player's desired username, as long as it's legit.
        """
        while True:
            proposed_username = input("Please enter a new username\n--->")
            if self.username_exists_check(player_username=proposed_username):
                print(f"{proposed_username} already taken! Please enter a new username")
                continue
            elif not self.username_meets_criteria_check(proposed_username=proposed_username):
                print(f"{proposed_username} is not a valid username! "
                      f"Usernames may not contain the following characters: "
                      f"{PlayerParameterRestrictions.username_parameters.disallowed_characters}, and "
                      f"must be at least: {PlayerParameterRestrictions.username_parameters.minimum_length} characters")
                continue
            else:
                return proposed_username

    def create_password(self) -> str:
        """
        Method to get the user to enter and then re-enter a valid password
        Returns: the player's desired password, as long as it's legit
        """
        min_password_length = PlayerParameterRestrictions.password_parameters.minimum_length
        while True:
            proposed_password = input(f"Please enter a password. Passwords must have at least:"
                                      f" {min_password_length} characters.\n--->")
            if not self.password_meets_criteria_check(proposed_password=proposed_password):
                print(f"Password does not meet minimum length criteria of {min_password_length} characters")
                continue
            else:
                re_entered_password = input("Please re-enter password.\n--->")
                if proposed_password == re_entered_password:
                    return proposed_password
                else:
                    print("Passwords do not match, please try again")
                    continue
