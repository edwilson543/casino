from Games.Roulette.app.game_setup.roulette_mechanics import RouletteInitiator
from Games.Roulette.app.game_setup.roulette_mechanics import BetSelector
from Games.Roulette.app.game_setup.roulette_mechanics import RouletteWheelWagers
from Games.Roulette.app.game_setup.roulette_mechanics import BetEvaluation
import sys

# Game parameters
min_depo = 100
permitted_depo_multiples = 10

# Game initialisation
play_setup = RouletteInitiator(min_deposit=min_depo, deposit_multiples=permitted_depo_multiples)
play_setup.game_initiator()
user_pot = play_setup.deposit_amount()
active_wheel_id = play_setup.wheel_choice()

# Bet selection
bet_selection = BetSelector(wheel_id=active_wheel_id, player_funds=user_pot)
active_bet_cat = bet_selection.choose_bet_category()
active_bet_type_id = bet_selection.choose_bet_type(bet_cat=active_bet_cat)
# Stake quantification
active_stake = bet_selection.choose_stake_amount(bet_type=active_bet_type_id)
user_pot -= active_stake

# Bet placing up to immediately before outcome evaluation
bet_placer = RouletteWheelWagers(stake=active_stake, bet_type_id=active_bet_type_id, wheel_id=active_wheel_id)
active_bet_choice, active_potential_winnings = bet_placer.place_bet()
active_winning_slots = bet_placer.get_winning_slots(player_bet=active_bet_choice)

# Bet evaluation
bet_evaluater = BetEvaluation(potential_winnings=active_potential_winnings,
                              winning_slots=active_winning_slots,
                              wheel_id=active_wheel_id)
winnings = bet_evaluater.evaluate_bet()
user_pot += winnings
print(f"Current pot: £{user_pot}")

sys.exit('Game over i.e. not coded any further yet')

# TODO finish script - while deposit>0 just loop over the bet script, once it has feature to change pot
# TODO make an overall class that is this script
