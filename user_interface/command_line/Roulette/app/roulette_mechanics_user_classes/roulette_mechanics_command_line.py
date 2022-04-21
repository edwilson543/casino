from Games.games_base_classes import Player

from user_interface.command_line.Roulette.definitions.wheel_defns_user import wheel_options_user
from user_interface.command_line.Roulette.definitions.bet_type_defns_user import bet_type_options_user
from user_interface.command_line.Roulette.definitions.navigation_defns import navigation_dict
from user_interface.command_line.Roulette.app.roulette_mechanics_user_classes.wheel_and_bet_type_selection_user import \
    WheelAndBetTypeSelectorUser
from user_interface.command_line.Roulette.app.roulette_mechanics_user_classes.roulette_continuation_user import \
    RouletteContinuationUser
from user_interface.command_line.Roulette.definitions.bet_type_defns_user import USER_BET_TYPES
from user_interface.command_line.Roulette.definitions.wheel_defns_user import USER_WHEEL_TYPES

import sys


##########
# Class pulling together all the components of the Roulette game and command line UI
##########

class RouletteGameUser:
    """
    Class to pull together all components of the roulette game, so they can be looped over
    Maybe there is a better way to do this than initialise dummy parameters, which never actually get used - looked at
    using None but apparently that is not ideal.
    The parameters are all those necessary to instantiate the classes in the other roulette_mechanics_action_classes.
    The game loops until the user runs out of money or
    """

    # TODO update bet and wheel with generic Vartypes
    def __init__(self,
                 active_player: Player = None,
                 active_wheel_id: str = None,
                 active_wheel: USER_WHEEL_TYPES = None,
                 active_bet: USER_BET_TYPES = None,
                 navigation_id: str = 'W'):
        self.active_player = active_player
        self.active_wheel_id = active_wheel_id
        self.active_wheel = active_wheel
        self.active_bet = active_bet
        self.navigation_id = navigation_id

        #  TODO - check whether any of these attributes can be got rid of

    def roulette_loop(self):
        """Method to loop over all game components, based on the navigation_id re-determined at end"""

        while True:

            wheel_bet_selector = WheelAndBetTypeSelectorUser(wheel_look_up=wheel_options_user,
                                                             bet_type_look_up=bet_type_options_user)
            ##########
            # Wheel selection
            ##########
            if self.navigation_id in navigation_dict['from_wheel_selection']:
                """i.e. if user chose to change wheel after their bet, or this is the first loop."""
                self.active_wheel_id, self.active_wheel = wheel_bet_selector.choose_playing_wheel()

            ##########
            # Bet type selection
            ##########
            if self.navigation_id in navigation_dict['from_bet_selection']:
                """i.e. if user chose to change change the bet category, or if this is the first loop.
                Also used if user changed the wheel as they then also need to change the bet category"""
                self.active_bet = wheel_bet_selector.choose_bet(wheel_id=self.active_wheel_id)
                self.active_bet.set_playing_wheel(wheel=self.active_wheel)  # tell bet object what wheel is in use

            ##########
            # Stake quantification
            ##########
            if self.navigation_id in navigation_dict['from_stake_quantification']:
                """i.e. if user chose to change wheel or bet type or stake amount."""
                stake, all_in_status = self.active_bet.choose_stake_amount(player_funds=self.active_player.active_pot)
                self.active_bet.set_stake_amount(amount=stake)
                self.active_player.set_all_in_status(true_or_false=all_in_status)

            ##########
            # Bet choice, specific to bet type
            ##########
            if self.navigation_id in navigation_dict['from_bet_choice']:
                """i.e. if user chose to change wheel or bet type or stake amount or bet choice."""
                # TODO fix bug where this results in error 'NoneType' object is not callable
                # TODO And define below process as a method, down below, so it can be added to some list
                bet_choice = self.active_bet.get_user_bet_choice()
                self.active_bet.set_stake_amount(bet_choice=bet_choice)
                # Not sure if it's unideal to create these variables here - they could be avoided by calling
                # the determine_win_criteria/calculate_payout methods within the setter method?
                win_criteria = self.active_bet.determine_win_criteria()
                self.active_bet.set_win_criteria(win_criteria=win_criteria)
                payout = self.active_bet.calculate_payout()
                self.active_bet.set_payout(amount=payout)

            ##########
            # Bet evaluation
            ##########
            if self.navigation_id in navigation_dict['from_bet_evaluation']:
                """i.e. if user chose to change wheel or bet type or stake amount or bet choice or just repeat bet."""
                # included here as otherwise a repeat bet wouldn't cost the player anything
                self.active_player.take_stake_from_pot(amount=self.active_bet.stake)
                winnings = self.active_bet.evaluate_user_bet()
                self.active_player.add_winnings_to_pot(amount=winnings)

            ##########
            # Establish game continuation criteria
            ##########
            if self.active_player.all_in_status:
                sys.exit(f"Game over. Your final pot is £{self.active_player.active_pot}")
            game_continuation = RouletteContinuationUser(stake=self.active_bet.stake)
            game_continuation.keep_playing(active_player=self.active_player)
            self.active_player = game_continuation.check_top_up_worthwhile(existing_player=self.active_player)
            self.navigation_id = game_continuation.choose_navigation(active_player=self.active_player)
