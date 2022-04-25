from games.games_base_classes import Player
from games.players.existing_players import existing_players
from games.roulette.definitions.game_parameters import deposit_parameters
from games.roulette.definitions.game_parameters import top_up_parameters
from games.roulette.definitions.game_parameters import threshold_for_top_up_prompt, low_pot_forced_top_up
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
        if username in existing_players:
            return existing_players[username]
        else:
            print(f"No user with username: {username} found. Please try again.")


class PlayerInteractionsUser:  # TODO make this a subclass of PlayerInteractions
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
            initial_deposit = self.get_user_top_up_deposit_amount(dep_top_word="deposit")
            active_player.set_initial_pot(amount=initial_deposit)
            return active_player
        elif active_player.player_type == 'E':  # i.e. if it's an existing player, use top up prompt method
            top_up_amount = self.check_top_up_worthwhile(existing_player=active_player)
            if top_up_amount == 0:  # i.e. they were asked to top up but don't want to
                return active_player
            else:
                active_player.add_top_up_to_pot(amount=top_up_amount)
                return active_player
        else:
            raise ValueError(
                f"Player: {active_player.name} has invalid player type and was passed to initial_deposit_or_top_up")

    ##########
    # Lower level methods called in the existing_or_new_player method above
    ##########

    def create_player_user(self) -> Player:  # TODO define this, using super class method
        pass

    ##########
    # lower level methods called in the initial_deposit_or_top_up method above
    ##########

    def check_top_up_worthwhile(self, existing_player: Player) -> int:
        """
        Method to check whether the user pot is below the threshold for a top up prompt to be worthwhile,
        and then make a top_up if it is worthwhile/ they have to to keep playing.
        Note that user will be forced to top up by see_if_user_wants_to_top_up in order to continue
        playing, if their pot is below a pre-determined threshold.
        """
        if existing_player.active_pot > threshold_for_top_up_prompt:
            return 0  # i.e. player's pot exceeds threshold so no need for prompt
        else:
            if self.see_if_user_wants_to_top_up(existing_player=existing_player):
                top_up_amount = self.get_user_top_up_deposit_amount(dep_top_word="top up")
                return top_up_amount

    def get_user_top_up_deposit_amount(self, dep_top_word: str) -> int:
        """
        Method to get users to specify how much they want to deposit/ top up.
        Parameters: dep_top_word - the word to be displayed in the text depending on whether the user is being
        asked to deposit, or to top up.
        Returns: A Player object, which is the input player with the initial_pot, initial_pot_datetime, and
        active_pot set to to the user input amount.
        """
        while True:
            amount = input(F"How much would you like to {dep_top_word} to play with?\n"
                           f"Deposits are allowed as multiples of £{self.deposit_multiples},"
                           f"the minimum deposit is £{self.min_deposit}. \n--->")
            try:
                amount_int = int(amount.replace("£", ""))  # e.g. replace '£100' with '100'
                if amount_int >= self.min_deposit and amount_int % self.deposit_multiples == 0:
                    confirmation = input(f"Are you sure you would like to {dep_top_word} £{amount_int} to play with?\n"
                                         "[Y]es, [N]o \n--->").upper()
                    if confirmation != 'Y':
                        continue
                    print(f"You have made a {dep_top_word} of £{amount_int} to play with!")
                    return amount_int
                else:
                    print(f"Invalid {dep_top_word} amount - please try again and refer to {dep_top_word} criteria.")
            except ValueError:
                print(f"Invalid {dep_top_word} amount - please try again and refer to {dep_top_word} criteria.")

    @staticmethod
    def see_if_user_wants_to_top_up(existing_player: Player) -> bool:
        """
        Method to get the user to specify if they want to top up, having been given the top up prompt
        If they have £0 in their pot, they don't have a choice and must top up to continue playing.
        """
        while True:
            if existing_player.active_pot > low_pot_forced_top_up:
                print(f"Your pot only contains £{existing_player.active_pot}.\n")
                proceed = input("Would you like to top up?\n[Y]es, [N]o\n--->")
                if proceed == "Y":
                    return True
                elif proceed == "N":
                    return False
                else:
                    print("Invalid command, please try again.")
            elif existing_player.active_pot <= low_pot_forced_top_up:
                proceed = input("You have no money left in your pot, "
                                "to continue playing you must top up.\n"
                                "Would you like to top up?\n[Y]es, [N]o, end game\n--->").upper()
                if proceed == "Y":
                    return True
                elif proceed == "N":
                    existing_player.end_session()
                else:
                    print("Invalid command, please try again.")
            else:
                raise ValueError(f"{existing_player.name} has ended up with a negative pot of"
                                 f"£{existing_player.active_pot}.")
