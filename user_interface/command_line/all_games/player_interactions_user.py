from Games.games_base_classes import Player
from Games.players.existing_players import existing_players
import sys


class PlayerUserInteractions:
    """
    Class to initiate the roulette game.
    Methods to get the user to initiate the game, set their initial deposit, and choose the wheel they want to play on
    """

    def __init__(self, min_deposit: int, deposit_multiples: int):
        self.min_deposit = min_deposit
        self.deposit_multiples = deposit_multiples

    ####
    # HERE to HERE2 should go in an overall game initiation class
    ####

    def existing_or_new_player(self):
        """Method to determine whether the user wants to access an existing player, or create a new player"""
        print("Welcome to Balint and Ed's online casino")  # TODO separate messsaging of this level into a new file
        # and allow functionality choose what game they'd like to play
        while True:
            player_type = input(
                "Would you like to play as a new or as an existing player?\n[G]uest, [E]xisting, [N]ew\n--->").upper()
            if player_type == 'G':
                return existing_players['guest']
            elif player_type == 'E':
                return self.player_password_check(self.access_player())  # TODO find out how to use decorator instead
            elif player_type == 'N':
                print("New player functionality not built yet")
                continue
            else:
                print(f"{player_type} not a valid option, please try again")

    def access_player(self):  # TODO should be moved outside somewhere
        """Method to set the active_player within the game"""
        while True:
            username = input(f"What is your username?\n--->").lower()
            if username in existing_players:
                return existing_players[username]
            else:
                print(f"No user with username: {username} found. Please try again.")

    def player_password_check(self, player: Player) -> Player:
        """Method to wrap the access_player method"""
        for attempt in range(5):
            password = input(f"Please enter your password\n--->")
            if password == player.password:
                return player
            elif attempt == 4:
                sys.exit("Too many invalid attempts")
            else:
                print(f"Incorrect password - please try again.\nYou have {attempt} attempts remaining")

    def create_new_player(self):
        pass

    # TODO integrate instead some interaction with the player class here
    def get_user_deposit_amount(self):
        """Method to get the user to specify how much they want to deposit."""
        while True:
            deposit_amount = input("How much would you like to deposit to play with?\n"
                                   f"Deposits are allowed as multiples of £{self.deposit_multiples},"
                                   f"the minimum deposit is £{self.min_deposit}. \n--->")
            try:
                user_pot = int(deposit_amount.replace("£", ""))  # in case someone types in e.g. £100 rather than 150
                if user_pot >= self.min_deposit and user_pot % self.deposit_multiples == 0:
                    confirmation = input(f"Are you sure you would like to deposit £{user_pot} to play with?\n"
                                         "[Y]es, [N]o \n--->").upper()
                    if confirmation != 'Y':
                        continue
                    print(f"You have deposited £{user_pot} to play with")
                    return user_pot
                else:
                    print('Invalid deposit amount - please try again and refer to deposit criteria.')
            except ValueError:
                print('Invalid deposit amount - please try again and refer to deposit criteria.')

    def get_user_top_up_amount(self):
        pass
