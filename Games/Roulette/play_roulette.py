from Games.Roulette.app.game_setup.roulette_mechanics import RouletteInitiator
from Games.Roulette.app.game_setup.roulette_mechanics import BetSelector
from Games.Roulette.app.game_setup.roulette_mechanics import RouletteWheelWagers
import sys

# Game parameters
min_depo = 100
permitted_depo_multiples = 10

# Game initialisation
play_setup = RouletteInitiator(min_deposit=min_depo, deposit_multiples=permitted_depo_multiples)
play_setup.game_initiator()
user_pot = play_setup.deposit_amount()
active_wheel_id, active_wheel = play_setup.wheel_choice()

# Bet selection
bet_selection = BetSelector(wheel_id=active_wheel_id, player_funds=user_pot)
active_bet_cat = bet_selection.choose_bet_category()
active_bet_type_id = bet_selection.choose_bet_type(bet_cat=active_bet_cat)
# Stake quantification
active_stake = bet_selection.choose_stake_amount(bet_type=active_bet_type_id)

# Bet placing and evaluation
bet_place_evaluate = RouletteWheelWagers(stake=active_stake, bet_type_id=active_bet_type_id, wheel_id=active_wheel_id)
active_bet_choice = bet_place_evaluate.place_bet()

sys.exit('Game over i.e. not coded any further yet')

# TODO finish script - while deposit>0 just loop over the bet script, once it has feature to change pot
# TODO make an overall class that is this script
