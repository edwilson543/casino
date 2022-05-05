from games.roulette.app.single_player_roulette.single_player_table import SinglePlayerRouletteTable
from games.roulette.app.roulette_wheel_base_class import wheel_spin_return
from games.roulette.constants.game_constants import AllGameParameters
from games.roulette.app.roulette_wheel_base_class import WHEEL_TYPES
from user_interface.command_line.roulette.app.single_player_roulette_user.roulette_continuation_user import \
    NavigationOptionRank
from user_interface.command_line.roulette.app.single_player_roulette_user.wheel_and_bet_construction_user import \
    WheelAndBetConstructorUser
from user_interface.command_line.roulette.app.single_player_roulette_user.roulette_continuation_user import \
    RouletteContinuationUser
from user_interface.command_line.roulette.app.roulette_bet_base_class_user import USER_BET_TYPES
from user_interface.command_line.games.player_base_class_user import PlayerUser
from user_interface.command_line.games.players.player_interactions_user import PlayerInteractionsUser

##########
# Class pulling together all the components of the roulette game and command line UI
##########

class SinglePlayerRouletteTableUser(SinglePlayerRouletteTable):
    """
    Class to pull together all components of the roulette game, so they can be looped over
    Maybe there is a better way to do this than initialise dummy parameters, which never actually get used - looked at
    using None but apparently that is not ideal.
    The parameters are all those necessary to instantiate the classes in the other single_player_roulette.
    The game loops until the user runs out of money or
    """

    def __init__(self,
                 active_player: PlayerUser = None,
                 active_wheel: WHEEL_TYPES = None,
                 constructor=WheelAndBetConstructorUser(),
                 player_database_interactor=PlayerInteractionsUser(),
                 active_all_bets_list: list = None,
                 next_step: int = 0):
        super().__init__(active_player, active_wheel, constructor, player_database_interactor, active_all_bets_list)
        self.next_step = next_step

    def roulette_loop(self):
        """Method to loop over all game components, based on the next_step re-determined at end"""

        while True:
            ##########
            # Wheel selection
            ##########
            if self.next_step <= NavigationOptionRank.CHANGE_WHEEL.value:
                """If user chose to change wheel after their bet, or this is the first loop."""
                self.active_wheel = self.constructor.choose_playing_wheel()

            ##########
            # Individual bet selection and accumulation
            ##########
            if self.next_step <= NavigationOptionRank.CHANGE_BETS.value:
                """If user has chosen to change all bets (or change wheel, need to do this too)"""
                self.active_player.reset_total_active_stake()  # so that it does not accumulate from previous bets
                self.set_all_active_bets_list()  # loops through individual bet selection and creates list of user bets

            ##########
            # Bet evaluation
            ##########
            if self.next_step == NavigationOptionRank.REPEAT_BETS.value:  # if player repeats bets, take stake again
                self.active_player.take_stake_from_pot(amount=self.active_player.total_active_stake)
            if self.next_step <= NavigationOptionRank.REPEAT_BETS.value:
                """If user chose to change wheel or bet type or stake amount or bet choice or just repeat bet."""
                spin_outcome: wheel_spin_return = self.active_wheel.user_spin()  # gets user to spin wheel
                bet_win_count, total_winnings = super().evaluate_all_active_bets_list(spin_outcome=spin_outcome)
                self.active_player.add_winnings_to_pot(amount=total_winnings)
                self.give_user_bet_news(bet_win_count=bet_win_count, total_winnings=total_winnings)

            ##########
            # Establish game continuation criteria
            ##########
            game_continuation = RouletteContinuationUser(stake=self.active_player.total_active_stake)
            game_continuation.keep_playing(active_player=self.active_player)
            top_up = self.active_player.check_top_up_scenario()
            # top_up, game_continues = self.active_player.check_top_up_scenario()
            # if not game_continues:
            #     self.terminate_player_session()
            # if player is low on funds, they'll be asked to top up. If really low, must top up to keep playing
            if top_up > 0:
                self.active_player.add_top_up_to_pot(amount=top_up)
            self.next_step = game_continuation.choose_navigation(active_player=self.active_player)

    ##########
    # Tier 2 Methods called in roulette_loop
    ##########
    def terminate_player_session_user(self) -> None:
        """
        Method to control the end of the game - chiefly to upload player progress to database
        """
        self.terminate_player_session()  # Uploads player's progress to database
        self.active_player.end_session_user_message()
        exit()


    def set_all_active_bets_list(self):
        """
        Method to repeatedly allow users to define bets and add them to the current spin.
        Calls the get_individual_bet to determine the parameters of each bet, and then accumulates them in the
        active_all_bets_list.
        The loop continues until either the user has gone all in or the user does not want to add any more bets.
        No returns - outcome is to set the active_all_bets_list
        """
        self.active_all_bets_list = []
        while True:
            individual_bet = self.get_individual_bet()
            self.active_all_bets_list.append(individual_bet)
            if self.determine_if_user_wants_to_add_more_bets():
                continue
            else:
                break

    def give_user_bet_news(self, bet_win_count: int, total_winnings: int):
        """Method to tell the user the outcome of all of their bets"""
        if bet_win_count > 0:
            print(f"Congratulations {self.active_player.name}! {bet_win_count} of your bets won!\n"
                  f"You've received a huge payout of £{total_winnings}")
        else:
            print("Better luck next time, none of your bets won.")

    ##########
    # Tier 3 methods called in set_all_active_bets_list
    ##########

    def get_individual_bet(self) -> USER_BET_TYPES:
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
        """
        while True:
            ##########
            # 1 Choose bet type
            ##########
            potential_bet: USER_BET_TYPES = self.constructor.choose_bet_type(wheel_name=self.active_wheel.wheel_name)
            potential_bet.set_playing_wheel(wheel=self.active_wheel)

            ##########
            # 2 Determine stake amount
            ##########
            stake = potential_bet.choose_stake_amount(player_funds=self.active_player.active_pot)
            potential_bet.set_stake_amount(amount=stake)

            ##########
            # 3 Determine bet choice, which is specific to the bet type
            ##########
            bet_choice = potential_bet.get_user_bet_choice()
            potential_bet.set_bet_choice(bet_choice=bet_choice)
            bet_choice_string = potential_bet.get_bet_choice_string_rep()
            potential_bet.set_bet_choice_string_rep(bet_choice_string=bet_choice_string)

            ##########
            # 4 Determine the win criteria and calculate the payout of the specific bet choice
            # and set these as attributes to the bet
            ##########
            win_criteria = potential_bet.determine_win_criteria()
            potential_bet.set_win_criteria(win_criteria=win_criteria)

            payout = potential_bet.calculate_payout()
            potential_bet.set_payout(amount=payout)

            ##########
            # 5 Bet choice confirmation - if not confirmed, the loop restarts
            ##########
            if potential_bet.confirm_bet_choice():
                self.active_player.total_active_stake += stake  # adds to active total stake in game
                self.active_player.take_stake_from_pot(amount=stake)
                return potential_bet
            else:
                continue

    def determine_if_user_wants_to_add_more_bets(self):
        while True:
            if self.active_player.active_pot <= AllGameParameters.top_up_parameters.low_pot_forced_top_up:
                user_wants_more_bets_via_top_up = input(
                    f"You have £{self.active_player.active_pot} left to play with, "
                    f"and £{self.active_player.total_active_stake} on the line.\n"
                    f"To add more bets to the current spin you must top up.\n"
                    f"Would you like to top up and place more bets?\n"
                    f"[Y]es, [N]o, proceed to wheel spinning\n--->").upper()
                if user_wants_more_bets_via_top_up == "Y":
                    top_up_amount = self.active_player.get_top_up_amount()
                    self.active_player.add_top_up_to_pot(amount=top_up_amount)
                    return True  # player has been topped up and will now cycle back through bet selection
                elif user_wants_more_bets_via_top_up == "N":
                    return False  # proceeds to wheel spinning
                else:
                    print("Invalid command, please try again")
                    continue
            else:
                user_wants_to_add_more_bets = input(
                    f"You currently have £{self.active_player.total_active_stake} "
                    f"on the line.\nWould you like to add more bets to the current wheel spin?\n"
                    "[Y]es, [N]o\n--->").upper()
                if user_wants_to_add_more_bets == "Y":
                    return True
                elif user_wants_to_add_more_bets == "N":
                    return False
                else:
                    print("Invalid command, please try again")
                    continue
