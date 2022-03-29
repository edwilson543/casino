from Games.Roulette.app.game_setup.roulette_mechanics import RouletteInitiator
from Games.Roulette.app.game_setup.roulette_mechanics import BetSelector
from Games.Roulette.app.game_setup.roulette_mechanics import RouletteWheelWagers
import sys

# Game parameters
min_depo = 100
permitted_depo_multiples = 10

# Game initialisation
play_setup = RouletteInitiator()
play_setup.game_initiator()
user_pot = play_setup.deposit_amount(min_deposit=min_depo, deposit_multiples=permitted_depo_multiples)
active_wheel_id, active_wheel = play_setup.wheel_choice()
print(active_wheel_id)  # to check working - to delete
print(active_wheel)  # to check working - to delete

# Bet selection
bet_selection = BetSelector()
active_bet_cat = bet_selection.choose_bet_category(wheel_id=active_wheel_id)
active_bet_type_id = bet_selection.choose_bet_type(wheel_id=active_wheel_id, bet_cat=active_bet_cat)

# Stake quantification
active_stake = BetSelector().choose_stake_amount(wheel_id=active_wheel_id, bet_type=active_bet_type_id,
                                                 user_funds=user_pot)

# Bet placing and evaluation
bet_place_evaluate = RouletteWheelWagers(stake=active_stake, bet_type_id=active_bet_type_id, wheel_id=active_wheel_id)
active_bet_choice = bet_place_evaluate.place_bet()

sys.exit('Game over i.e. not coded any further yet')

# TODO finish script - while deposit>0 just loop over the bet script, once it has feature to change pot
# TODO make an overall class that is this script
