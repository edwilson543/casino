from Games.games_base_classes import Player
from user_interface.command_line.Roulette.definitions.navigation_defns_user import navigation_dict
from user_interface.command_line.all_games.player_interactions_user import PlayerUserInteractions
from user_interface.command_line.Roulette.app.roulette_mechanics_user_classes.roulette_initiation_user import \
    RouletteInitiatorUser
from Games.Roulette.app.roulette_mechanics_action_classes.bet_selection import BetSelector

from user_interface.command_line.Roulette.app.roulette_mechanics_user_classes.bet_placement_user import BetPlacementUser

from Games.Roulette.app.roulette_mechanics_action_classes.bet_evaluation import BetEvaluation
from user_interface.command_line.Roulette.app.roulette_mechanics_user_classes.roulette_continuation_user import \
    RouletteContinuationUser

import sys
# added whilst updating
from Games.Roulette.app.roulette_wheel_base_class import RouletteWheel
from Games.Roulette.definitions.wheel_defns import wheel_options


################
# Game set up - this could be moved out to be at Game level/ renamed log in process etc.
################
def roulette_setup():
    """Method to access command line game selection, and choose the player/play as gues/new player"""
    play_setup = PlayerUserInteractions()
    active_player = play_setup.existing_or_new_player()  # allows user to play as guest/ existing/ new player
    active_player = play_setup.initial_deposit_or_top_up(active_player)
    return active_player


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

    def __init__(self,
                 active_player: Player = None,
                 active_top_up_amount: int = 0,
                 active_wheel_id: str = 'E',
                 active_bet_cat: str = 'O',
                 active_bet_type_id: str = 'C',
                 active_stake: int = 20,
                 active_bet_choice: str = 'G',
                 active_winning_slots: list = None,  # resolution needed?
                 active_potential_winnings: int = 50,
                 active_winnings: int = 0,
                 all_in_status: bool = False,
                 navigation_id: str = 'W',
                 active_wheel: RouletteWheel = None):
        self.active_player = active_player
        self.active_top_up_amount = active_top_up_amount
        self.active_wheel_id = active_wheel_id
        self.active_bet_cat = active_bet_cat
        self.active_bet_type_id = active_bet_type_id
        self.active_stake = active_stake
        self.active_bet_choice = active_bet_choice
        self.active_winning_slots = active_winning_slots
        self.active_potential_winnings = active_potential_winnings
        self.active_winnings = active_winnings
        self.all_in_status = all_in_status
        self.navigation_id = navigation_id
        self.active_wheel = active_wheel  # TODO link up elsewhere

    def roulette_loop(self):
        """Method to loop over all game components, based on the navigation_id re-determined at end"""

        while True:
            ##################
            # NOT UPDATED
            ##################
            if self.navigation_id in navigation_dict['from_wheel_selection']:
                """i.e. if user chose to change wheel after their bet, or this is the first loop."""
                # Could maybe take the wheel choice method out of game initiation as not really relevant to min/max depo
                # wheel selection
                play_setup = RouletteInitiatorUser(min_deposit=0,
                                                   deposit_multiples=200)
                self.active_wheel_id = play_setup.wheel_choice()
                self.active_wheel = wheel_options[self.active_wheel_id]  # TODO integrate into wheel selection,
                # and probably just get rid of the whole wheel_id thing

            # bet selection
            #################
            # NOT UPDATED
            ################
            if self.navigation_id in navigation_dict['from_bet_selection']:
                """i.e. if user chose to change wheel or change bet category, or this is the first loop.
                or used because if they changed the wheel then also need to change bet category"""
                bet_selection = BetSelector(wheel_id=self.active_wheel_id, player_funds=self.active_player.active_pot)
                self.active_bet_cat = bet_selection.choose_bet_category()
                self.active_bet_type_id = bet_selection.choose_bet_type(bet_cat=self.active_bet_cat)

            # stake quantification - use of bet_selection from previous if maybe a bit unideal
            ################
            # NOT UPDATED
            ##################
            if self.navigation_id in navigation_dict['from_stake_quantification']:
                """i.e. if user chose to change wheel or bet type or stake amount."""
                bet_selection = BetSelector(wheel_id=self.active_wheel_id, player_funds=self.active_player.active_pot)
                self.active_stake, self.all_in_status = bet_selection.choose_stake_amount(
                    bet_type=self.active_bet_type_id)

            # Bet placing up to immediately before outcome evaluation
            ############
            # UPDATED
            ###########
            if self.navigation_id in navigation_dict['from_bet_choice']:
                """i.e. if user chose to change wheel or bet type or stake amount or bet choice."""
                bet_placer = BetPlacementUser(bet_type_id=self.active_bet_type_id,
                                              stake=self.active_stake,
                                              playing_wheel=self.active_wheel)
                self.active_bet_choice = bet_placer.get_user_bet_choice()
                self.active_winning_slots = bet_placer.get_winning_slots(self.active_bet_choice)
                self.active_potential_winnings = bet_placer.get_potential_winnings(self.active_winning_slots)

            # Bet evaluation
            ###############
            # PARTIALLY UPDATED
            ###############
            if self.navigation_id in navigation_dict['from_bet_evaluation']:
                """i.e. if user chose to change wheel or bet type or stake amount or bet choice or just repeat bet."""
                self.active_player.take_stake_from_pot(self.active_stake)  # included here incase user does a repeat bet
                bet_evaluater = BetEvaluation(potential_winnings=self.active_potential_winnings,
                                              winning_slots=self.active_winning_slots,
                                              user_pot=self.active_player.active_pot,
                                              wheel_id=self.active_wheel_id)
                self.active_winnings = bet_evaluater.evaluate_bet()
                self.active_player.add_winnings_to_pot(self.active_winnings)

            ##########
            # Partially updated
            # Establish game continuation criteria
            ##########
            if self.all_in_status:
                sys.exit(f"Game over. Your final pot is £{self.active_player.active_pot}")
            game_continuation = RouletteContinuationUser(stake=self.active_stake)
            game_continuation.keep_playing(active_player=self.active_player)
            self.active_player = game_continuation.check_top_up_worthwhile(existing_player=self.active_player)
            self.navigation_id = game_continuation.choose_navigation(active_player=self.active_player)
