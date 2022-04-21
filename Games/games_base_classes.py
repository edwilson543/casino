"""
Contents:
Player (base class)
Bet (base class)
"""
from datetime import datetime
from typing import Union, Any
from abc import abstractmethod


class Player:
    """Class to hold the pot and define interactions with the pot.
    Player has money taken from the pot, and added to the pot"""

    # TODO add an attribute along the lines of 'last played time'
    # and when the player starts the game, update it to datetime.now()
    # then add a method in_game_profit_report, to be used at game continuation
    def __init__(self,
                 player_type: str,  # restrict to 'E', 'G', 'N'
                 name: str,
                 username: str,
                 password: str,
                 initial_pot: int,
                 initial_pot_datetime: datetime,
                 active_pot: int,
                 last_top_up_datetime: datetime,
                 active_session_initial_pot: int = None,
                 active_session_start_time: datetime = None,
                 active_session_top_ups: int = 0,
                 all_in_status: bool = False):
        self.player_type = player_type
        self.name = name
        self.username = username
        self.password = password
        self.initial_pot = initial_pot
        self.initial_pot_datetime = initial_pot_datetime
        self.active_pot = active_pot
        self.last_top_up_datetime = last_top_up_datetime
        self.active_session_initial_pot = active_session_initial_pot
        self.active_session_start_time = active_session_start_time
        self.active_session_top_ups = active_session_top_ups
        self.all_in_status = all_in_status

    ##########
    # Setter methods
    ##########
    def set_initial_pot(self, amount: int):
        self.initial_pot = amount
        self.active_pot = amount
        self.initial_pot_datetime = datetime.now()

    def add_top_up_to_pot(self, amount: int):
        self.active_pot += amount
        self.active_session_top_ups += amount
        self.last_top_up_datetime = datetime.now()

    def add_winnings_to_pot(self, amount: int):
        self.active_pot += amount

    def take_stake_from_pot(self, amount: int):
        self.active_pot -= amount

    def set_name(self, name: str):
        self.name = name

    def set_username(self, username: str):
        self.username = username

    def set_password(self, password: str):
        if len(password) >= 5:
            self.password = password
        else:
            raise ValueError("Password attempted to be set at insufficient length")

    def set_active_session_initial_pot_and_time(self):
        self.active_session_initial_pot = self.active_pot
        self.active_session_start_time = datetime.now()

    def set_all_in_status(self, true_or_false: bool):
        self.all_in_status = true_or_false

    ##########
    # Calculation methods
    ##########

    def calculate_active_session_duration_minutes(self) -> int:
        duration_timedelta = datetime.now() - self.active_session_start_time
        duration_seconds = duration_timedelta.seconds
        duration_minutes = duration_seconds / 60
        return int(round(duration_minutes, 0))

    def calculate_active_session_winnings(self) -> int:
        if self.player_type == 'E':
            return self.active_pot - self.active_session_initial_pot - self.active_session_top_ups
        elif self.player_type in ['G', 'N']:
            return self.active_pot - self.active_session_initial_pot - \
                   self.active_session_top_ups - self.initial_pot

    ##########
    # more UI focused - could separate into UI at some point
    ##########

    def get_active_session_report(self):
        print(f"Your current pot is £{self.active_pot}.\n"
              f"You have been playing for {self.calculate_active_session_duration_minutes()} minute(s), "
              f"during which time you have {self.won_or_lost()}: "
              f"£{abs(self.calculate_active_session_winnings())}.")

    def get_full_status_report(self):
        print(f"You are playing as: {self.name}.\n"
              f"Your current pot is £{self.active_pot}.\n"
              f"You last topped up at {self.last_top_up_datetime}.\n"
              f"Since {str(self.initial_pot_datetime)}, you have {self.won_or_lost()}:"
              f" £{abs(self.active_pot - self.initial_pot)}")

    # lower level UI methods

    def won_or_lost(self):
        if self.calculate_active_session_winnings() > 0:
            return "won"
        else:
            return "lost"


#  TODO is it bad practice to use abstract methods and call them artificially in a setter?
class Bet:
    def __init__(self,
                 min_bet: int,
                 max_bet: int,
                 bet_type_id: str,
                 stake: int,
                 bet_choice: Union[int, str, list],
                 win_criteria: Any,
                 payout: int):
        self.min_bet = min_bet
        self.max_bet = max_bet
        self.bet_type_id = bet_type_id
        self.stake = stake
        self.bet_choice = bet_choice
        self.win_criteria = win_criteria
        self.payout = payout

    ##########
    # Abstract methods
    ##########

    # this is an abstract method but not being implemented until 2 subclasses' time throws an error
    def determine_win_criteria(self, *args, **kwargs):
        """
        Abstract method for calculating the win criteria of a given bet.
        Defined differently for each specific roulette bet (e.g. ColoursBet) in bet_type_defns.
        """
        pass

    @abstractmethod
    def calculate_payout(self, *args, **kwargs):
        """
        Abstract method for calculating the payout for the bet
        Defined in the RouletteBet class for all roulette bets.
        """
        pass

    @abstractmethod
    def evaluate_bet(self, *args, **kwargs):
        """
        Abstract method for evaluating the outcome of the bet
        Defined in the RouletteBet class for all roulette bets.
        """
        pass

    ##########
    # Setter methods for the bet attributes attributes
    # Note that the setters depend on the versions of the above methods which are defined downstream
    ##########

    def set_stake_amount(self, amount: int):
        """Sets the stake attribute of the bet, as long as it's within the min/max interval"""
        if self.min_bet <= amount <= self.max_bet:
            self.stake = amount
        else:
            raise ValueError("Stake amount passed to set_stake_amount outside min/max bet interval")

    def set_bet_choice(self, bet_choice: Union[int, str, list]):
        """Sets the bet choice attribute of the bet"""
        self.bet_choice = bet_choice

    def set_win_criteria(self, win_criteria: Any):
        # Could instead call get_win_criteria here, rather than taking a parameter?
        """
        Sets the win_criteria attribute of the bet, by calling the determine_win_criteria method.
        Note the determine_win_criteria method is defined downstream (in RouletteBet), and the MRO ensures this
        downstream version of the method is called here.
        """
        self.win_criteria = win_criteria

    def set_payout(self, amount: int):
        # Could instead call calculate_payout here, rather than taking a parameter?
        """
        Sets the payout attribute of the bet, by calling the calculate_payout method.
        Note the calculate_payout method is defined downstream (in each subclass of RouletteBet defining a specific bet,
        and the MRO ensures this downstream version of the method is called here.
        """
        self.payout = amount
