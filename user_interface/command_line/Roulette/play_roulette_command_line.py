from user_interface.command_line.Roulette.app.roulette_mechanics_user_classes.roulette_mechanics_command_line import \
    RouletteGameUser
from user_interface.command_line.all_games.player_interactions_user import PlayerUserInteractions

if __name__ == '__main__':
    active_player = PlayerUserInteractions().all_games_set_up()  # sets the player for the game
    roulette = RouletteGameUser(active_player=active_player)
    roulette.roulette_loop()

# TODO completely get rid of all in functionality and replace with top up
# TODO separate out all UI confirmation prompts into their own methods, so they can be turned on/off in one go
