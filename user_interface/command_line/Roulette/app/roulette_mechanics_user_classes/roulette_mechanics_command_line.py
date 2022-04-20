from Games.games_base_classes import Player
from Games.games_base_classes import Bet
from Games.Roulette.app.roulette_wheel_base_class import RouletteWheel

from user_interface.command_line.Roulette.definitions.wheel_defns_user import wheel_options_user
from user_interface.command_line.Roulette.definitions.bet_type_defns_user import bet_type_options_user
from user_interface.command_line.Roulette.definitions.navigation_defns import navigation_dict
from user_interface.command_line.all_games.player_interactions_user import PlayerUserInteractions
from user_interface.command_line.Roulette.app.roulette_mechanics_user_classes.bet_selection_user import \
    WheelAndBetTypeSelectorUser
from user_interface.command_line.Roulette.app.roulette_mechanics_user_classes.bet_placement_evaluation_user import \
    BetPlacementEvaluationUser
from user_interface.command_line.Roulette.app.roulette_mechanics_user_classes.roulette_continuation_user import \
    RouletteContinuationUser

from typing import Union
import sys


################
# Game set up - this could be moved out to be at Game level/ renamed log in process etc.
################
def roulette_setup() -> Player:
    """Method to access command line game selection, and choose the player/play as a guest/new player"""
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
                 active_wheel_id: str = 'E',
                 active_wheel: RouletteWheel = None,
                 active_bet_type: Bet = None,
                 active_bet_choice: Union[int, str, list] = None,
                 active_stake: int = 20,
                 active_winnings: int = 0,
                 all_in_status: bool = False,
                 navigation_id: str = 'W'):
        self.active_player = active_player
        self.active_wheel_id = active_wheel_id
        self.active_wheel = active_wheel
        self.active_bet_type = active_bet_type
        self.active_bet_choice = active_bet_choice
        self.active_stake = active_stake
        self.active_winnings = active_winnings
        self.all_in_status = all_in_status
        self.navigation_id = navigation_id

        #  TODO - check whether any of these attributes can be got rid of

    def roulette_loop(self):
        """Method to loop over all game components, based on the navigation_id re-determined at end"""

        while True:

            wheel_bet_selector = WheelAndBetTypeSelectorUser(wheel_look_up=wheel_options_user,
                                                             bet_type_look_up=bet_type_options_user,
                                                             active_player=self.active_player)  # might not need
            ##########
            # Wheel selection
            ##########
            if self.navigation_id in navigation_dict['from_wheel_selection']:
                """i.e. if user chose to change wheel after their bet, or this is the first loop."""
                self.active_wheel_id, self.active_wheel = wheel_bet_selector.choose_playing_wheel()

            ##########
            # Bet selection
            ##########
            if self.navigation_id in navigation_dict['from_bet_selection']:
                """i.e. if user chose to change wheel or change bet category, or this is the first loop.
                or used because if they changed the wheel then also need to change bet category"""
                self.active_bet_type = wheel_bet_selector.choose_bet(wheel_id=self.active_wheel_id)

            ##########
            # Class instance of class to quantify stakes, place and evaluate bets
            ##########
            bet_placer_evaluater = BetPlacementEvaluationUser(bet_type=self.active_bet_type,
                                                              stake=self.active_stake,
                                                              playing_wheel=self.active_wheel,
                                                              player_funds=self.active_player.active_pot)
            # maybe get rid of the player_funds usage here?
            ##########
            # Stake quantification
            ##########
            if self.navigation_id in navigation_dict['from_stake_quantification']:
                """i.e. if user chose to change wheel or bet type or stake amount."""
                self.active_stake, self.all_in_status = bet_placer_evaluater.choose_stake_amount()

            ##########
            # Bet placement
            ##########
            if self.navigation_id in navigation_dict['from_bet_choice']:
                """i.e. if user chose to change wheel or bet type or stake amount or bet choice."""
                self.active_bet_choice = bet_placer_evaluater.get_user_bet_choice()

            ##########
            # Bet evaluation
            ##########
            if self.navigation_id in navigation_dict['from_bet_evaluation']:
                """i.e. if user chose to change wheel or bet type or stake amount or bet choice or just repeat bet."""
                # included here as otherwise misses by a repeat bet
                self.active_player.take_stake_from_pot(self.active_stake)
                self.active_winnings = bet_placer_evaluater.evaluate_user_bet(bet_choice=self.active_bet_choice)
                self.active_player.add_winnings_to_pot(self.active_winnings)

            ##########
            # Establish game continuation criteria
            ##########
            if self.all_in_status:
                sys.exit(f"Game over. Your final pot is £{self.active_player.active_pot}")
            game_continuation = RouletteContinuationUser(stake=self.active_stake)
            game_continuation.keep_playing(active_player=self.active_player)
            self.active_player = game_continuation.check_top_up_worthwhile(existing_player=self.active_player)
            self.navigation_id = game_continuation.choose_navigation(active_player=self.active_player)
