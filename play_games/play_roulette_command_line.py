from user_interface.command_line.roulette.app.roulette_mechanics_user_classes.roulette_mechanics_command_line import \
    RouletteGameUser
from user_interface.command_line.all_games.player_interactions_user import PlayerInteractionsUser

if __name__ == '__main__':
    active_player = PlayerInteractionsUser().all_games_set_up()  # sets the player for the game
    roulette = RouletteGameUser(active_player=active_player)
    roulette.roulette_loop()
