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
                 active_individual_bet: USER_BET_TYPES = None,
                 navigation_id: str = 'W'):
        self.active_player = active_player
        self.active_wheel_id = active_wheel_id
        self.active_wheel = active_wheel
        self.active_individual_bet = active_individual_bet
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
            # Individual bet selection
            ##########
            if self.navigation_id in navigation_dict['from_individual_bet_selection']:
                self.set_active_individual_bet(wheel_bet_selector=wheel_bet_selector)

            ##########
            # Bet evaluation #TODO do this as a for bet in bet list
            ##########
            if self.navigation_id in navigation_dict['from_bet_evaluation']:
                """i.e. if user chose to change wheel or bet type or stake amount or bet choice or just repeat bet."""
                # included here as otherwise a repeat bet wouldn't cost the player anything
                self.active_player.take_stake_from_pot(amount=self.active_individual_bet.stake)
                winnings = self.active_individual_bet.evaluate_user_bet()
                self.active_player.add_winnings_to_pot(amount=winnings)

            ##########
            # Establish game continuation criteria
            ##########
            if self.active_player.all_in_status:
                sys.exit(f"Game over. Your final pot is £{self.active_player.active_pot}")
            game_continuation = RouletteContinuationUser(stake=self.active_individual_bet.stake)
            game_continuation.keep_playing(active_player=self.active_player)
            self.active_player = game_continuation.check_top_up_worthwhile(existing_player=self.active_player)
            self.navigation_id = game_continuation.choose_navigation(active_player=self.active_player)

    def set_active_individual_bet(self, wheel_bet_selector: WheelAndBetTypeSelectorUser) -> USER_BET_TYPES:
        """
        Method that takes the user through the process of specifying one individual bet.
        Parameters:
        wheel_bet_selector - This is the utility class which allows the user to select the type of bet, and
        the wheel, but not within this method as all bets must be on the same wheel.
        Returns:
        self.active_bet (as a USER_BET_TYPES). The purpose of the return is to more cleanly add it to the collection
        of all active bets on the given wheel
        """
        while True:
            ##########
            # 1 Choose bet type
            ##########
            potential_bet: USER_BET_TYPES = wheel_bet_selector.choose_bet(wheel_id=self.active_wheel_id)
            potential_bet.set_playing_wheel(wheel=self.active_wheel)
            ##########
            # 2 Determine stake amount
            ##########
            stake, all_in_status = potential_bet.choose_stake_amount(player_funds=self.active_player.active_pot)
            potential_bet.set_stake_amount(amount=stake)
            ##########
            # 3 Determine bet choice, which is specific to the bet type
            ##########
            bet_choice = potential_bet.get_user_bet_choice()
            potential_bet.set_bet_choice(bet_choice=bet_choice)
            ##########
            # 4 Determine the win criteria and calculate the payout of the specific bet choice, and set these to the bet
            ##########
            win_criteria = potential_bet.determine_win_criteria()
            potential_bet.set_win_criteria(win_criteria=win_criteria)
            payout = potential_bet.calculate_payout()
            potential_bet.set_payout(amount=payout)
            ##########
            # Bet choice confirmation - if not confirmed, the loop restarts
            ##########
            if potential_bet.confirm_bet_choice():
                self.active_individual_bet = potential_bet
                self.active_player.set_all_in_status(true_or_false=all_in_status)
                break
            else:
                continue
