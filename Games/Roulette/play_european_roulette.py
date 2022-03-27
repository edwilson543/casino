from Games.Roulette.app.game_setup.roulette_mechanics import RouletteInitiator
from Games.Roulette.app.game_setup.roulette_mechanics import BetSelector

play_setup = RouletteInitiator()
play_setup.game_initiator()
user_pot = play_setup.deposit_amount()
print(user_pot)  # just to check its working - to be removed
active_wheel = play_setup.wheel_choice()
print(active_wheel)  # just to check its working - to be removed

bet_selection = BetSelector()
active_bet_type = bet_selection.choose_bet_type()
print(active_bet_type)  # to check its working - to be removed

# TODO finish script - while deposit>0 just loop over the bet script, once it has feature to change pot
# TODO make an overalll class that is this script
