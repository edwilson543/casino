"""Module to run in order to play roulette on the command line."""

# Standard library imports
import logging

# Local application imports
from games.logging_setup import LogConfiguration

# Local application UI imports
from user_interface.games.roulette.app.single_player_roulette_user.single_player_table_user import \
    SinglePlayerRouletteTableUser
from user_interface.games.players.player_database_interactions_user import PlayerDatabaseInteractionsUser

if __name__ == '__main__':
    LogConfiguration(log_file_name="game_log.txt").logging_set_up()
    logging.info("Initiating a game of Roulette.")
    active_player = PlayerDatabaseInteractionsUser().all_games_set_up()  # sets the player for the game
    roulette = SinglePlayerRouletteTableUser(active_player=active_player)
    roulette.roulette_loop()
