from base_path import ROOT_DIRECTORY
from pathlib import Path
from datetime import datetime
import json
from games.player_base_class import Player, PLAYER_TYPES

#  TODO add player data file to the gitignore
class PlayerInteractions:
    def __init__(self,
                 player_object: PLAYER_TYPES = Player,
                 player_data_directory_path: Path = ROOT_DIRECTORY / "games" / "players",
                 player_datafile_name: str = "player_data.json",
                 guest_datafile_name: str = "guest_data.json"):
        """
        Parameters:
        ----------
        player_object: the type of player object to be instantiated from their attributes in storage.
        This will currently either be just Player or PlayerUser.
        # TODO write this docstring
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
        Parameters: player_username: the player_username of the player to be retrieved. Note that if the guest player_username
        is passed, then the data_path will just point to the guest_data.json
        Returns: live_player: an instance of the desired Player subclass
        """
        data_path = self.get_data_path(player_username=player_username)
        with open(data_path, "r") as player_data_file:  # TODO update this path to be dynamic
            try:
                all_player_data_dict: dict = json.load(player_data_file)
                encoded_player_data = all_player_data_dict[player_username]
                live_player = self.decode_player(serialised_attributes_dict=encoded_player_data)
                return live_player
            except KeyError:
                raise KeyError("load_player method attempted to load a player not found in player database.")

    def upload_player(self, player: PLAYER_TYPES) -> None:
        """
        Method to upload a player to the JSON data storage.
        For new player's this represents creation, for existing player's this just updates their data.
        Player object -> python dict (self.encode_player) -> JSON dict -> insert into JSON database
        Parameters: player - the player being stored
        """
        data_path = self.get_data_path(player_username=player.username)
        with open(data_path, "r") as player_data_file:
            all_player_data_dict: dict = json.load(player_data_file)
        all_player_data_dict[player.username] = self.encode_player(player=player)
        with open(data_path, "w") as player_data_file:
            json.dump(all_player_data_dict, player_data_file)

    def create_player(self, name, player_username, password) -> None:
        """
        Method to check whether or not a given player_username already exists,
        and then upload them to the database if not.
        """
        if self.username_existence_check(username=player_username):
            raise ValueError(f"create_player called with player_username: {player_username} which is already in use.")
        else:
            player = self.player_object(name=name, username=player_username, password=password)  # Other params default
            self.upload_player(player=player)

    def delete_player(self, player_username) -> None:
        """
        Method to delete the player with the given player_username from the database.
        Opens the JSON database, converts to python dict, pops out the given player, writes back the database.
        """
        data_path = self.get_data_path(player_username=player_username)
        if not self.username_existence_check(username=player_username):
            raise ValueError(f"delete_player called with player_username: {player_username} which is already in use.")
        else:
            with open(data_path, "r") as player_data_file:
                all_player_data_dict: dict = json.load(player_data_file)
            all_player_data_dict.pop(player_username)
            with open(data_path, "w") as player_data_file:
                json.dump(all_player_data_dict, player_data_file)

    def get_data_path(self, player_username: str) -> Path:
        """
        Method to:
        1) Return a specific path to the guest player data if the user has played as a guest
        2) Return the path to player data when a user player (non-guest) is being used
        3) Create the player data folder if it is empty by calling the create_player_data_file() method
        """
        if player_username == "guest":
            player_data_path = self.player_data_directory_path / self.guest_datafile_name
            return player_data_path
        else:
            player_data_path = self.player_data_directory_path / self.player_datafile_name
            if player_data_path.is_file():  # i.e. if the file has already been created
                return player_data_path
            else:  # if the file hasn't been created, call the file creation method before returning path to it
                self.create_player_data_file()
                return player_data_path

    ##########
    # Methods relating to the storage location of players
    ##########
    def create_player_data_file(self) -> None:
        """
        Method to create an empty json data file that player data will be uploaded to - this will only be done if the
        file does not already exist, otherwise an error will be raised
        """
        player_data_path = self.player_data_directory_path / self.player_datafile_name
        if player_data_path.is_file():  # i.e. if the file has already been created
            raise FileExistsError(
                f"create_player_data_file method of {self.__name__} "
                f"was called although the player data file already exists")
        else:  # if the file hasn't been created
            with open(player_data_path, "x") as new_data_file:
                empty_dict: dict = {}  # This is the dict that will get written to JSON and filled with player data
                json.dump(empty_dict, new_data_file)

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
        unserialisable_dict = player.__dict__
        serialisable_dict = {}
        for key, value in unserialisable_dict.items():
            if type(value) is datetime:
                serialisable_dict[key] = value.isoformat()
            else:
                serialisable_dict[key] = value
        return serialisable_dict

    ##########
    # Methods to serialise/deserialise the Player object
    ##########
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

    def username_existence_check(self, username: str) -> bool:
        """
        Method to check whether or not there is already a player in the database with the given player_username.
        Returns: True if the player_username exists, False if not
        """
        with open(self.player_data_directory_path, "r") as all_player_data:  # TODO updated path to be dynamic
            all_player_data_dict: dict = json.load(all_player_data)
        return username in all_player_data_dict.keys()
