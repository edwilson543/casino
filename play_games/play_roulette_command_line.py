"""Module that should be run to play roulette on the command line"""

from user_interface.command_line.roulette.app.single_player_roulette_user.single_player_table_user import \
    SinglePlayerRouletteTableUser
from user_interface.command_line.games.players.player_database_interactions_user import PlayerDatabaseInteractionsUser


if __name__ == '__main__':
    active_player = PlayerDatabaseInteractionsUser().all_games_set_up()  # sets the player for the game
    roulette = SinglePlayerRouletteTableUser(active_player=active_player)
    roulette.roulette_loop()
