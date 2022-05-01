from games.player_base_class import Player, PLAYER_TYPES
from games.players.player_data import AllPlayerData
from dataclasses import asdict

class PlayerInteractions:
    # def __init__(self):
    #     pass

    @staticmethod
    def get_player_from_player_username(username:str, desired_player_object=Player) -> PLAYER_TYPES:
        if hasattr(AllPlayerData, username):
            player_data = getattr(AllPlayerData, username)
            player_data_dict = asdict(player_data)
            live_player = desired_player_object(**player_data_dict)
            return live_player
        else:
            raise ValueError(f"No player with username {username} found")


    def load_player(self):
        """
        Reading JSON file to instantiate player
        JSON -> dict -> instantiate player as Player(**dict)
        """
        pass

    def create_player(self):
        """Encoding to JSON method"""
        pass

    def upload_player_progress(self):
        pass

    def player_search(self):
        """
        Method to read all the individual player files to search for a username
        Do not open all of them! Use glob - it is a bit nicer version of os.listdir
        """
        pass


#  TODO write the load/ create methods into individual files
# TODO create a file in the head folder using pathlib that determines the location of a file
# works a bit like the import path structure - relative path from there to this file
# Git ignore all files except for the guest file
