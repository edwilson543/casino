from Games.Roulette.app.game_setup.roulette_mechanics import RouletteInitiator
from Games.Roulette.app.game_setup.roulette_mechanics import BetSelector
import sys

min_depo = 100
permitted_depo_multiples = 10

play_setup = RouletteInitiator()
play_setup.game_initiator()
user_pot = play_setup.deposit_amount(min_deposit=min_depo, deposit_multiples=permitted_depo_multiples)
active_wheel = play_setup.wheel_choice()
print(active_wheel)  # just to check its working - to be removed

bet_selection = BetSelector()
active_bet_cat = bet_selection.choose_bet_category()
print(active_bet_cat) # to check uts working - to be removed
active_bet_type = bet_selection.choose_bet_type(bet_cat=active_bet_cat)
print(active_bet_type)  # to check its working - to be removed

sys.exit('Game over i.e. not coded any further yet')

# TODO finish script - while deposit>0 just loop over the bet script, once it has feature to change pot
# TODO make an overalll class that is this script
