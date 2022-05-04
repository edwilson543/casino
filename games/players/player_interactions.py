from games.player_base_class import Player, PLAYER_TYPES
from games.players.player_data import AllPlayerData
from dataclasses import asdict
from datetime import datetime
import json


class PlayerInteractions:
    def __init__(self,
                 player_object: PLAYER_TYPES=Player,
                 player_datafile: str = "player_data.json"):
        """
        Parameters:
        ----------
        player_object: the type of player object to be instantiated from their attributes in storage.
        This will currently either be just Player or PlayerUser.
        """
        self.player_object = player_object
        self.player_datafile = player_datafile

    @staticmethod  # TODO delete this method
    def get_player_from_player_username(username: str, desired_player_object=Player) -> PLAYER_TYPES:
        if hasattr(AllPlayerData, username):
            player_data = getattr(AllPlayerData, username)
            player_data_dict = asdict(player_data)
            live_player = desired_player_object(**player_data_dict)
            return live_player
        else:
            raise ValueError(f"No player with username {username} found")

    def load_player(self, player_username) -> PLAYER_TYPES:
        """
        Method to reading the JSON file storing all player data, retrieve the relevant player's data and then
        instantiate a player as an instance of self.player_object (using decode_player)
        JSON database -> player's JSON dict -> python dict (self.decode_player) -> instantiate player as a Player object
        Parameters: player_username: the username of the player to be retrieved
        Returns: live_player: an instance of the desired Player subclass
        """
        with open(self.player_datafile, "r") as all_player_data:  # TODO update this path to be dynamic
            try:
                all_player_data_dict: dict = json.load(all_player_data)
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
        with open(self.player_datafile, "r") as all_player_data:  # TODO updated path to be dynamic
            all_player_data_dict: dict = json.load(all_player_data)
        all_player_data_dict[player.username] = self.encode_player(player=player)
        with open("player_data.json", "w") as all_player_data:
            json.dump(all_player_data_dict, all_player_data)

    def create_player(self, name, username, password) -> None:
        """
        Method to check whether or not a given username already exists,
        and then upload them to the database if not.
        """
        if self.username_existence_check(username=username):
            raise ValueError(f"create_player called with username: {username} which is already in use.")
        else:
            player = self.player_object(name=name, username=username, password=password)  # All other parameters default
            self.upload_player(player=player)

    def delete_player(self, username) -> None:
        """
        Method to delete the player with the given username from the database.
        Opens the JSON database, converts to python dict, pops out the given player, writes back the database.
        """
        if not self.username_existence_check(username=username):
            raise ValueError(f"delete_player called with username: {username} which is already in use.")
        else:
            with open(self.player_datafile, "r") as all_player_data:  # TODO updated path to be dynamic
                all_player_data_dict: dict = json.load(all_player_data)
            all_player_data_dict.pop(username)
            with open("player_data.json", "w") as all_player_data:
                json.dump(all_player_data_dict, all_player_data)

    def username_existence_check(self, username: str) -> bool:
        """
        Method to check whether or not there is already a player in the database with the given username.
        Returns: True if the username exists, False if not
        """
        with open(self.player_datafile, "r") as all_player_data:  # TODO updated path to be dynamic
            all_player_data_dict: dict = json.load(all_player_data)
        return username in all_player_data_dict.keys()

    @staticmethod
    def encode_player(player: PLAYER_TYPES) -> dict:
        """
        Method to take a player object, and then store all their parameters in a dictionary, so that
        the player is then serialisable by json.dumps().
        Note that if in the future player attributes are introduced of different types that are not immediately
        serialisable, then the encoding function below must be updated.
        Parameters: player (the player whose attributes are being converted to a dict)
        Returns: dict (a dictionary of the player's attributes, containing only serialisable data types)
        """
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

# TODO create a file in the head folder using pathlib that determines the location of a file
# works a bit like the import path structure - relative path from there to this file
