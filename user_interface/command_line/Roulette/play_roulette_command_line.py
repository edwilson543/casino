from user_interface.command_line.Roulette.app.roulette_mechanics_user_classes.roulette_mechanics_user import \
    RouletteGameUser
from user_interface.command_line.all_games.player_interactions_user import PlayerUserInteractions

if __name__ == '__main__':
    active_player = PlayerUserInteractions().all_games_set_up()  # sets the player for the game
    roulette = RouletteGameUser(active_player=active_player)
    roulette.roulette_loop()

# TODO fix stake confirmation from going through with just an 'enter'
