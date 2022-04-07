from user_interface.command_line.Roulette.app.roulette_mechanics_user_classes.roulette_mechanics_user import \
    RouletteGameUser

if __name__ == '__main__':
    roulette = RouletteGameUser()
    roulette.roulette_setup()
    roulette.roulette_loop()
