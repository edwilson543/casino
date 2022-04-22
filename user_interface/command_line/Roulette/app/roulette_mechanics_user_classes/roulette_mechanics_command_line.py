from Games.games_base_classes import Player

from Games.Roulette.app.roulette_wheel_base_class import wheel_spin_return
from user_interface.command_line.Roulette.definitions.wheel_defns_user import wheel_options_user
from user_interface.command_line.Roulette.definitions.bet_type_defns_user import bet_type_options_user
from user_interface.command_line.Roulette.definitions.navigation_defns import post_spin_navigation_dict
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
                 active_all_bets_list: list = None,
                 active_spin_outcome: wheel_spin_return = None,
                 active_bet_win_count=0,
                 active_total_winnings=0,
                 navigation_id: str = 'W'):
        self.active_player = active_player
        self.active_wheel_id = active_wheel_id
        self.active_wheel = active_wheel
        self.active_all_bets_list = active_all_bets_list
        self.active_spin_outcome = active_spin_outcome
        self.active_bet_win_count = active_bet_win_count
        self.active_total_winnings = active_total_winnings
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
            if self.navigation_id in post_spin_navigation_dict['from_wheel_selection']:
                """i.e. if user chose to change wheel after their bet, or this is the first loop."""
                self.active_wheel_id, self.active_wheel = wheel_bet_selector.choose_playing_wheel()

            ##########
            # Individual bet selection and accumulation
            ##########
            if self.navigation_id in post_spin_navigation_dict['from_bet_selection']:
                """i.e. if user has chosen to change all bets (or change wheel, need to do this too)"""
                self.active_player.reset_active_total_stake()
                self.set_all_active_bets_list(wheel_bet_selector=wheel_bet_selector)  # creates a list of all user bets

            ##########
            # Bet evaluation
            ##########
            if self.navigation_id in post_spin_navigation_dict['from_bet_evaluation']:
                """i.e. if user chose to change wheel or bet type or stake amount or bet choice or just repeat bet."""
                self.active_spin_outcome = self.active_wheel.user_spin()  # gets user to spin wheel
                self.evaluate_all_active_bets_list()  # accumulates the winnings of each bet in the list
                self.give_user_bet_news()  # Tells user how many of their bets won, and winnings
                self.reset_game_attributes()  # Clears the spin/winnings outcomes, ready for the next spin

            ##########
            # Establish game continuation criteria
            ##########
            if self.active_player.all_in_status:
                sys.exit(f"Game over. Your final pot is £{self.active_player.active_pot}")
            game_continuation = RouletteContinuationUser(stake=self.active_player.active_total_stake)
            game_continuation.keep_playing(active_player=self.active_player)
            self.active_player = game_continuation.check_top_up_worthwhile(existing_player=self.active_player)
            self.navigation_id = game_continuation.choose_navigation(active_player=self.active_player)

    def set_all_active_bets_list(self, wheel_bet_selector: WheelAndBetTypeSelectorUser):
        """
        Method to repeatedly allow users to define bets and add them to the current spin.
        Calls the get_individual_bet to determine the parameters of each bet, and then accumulates them in the
        active_all_bets_list.
        The loop continues until either the user has gone all in or the user does not want to add any more bets.
        No returns - outcome is to set the active_all_bets_list
        """
        self.active_all_bets_list = []
        while True:
            individual_bet = self.get_individual_bet(wheel_bet_selector=wheel_bet_selector)
            self.active_all_bets_list.append(individual_bet)
            if self.active_player.all_in_status:  # i.e. if the player has gone all in, don't let them add more bets...
                break
            elif self.determine_if_user_wants_to_add_more_bets():
                continue
            else:
                break

    def evaluate_all_active_bets_list(self):
        """Method to evaluate each active bet in the list"""
        # TODO this is non ui focused - could go somewhere else, maybe new module
        for bet in self.active_all_bets_list:
            winnings = bet.evaluate_bet(spin_outcome=self.active_spin_outcome)
            if winnings > 0:
                self.active_bet_win_count += 1
                self.active_total_winnings += winnings
        self.active_player.add_winnings_to_pot(amount=self.active_total_winnings)

    def give_user_bet_news(self):
        if self.active_bet_win_count > 0:
            print(f"Congratulations! {self.active_bet_win_count} of your bets won!\n"
                  f"You've received a huge payout of £{self.active_total_winnings}")
        else:
            print("Better luck next time, none of your bets won.")

    def reset_game_attributes(self):
        self.active_spin_outcome = None
        self.active_bet_win_count = 0
        self.active_total_winnings = 0

    ##########
    # Lower level methods called in multi_bet_selection loop
    ##########

    def get_individual_bet(self, wheel_bet_selector: WheelAndBetTypeSelectorUser) -> USER_BET_TYPES:
        """
        Method that takes the user through the process of specifying one individual bet.
        Parameters:
        wheel_bet_selector - This is the utility class which allows the user to select the type of bet, and
        the wheel, but not within this method as all bets must be on the same wheel.

        Returns:
        self.active_bet (as a USER_BET_TYPES). The purpose of the return is to more cleanly add it to the collection
        of all active bets on the given wheel

        Other outcomes:
        Adds stake to active player's active_total_stake.
        Removes stake from active player's active_pot.
        Adds payout to active player's active_total_potential_winnings
        Sets active player's all_in_status
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
                self.active_player.take_stake_from_pot(amount=stake)  # also adds to player's active total stake
                self.active_player.set_all_in_status(true_or_false=all_in_status)
                return potential_bet
            else:
                continue

    def determine_if_user_wants_to_add_more_bets(self):
        while True:
            user_wants_to_add_more_bets = input(f"You currently have: £{self.active_player.active_total_stake} "
                                                f"on the line.\n"
                                                "Would you like to add more bets to the current wheel spin?\n"
                                                "[Y]es, [N]o\n"
                                                "--->").upper()
            if user_wants_to_add_more_bets == "Y":
                return True
            elif user_wants_to_add_more_bets == "N":
                return False
            else:
                print("Invalid command, please try again")
