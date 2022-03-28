from Games.Roulette.app.game_setup.roulette_mechanics import RouletteInitiator
from Games.Roulette.app.game_setup.roulette_mechanics import BetSelector
import sys

# Game parameters
min_depo = 100
permitted_depo_multiples = 10

# Game initialisation
play_setup = RouletteInitiator()
play_setup.game_initiator()
user_pot = play_setup.deposit_amount(min_deposit=min_depo, deposit_multiples=permitted_depo_multiples)
active_wheel = play_setup.wheel_choice()

# Bet selection
bet_selection = BetSelector()
active_bet_cat = bet_selection.choose_bet_category()
active_bet_type = bet_selection.choose_bet_type(bet_cat=active_bet_cat)
# Stake quantification, bet placing and evaluation
stake = BetSelector().choose_stake_amount(bet_type=active_bet_type, user_funds=user_pot)

sys.exit('Game over i.e. not coded any further yet')

# TODO finish script - while deposit>0 just loop over the bet script, once it has feature to change pot
# TODO make an overall class that is this script
