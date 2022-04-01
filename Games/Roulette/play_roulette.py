from Games.Roulette.definitions.game_parameters import deposit_parameters, top_up_parameters
from Games.Roulette.app.roulette_mechanics_classes.roulette_initiation import RouletteInitiator
from Games.Roulette.app.roulette_mechanics_classes.bet_selection import BetSelector
from Games.Roulette.app.roulette_mechanics_classes.bet_placement import RouletteWheelWagers
from Games.Roulette.app.roulette_mechanics_classes.bet_evaluation import BetEvaluation
from Games.Roulette.app.roulette_mechanics_classes.roulette_continuation import RouletteContinuation

# Game initialisation
play_setup = RouletteInitiator(min_deposit=deposit_parameters['min_deposit'],
                               deposit_multiples=deposit_parameters['deposit_multiples'])
play_setup.game_initiator()
initial_user_pot = play_setup.deposit_amount()
active_user_pot = initial_user_pot  # to print total win / loss at end of game or commentary on up/down

while True:
    active_wheel_id = play_setup.wheel_choice()

    # Bet selection
    bet_selection = BetSelector(wheel_id=active_wheel_id, player_funds=active_user_pot)
    active_bet_cat = bet_selection.choose_bet_category()
    active_bet_type_id = bet_selection.choose_bet_type(bet_cat=active_bet_cat)
    # Stake quantification
    active_stake = bet_selection.choose_stake_amount(bet_type=active_bet_type_id)
    active_user_pot -= active_stake

    # Bet placing up to immediately before outcome evaluation
    bet_placer = RouletteWheelWagers(stake=active_stake, bet_type_id=active_bet_type_id, wheel_id=active_wheel_id)
    active_bet_choice, active_potential_winnings = bet_placer.place_bet()
    active_winning_slots = bet_placer.get_winning_slots(player_bet=active_bet_choice)

    # Bet evaluation
    bet_evaluater = BetEvaluation(potential_winnings=active_potential_winnings,
                                  winning_slots=active_winning_slots,
                                  user_pot=active_user_pot,
                                  wheel_id=active_wheel_id)
    winnings = bet_evaluater.evaluate_bet()
    active_user_pot += winnings

    # establish game continuation criteria
    continuation = RouletteContinuation(user_pot=active_user_pot, min_top_up=top_up_parameters['min_top_up'],
                                        top_up_multiples=top_up_parameters['top_up_multiples'])
    continuation.keep_playing()
    top_up = continuation.check_top_up_prompt_worthwhile()
    active_user_pot += top_up

# TODO finish script - while deposit>0 loop over the bet script, once it has feature to change pot
# TODO make an overall class that is this script
