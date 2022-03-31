from Games.Roulette.definitions.game_parameters import deposit_parameters, top_up_parameters
from Games.Roulette.app.roulette_mechanics_classes.roulette_initiation import RouletteInitiator
from Games.Roulette.app.roulette_mechanics_classes.bet_selection import BetSelector
from Games.Roulette.app.roulette_mechanics_classes.bet_placement import RouletteWheelWagers
from Games.Roulette.app.roulette_mechanics_classes.bet_evaluation import BetEvaluation
from Games.Roulette.app.roulette_mechanics_classes.roulette_continuation import RouletteContinuation


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
                 active_potential_winnings=50,
                 active_winnings=0,
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
        self.navigation_id = navigation_id

    def play_setup(self):
        play_setup = RouletteInitiator(min_deposit=self.min_deposit, deposit_multiples=self.deposit_multiples)
        play_setup.game_initiator()
        initial_deposit = play_setup.deposit_amount()
        self.initial_user_pot = initial_deposit
        self.active_user_pot = initial_deposit

    def game_loop(self):
        """Method to loop over all game components, based on the navigation_id re-determined at end"""
        # TODO make a dictionary/list of the navigation_ids and what they do, so don't reference directly to strings
        # This could introduce quite  pointless step e.g. 'W' -> 'choose wheel' -> 'W'
        # And also a list of the text command options
        # Perhaps each of the classes that are instantiated within the if loops should first also be done here, or
        # alternatively could become class attributes so they can be called directly

        while True:
            # wheel selection
            if self.navigation_id == 'W':
                """i.e. if user chose to change wheel after their bet, or this is the first loop."""
                # Could maybe take the wheel choice method out of game initiation as not really relevant to min/max depo
                play_setup = RouletteInitiator(min_deposit=self.min_deposit, deposit_multiples=self.deposit_multiples)
                self.active_wheel_id = play_setup.wheel_choice()

            # bet selection
            if self.navigation_id == 'W' or 'BT':
                """i.e. if user chose to change wheel or change bet category, or this is the first loop.
                or used because if they changed the wheel then also need to change bet category"""
                bet_selection = BetSelector(wheel_id=self.active_wheel_id, player_funds=self.active_user_pot)
                self.active_bet_cat = bet_selection.choose_bet_category()
                self.active_bet_type_id = bet_selection.choose_bet_type(bet_cat=self.active_bet_cat)

            # stake quantification - use of bet_selection from previous if maybe a bit unideal
            if self.navigation_id == 'W' or 'BT' or 'S':
                """i.e. if user chose to change wheel or bet type or stake amount."""
                bet_selection = BetSelector(wheel_id=self.active_wheel_id, player_funds=self.active_user_pot)
                self.active_stake = bet_selection.choose_stake_amount(bet_type=self.active_bet_type_id)
                self.active_user_pot -= self.active_stake

            # Bet placing up to immediately before outcome evaluation
            if self.navigation_id == 'W' or 'BT' or 'S' or 'BC':
                """i.e. if user chose to change wheel or bet type or stake amount or bet choice."""
                bet_placer = RouletteWheelWagers(stake=self.active_stake, bet_type_id=self.active_bet_type_id,
                                                 wheel_id=self.active_wheel_id)
                self.active_bet_choice, self.active_potential_winnings = bet_placer.place_bet()
                self.active_winning_slots = bet_placer.get_winning_slots(player_bet=self.active_bet_choice)

            # Bet evaluation
            if self.navigation_id == 'W' or 'BT' or 'S' or 'BC' or 'R':
                """i.e. if user chose to change wheel or bet type or stake amount or bet choice or just repeat bet."""
            bet_evaluater = BetEvaluation(potential_winnings=self.active_potential_winnings,
                                          winning_slots=self.active_winning_slots,
                                          user_pot=self.active_user_pot,
                                          wheel_id=self.active_wheel_id)
            self.active_winnings = bet_evaluater.evaluate_bet()
            self.active_user_pot += self.active_winnings

            # establish game continuation criteria
            """Code here that goes through some continuation steps and sends loop back to relevant place.
            Need to develop, and within roulette continuation"""
            continuation = RouletteContinuation(user_pot=self.active_user_pot,
                                                min_top_up=self.min_top_up,
                                                top_up_multiples=self.top_up_multiples)
            continuation.keep_playing()
            self.active_top_up = continuation.check_top_up_prompt_worthwhile()
            self.active_user_pot += self.active_top_up
