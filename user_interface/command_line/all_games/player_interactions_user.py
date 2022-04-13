from Games.games_base_classes import Player
from Games.players.existing_players import existing_players
from Games.Roulette.definitions.game_parameters import deposit_parameters
from Games.Roulette.definitions.game_parameters import top_up_parameters
from Games.Roulette.definitions.game_parameters import threshold_for_top_up_prompt
import sys
import functools


##########
# Functions to access players, requiring user input of password
##########

def password_proected(n_attempts):
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


@password_proected(n_attempts=5)
def access_player():
    """Method to set the active_player within the game"""
    while True:
        username = input(f"What is your username?\n--->").lower()
        if username in existing_players:
            return existing_players[username]
        else:
            print(f"No user with username: {username} found. Please try again.")


class PlayerUserInteractions:
    """
    Class to initiate the roulette game.
    Methods to get the user to initiate the game, set their initial deposit, and choose the wheel they want to play on
    """

    def __init__(self,
                 min_deposit: int = deposit_parameters['min_deposit'],
                 deposit_multiples: int = deposit_parameters['deposit_multiples'],
                 min_top_up: int = top_up_parameters['min_top_up'],
                 top_up_multiples: int = top_up_parameters['top_up_multiples']):
        self.min_deposit = min_deposit
        self.deposit_multiples = deposit_multiples
        self.min_top_up = min_top_up
        self.top_up_multiples = top_up_multiples

    def all_games_set_up(self) -> Player:
        active_player = self.existing_or_new_player()
        active_player.set_active_session_initial_pot_and_time()
        active_player = self.initial_deposit_or_top_up(active_player=active_player)
        return active_player

    @staticmethod
    def existing_or_new_player() -> Player:
        """Method to determine whether the user wants to access an existing player, or create a new player"""
        print("Welcome to Balint and Ed's online casino!")
        # and allow functionality choose what game they'd like to play
        while True:
            player_type = input(
                "Would you like to play as a new or as an existing player?\n[G]uest, [E]xisting, [N]ew\n--->").upper()
            if player_type == 'G':
                return existing_players['guest']
            elif player_type == 'E':
                return access_player()
            elif player_type == 'N':
                print("New player functionality not built yet")
                continue
            else:
                print(f"{player_type} not a valid option, please try again")

    def initial_deposit_or_top_up(self, active_player) -> Player:
        """Method to get the user to either set an initial deposit if they are playing as a guest or as a new player,
        or to top up if playing as an existing player."""
        if active_player.player_type in ['G', 'N']:  # i.e. if player is a guest or new player, make them deposit
            return self.get_user_deposit_amount(new_player=active_player)
        elif active_player.player_type == 'E':  # i.e. if it's an existing player, use top up prompt method
            return self.check_top_up_worthwhile(existing_player=active_player)
        else:
            raise ValueError(
                f"Player: {active_player.name} has invalid player type and was passed to initial_deposit_or_top_up")

    ##########
    # Lower level methods called in the existing_or_new_player method above
    ##########

    def create_new_player(self) -> Player:  # TODO define this, will require some sort of reading/writing
        pass

    ##########
    # lower level methods called in the initial_deposit_or_top_up method above
    ##########

    def get_user_deposit_amount(self, new_player) -> Player:
        """
        Method to get new/guest users to specify how much they want to deposit.
        Parameters: new_player. This will either be a new or guest user, and hence the initial_pot,
        initial_pot_datetime, and active_pot are not yet determined. This method is to set these attributes.
        Returns: A Player object, which is the input player with the initial_pot, initial_pot_datetime, and
        active_pot set to to the user input amount.
        """
        while True:
            deposit_amount = input("How much would you like to deposit to play with?\n"
                                   f"Deposits are allowed as multiples of £{self.deposit_multiples},"
                                   f"the minimum deposit is £{self.min_deposit}. \n--->")
            try:
                deposit_amount_int = int(deposit_amount.replace("£", ""))  # e.g. replace '£100' with '100'
                if deposit_amount_int >= self.min_deposit and deposit_amount_int % self.deposit_multiples == 0:
                    confirmation = input(f"Are you sure you would like to deposit £{deposit_amount_int} to play with?\n"
                                         "[Y]es, [N]o \n--->").upper()
                    if confirmation != 'Y':
                        continue
                    print(f"You have deposited £{deposit_amount_int} to play with")
                    new_player.set_initial_pot(amount=deposit_amount_int)
                    return new_player
                else:
                    print('Invalid deposit amount - please try again and refer to deposit criteria.')
            except ValueError:
                print('Invalid deposit amount - please try again and refer to deposit criteria.')

    def check_top_up_worthwhile(self, existing_player) -> Player:
        """Method to check whether the user pot is below the threshold for a top up prompt to be worthwhile,
        and then make a top_up if it is worthwhile"""
        if existing_player.active_pot > threshold_for_top_up_prompt:
            return existing_player  # i.e. player's pot exceeds threshold so no need for prompt
        else:
            return self.get_user_top_up_amount(existing_player=existing_player)  # increased player pot if top up

    # method called in the check_top_up_worthwhile, if it is worthwhile, i.e. user pot is low
    def get_user_top_up_amount(self, existing_player) -> Player:
        """Method to get the user to specify if and then how much they want to top up by.
        Parameters: existing player - a player already fully defined in the existing_players dict. (With the
        exception perhaps of last_top_up_datetime).
        Returns: The same existing player, but with either a higher pot, or the same pot. The player attributes
        affected are active_pot and last_top_up_datetime"""
        while True:
            proceed = input(f"Your pot only contains £{existing_player.active_pot}.\n"
                            f"would you like to top up?\n[Y]es, [N]o\n--->").upper()
            if proceed == 'Y':
                break
            elif proceed == 'N':
                return existing_player  # output is then input, unaffected i.e. no top up
            else:
                print("Invalid command, please try again.")
        while True:
            top_up_amount = input("How much would you like to top up?\n"
                                  f"Top ups are allowed as multiples of £{self.top_up_multiples},"
                                  f"the minimum top up is £{self.min_top_up}.\n--->")
            try:
                top_up_int = int(top_up_amount.replace("£", ""))  # in case someone types in e.g. £100 rather than 100
                if top_up_int >= self.min_top_up and top_up_int % self.top_up_multiples == 0:
                    confirmation = input(f"Are you sure you would like to top up by £{top_up_int}?\n"
                                         "[Y]es, [N]o \n--->").upper()
                    if confirmation != 'Y':
                        continue
                    existing_player.add_top_up_to_pot(amount=top_up_int)
                    print(f"You have deposited £{top_up_int}.\n"
                          f"Your new pot is £{existing_player.active_pot}.")
                    return existing_player
                else:
                    print('Invalid top up amount - please try again and refer to criteria.')
            except ValueError:
                print('Invalid top up amount - please try again and refer to criteria.')
