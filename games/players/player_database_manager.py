from games.all_game_constants.player_constants import PlayerParameterRestrictions
from games.players.player_base_class import Player, PLAYER_TYPES
from games.all_game_constants.root_directory import ROOT_DIRECTORY
from pathlib import Path
import logging
from datetime import datetime
import json


class PlayerDatabaseManager:
    def __init__(self,
                 player_object: PLAYER_TYPES = Player,
                 player_data_directory_path: Path = ROOT_DIRECTORY / "data" / "player_data",
                 player_datafile_name: str = "player_data.json",
                 guest_datafile_name: str = "guest_data.json"):
        """
        Parameters:
        ----------
        player_object: the type of player object to be instantiated from their attributes in storage.
        This will currently either be just Player or PlayerUser.

        player_data_directory_path: A Path object that specifies where the player and guest data is / will be stored,
        relative to the ROOT_DIRECTORY. This can easily be changed from the default if a user would like to store their
        player data elsewhere.

        player_data_file_name: Name of the player datafile - note that new player data files could be created by
        changing this string, although the JSON extension must always be used.
        The player datafile with the default name and default path is in the .gitignore, however will automatically
        populate when a new user creates an account on their own device, as an empty JSON dictionary, which then will
        get filled with their data.

        guest_datafile_name: Name of the guest data file - this is NOT on the .gitignore, as all users will need it to
        be able to play as a guest
        """
        self.player_object = player_object
        self.player_data_directory_path = player_data_directory_path
        self.player_datafile_name = player_datafile_name
        self.guest_datafile_name = guest_datafile_name

    def load_player(self, player_username: str) -> PLAYER_TYPES:
        """
        Method to read the JSON file storing player data, retrieve the relevant player's data and then
        instantiate a player as an instance of self.player_object (using decode_player).
        JSON database -> player's JSON dict -> python dict (self.decode_player) -> instantiate player as a Player object
        Parameters: player_username: the player_username of the player to be retrieved. Note that if the
        guest player_username is passed, then the data_path will just point to the test_guest_data.json
        Returns: live_player: an instance of the desired Player subclass
        """
        data_path = self.get_data_path(player_username=player_username)
        with open(data_path, "r") as player_data_file:
            try:
                all_player_data_dict: dict = json.load(player_data_file)
                encoded_player_data = all_player_data_dict[player_username]
                live_player = self.decode_player(serialised_attributes_dict=encoded_player_data)
                logging.info(f"Player username: {player_username} was retrieved from the database.")
                return live_player
            except KeyError:
                logging.exception("Exception occurred when retrieving from player database.")
                raise KeyError("load_player method attempted to load a player not found in player database.")

    def upload_player(self, player: PLAYER_TYPES) -> None:
        """
        Method to upload a player to the JSON data storage.
        For new player's this represents creation, for existing player's this just updates their data.
        Player object -> python dict (self.encode_player) -> JSON dict -> insert into JSON database
        Parameters: player - the player being stored
        """
        if player.username == "guest":
            pass
        else:
            data_path = self.get_data_path(player_username=player.username)
            with open(data_path, "r") as player_data_file:
                all_player_data_dict: dict = json.load(player_data_file)
            all_player_data_dict[player.username] = self.encode_player(player=player)
            with open(data_path, "w") as player_data_file:
                json.dump(all_player_data_dict, player_data_file)
            logging.info(f"Player username: {player.username} was uploaded back to the database.")

    def create_player(self, name, player_username, password) -> None:
        """
        Method to check whether or not a given player_username already exists,
        and then upload them to the database if not.
        """
        if self.username_exists_check(player_username=player_username):
            raise ValueError(f"create_player called with player_username: {player_username} which is already in use.")
        elif not self.username_meets_criteria_check(proposed_username=player_username):
            raise ValueError("create_player method in player_database_manager attempted to create a player"
                             f" with invalid username: {player_username}")
        elif not self.password_meets_criteria_check(proposed_password=password):
            raise ValueError("create_player method in player_database_manager attempted to create a player"
                             f" with invalid password: {password}")
        elif not self.name_meets_criteria_check(proposed_name=name):
            raise ValueError("create_player method in player_database_manager attempted to create a player"
                             f" with invalid name: {name}")
        else:
            player = self.player_object(name=name, username=player_username, password=password)  # Other params default
            self.upload_player(player=player)

    def delete_player(self, player_username) -> None:
        """
        Method to delete the player with the given player_username from the database.
        Opens the JSON database, converts to python dict, pops out the given player, writes back the database.
        """
        data_path = self.get_data_path(player_username=player_username)
        if not self.username_exists_check(player_username=player_username):
            raise ValueError(f"delete_player called with player_username: {player_username} but no player "
                             f"with this username exists.")
        else:
            with open(data_path, "r") as player_data_file:
                all_player_data_dict: dict = json.load(player_data_file)
            all_player_data_dict.pop(player_username)
            with open(data_path, "w") as player_data_file:
                json.dump(all_player_data_dict, player_data_file)

    ##########
    # Methods relating to the storage location of players
    ##########
    def get_data_path(self, player_username: str) -> Path:
        """
        Method to:
        1) Return a specific path to the guest player data if the user has played as a guest
        2) Return the path to player data when a user player (non-guest) is being used
        3) Create the player data folder if it is empty by calling the create_player_data_file() method
        """
        if player_username == "guest":
            guest_player_data_path = self.player_data_directory_path / self.guest_datafile_name
            if guest_player_data_path.is_file():
                return guest_player_data_path
            else:
                self.create_guest_and_guest_data_file()
                return guest_player_data_path
        else:
            player_data_path = self.player_data_directory_path / self.player_datafile_name
            if player_data_path.is_file():  # i.e. if the file has already been created
                return player_data_path
            else:  # if the file hasn't been created, call the file creation method before returning path to it
                self.create_player_data_file()
                return player_data_path

    def create_player_data_file(self) -> None:
        """
        Method to create an empty json data file that player data will be uploaded to - this will only be done if the
        file does not already exist, otherwise an error will be raised
        """
        player_data_path = self.player_data_directory_path / self.player_datafile_name  # Where non-guest data goes
        if player_data_path.is_file():  # i.e. if the file has already been created
            raise FileExistsError(
                f"create_player_data_file method of PlayerDatabaseManager "
                f"was called although the player data file already exists")
        else:  # if the file hasn't been created
            if not Path.is_dir(self.player_data_directory_path):
                self.player_data_directory_path.mkdir(parents=True)
            with open(player_data_path, "x") as new_data_file:
                empty_dict: dict = {}  # This is the dict that will get written to JSON and filled with player data
                json.dump(empty_dict, new_data_file)

    def create_guest_and_guest_data_file(self) -> None:
        """
        Method to create the guest player - this will be called the first time a user chooses to play as the guest,
        i.e. when the guest player data file does not exist yet.
        The guest player is encoded in JSON and given their own file - now when a user tries to load them, they are
        available.
        """
        guest_data_path = self.player_data_directory_path / self.guest_datafile_name
        if guest_data_path.is_file():  # i.e. if the file has already been created
            raise FileExistsError(
                f"create_guest_and_guest_data_file method of PlayerDatabaseManager "
                f"was called although the guest data file already exists")
        else:
            if not Path.is_dir(self.player_data_directory_path):
                self.player_data_directory_path.mkdir(parents=True)

            # Create and encode a new guest player, then dump them in a json file
            guest = self.player_object(name="Guest", username="guest", password="guest")  # Other params default
            encoded_guest = self.encode_player(player=guest)
            guest_data_dict = {"guest": encoded_guest}
            with open(guest_data_path, "w") as guest_data_file:
                json.dump(guest_data_dict, guest_data_file)

    ##########
    # Methods to serialise/deserialise the Player object
    ##########
    @staticmethod
    def encode_player(player: PLAYER_TYPES) -> dict:
        """
        Method to take a player object, serialise all their parameters, and then store these parameters in a dictionary
        so that json.dump() can be used on the dictionary.


        Parameters: player (the player whose attributes are being converted to a dict)
        Returns: dict (a dictionary of the player's attributes, containing only serialisable data types)

        Note that if in the future player attributes are introduced of different types that are not immediately
        serialisable, then the encoding function below must be updated.
        """
        #  TODO add some form of encryption for player password encoding
        unserialisable_dict = player.__dict__
        serialisable_dict = {}
        for key, value in unserialisable_dict.items():
            if type(value) is datetime:
                serialisable_dict[key] = value.isoformat()
            else:
                serialisable_dict[key] = value
        return serialisable_dict

    def decode_player(self, serialised_attributes_dict: dict) -> PLAYER_TYPES:
        """
        Method to take a dictionary of a player's attributes, that has been loaded using json.loads(), and then
        instantiate a player based on this dictionary.

        Parameters: serialised_attributes_dict - the player's attributes in a format that can be stored as JSON
        Returns: The instantiated player, once their attributes have been deserialised

        Note that if in the future player attributes are introduced of different types that are not immediately
        serialisable, then the encoding function below must be updated.
        """
        attributes_dict = {}  # i.e. attributes in the type that player_object takes
        for key, value in serialised_attributes_dict.items():
            if isinstance(value, str):
                try:
                    attributes_dict[key] = datetime.fromisoformat(value)
                except ValueError:
                    attributes_dict[key] = value
            else:
                attributes_dict[key] = value
        live_player = self.player_object(**attributes_dict)
        return live_player

    ##########
    # Lower level player interaction methods
    ##########

    def username_exists_check(self, player_username: str) -> bool:
        """
        Method to check whether or not there is already a player in the database with the given player_username.
        Returns: True if the player_username exists, False if not
        """
        data_path = self.get_data_path(player_username=player_username)
        with open(data_path, "r") as all_player_data:
            all_player_data_dict: dict = json.load(all_player_data)
        return player_username in all_player_data_dict.keys()

    @staticmethod
    def username_meets_criteria_check(proposed_username: str) -> bool:
        """Method to check that a player's desired username meets the desired criteria"""
        disallowed_username_characters: list = PlayerParameterRestrictions.username_parameters.disallowed_characters
        min_length: int = PlayerParameterRestrictions.username_parameters.minimum_length
        username_allowed = True
        for char in disallowed_username_characters:
            username_allowed *= char not in proposed_username
        username_allowed *= len(proposed_username) >= min_length
        return username_allowed

    @staticmethod
    def password_meets_criteria_check(proposed_password: str) -> bool:
        minimum_length: int = PlayerParameterRestrictions.password_parameters.minimum_length
        if len(proposed_password) >= minimum_length:
            return True
        else:
            return False

    @staticmethod
    def name_meets_criteria_check(proposed_name: str) -> bool:
        disallowed_name_characters: list = PlayerParameterRestrictions.name_parameters.disallowed_characters
        username_allowed = True
        for char in disallowed_name_characters:
            username_allowed *= char not in proposed_name
        return username_allowed
