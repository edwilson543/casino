from Games.Roulette.definitions.game_parameters import deposit_parameters, top_up_parameters
from Games.Roulette.app.roulette_mechanics_classes.roulette_initiation import RouletteInitiator
from Games.Roulette.app.roulette_mechanics_classes.bet_selection import BetSelector
from Games.Roulette.app.roulette_mechanics_classes.bet_placement import RouletteWheelWagers
from Games.Roulette.app.roulette_mechanics_classes.bet_evaluation import BetEvaluation
from Games.Roulette.app.roulette_mechanics_classes.roulette_continuation import RouletteContinuation
from Games.Roulette.definitions.navigation_defns import navigation_dict
import sys


class RouletteGame:
    """
    Class to pull together all components of the roulette game, so they can be loooped over
    Maybe there is a better way to do this than initialise dummy parameters, which never actually get used - looked at
    using None but apparently that is not ideal.
    The parameters are all those necessary to instantiate the classes in the other roulette_mechanics_classes.
    The game loops until the user runs out of money or
    """

    def __init__(self,
                 min_deposit: int = deposit_parameters['min_deposit'],
                 deposit_multiples: int = deposit_parameters['deposit_multiples'],
                 initial_user_pot: int = 0,
                 active_user_pot: int = 0,
                 min_top_up: int = top_up_parameters['min_top_up'],
                 top_up_multiples: int = top_up_parameters['top_up_multiples'],
                 active_top_up: int = 0,
                 active_wheel_id: str = 'E',
                 active_bet_cat: str = 'O',
                 active_bet_type_id: str = 'C',
                 active_stake: int = 20,
                 active_bet_choice: str = 'G',
                 active_winning_slots: list = [],  # resolution needed?
                 active_potential_winnings: int = 50,
                 active_winnings: int = 0,
                 all_in_status: bool = False,
                 navigation_id: str = 'W'):
        self.min_deposit = min_deposit
        self.deposit_multiples = deposit_multiples
        self.initial_user_pot = initial_user_pot
        self.active_user_pot = active_user_pot
        self.min_top_up = min_top_up
        self.top_up_multiples = top_up_multiples
        self.active_top_up = active_top_up
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

    def roulette_setup(self):
        play_setup = RouletteInitiator(min_deposit=self.min_deposit, deposit_multiples=self.deposit_multiples)
        play_setup.game_initiator()
        initial_deposit = play_setup.deposit_amount()
        self.initial_user_pot = initial_deposit
        self.active_user_pot = initial_deposit

    def roulette_loop(self):
        """Method to loop over all game components, based on the navigation_id re-determined at end"""

        while True:
            # wheel selection
            if self.navigation_id in navigation_dict['from_wheel_selection']:
                """i.e. if user chose to change wheel after their bet, or this is the first loop."""
                # Could maybe take the wheel choice method out of game initiation as not really relevant to min/max depo
                play_setup = RouletteInitiator(min_deposit=self.min_deposit, deposit_multiples=self.deposit_multiples)
                self.active_wheel_id = play_setup.wheel_choice()

            # bet selection
            if self.navigation_id in navigation_dict['from_bet_selection']:
                """i.e. if user chose to change wheel or change bet category, or this is the first loop.
                or used because if they changed the wheel then also need to change bet category"""
                bet_selection = BetSelector(wheel_id=self.active_wheel_id, player_funds=self.active_user_pot)
                self.active_bet_cat = bet_selection.choose_bet_category()
                self.active_bet_type_id = bet_selection.choose_bet_type(bet_cat=self.active_bet_cat)

            # stake quantification - use of bet_selection from previous if maybe a bit unideal
            if self.navigation_id in navigation_dict['from_stake_quantification']:
                """i.e. if user chose to change wheel or bet type or stake amount."""
                bet_selection = BetSelector(wheel_id=self.active_wheel_id, player_funds=self.active_user_pot)
                self.active_stake, self.all_in_status = bet_selection.choose_stake_amount(
                    bet_type=self.active_bet_type_id)

            # Bet placing up to immediately before outcome evaluation
            if self.navigation_id in navigation_dict['from_bet_choice']:
                """i.e. if user chose to change wheel or bet type or stake amount or bet choice."""
                bet_placer = RouletteWheelWagers(stake=self.active_stake, bet_type_id=self.active_bet_type_id,
                                                 wheel_id=self.active_wheel_id)
                self.active_bet_choice, self.active_potential_winnings = bet_placer.place_bet()
                self.active_winning_slots = bet_placer.get_winning_slots(player_bet=self.active_bet_choice)

            # Bet evaluation
            if self.navigation_id in navigation_dict['from_bet_evaluation']:
                """i.e. if user chose to change wheel or bet type or stake amount or bet choice or just repeat bet."""
                self.active_user_pot -= self.active_stake  # included here if user does a repeat bet
                bet_evaluater = BetEvaluation(potential_winnings=self.active_potential_winnings,
                                              winning_slots=self.active_winning_slots,
                                              user_pot=self.active_user_pot,
                                              wheel_id=self.active_wheel_id)
                self.active_winnings = bet_evaluater.evaluate_bet()
                self.active_user_pot += self.active_winnings

            # Establish game continuation criteria
            if self.all_in == True:
                sys.exit(f"Game over. Your final pot is {self.active_user_pot}")
            continuation = RouletteContinuation(initial_user_pot=self.initial_user_pot,
                                                user_pot=self.active_user_pot,
                                                min_top_up=self.min_top_up,
                                                top_up_multiples=self.top_up_multiples)
            self.active_top_up, self.navigation_id = continuation.game_continuation_steps()
            self.active_user_pot += self.active_top_up
