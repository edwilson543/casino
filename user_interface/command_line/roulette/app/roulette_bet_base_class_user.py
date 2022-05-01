from games.roulette.app.roulette_bet_base_class import RouletteBet
from games.roulette.app.roulette_wheel_base_class import WHEEL_TYPES

from typing import TypeVar, Any
from abc import abstractmethod


class RouletteBetUser(RouletteBet):
    def __init__(self,
                 bet_type_name: str,
                 min_bet: int,
                 max_bet: int,
                 stake: int,
                 bet_choice: Any,  # Varies a lot by bet type
                 win_criteria: list[int],
                 payout: int,
                 playing_wheel: WHEEL_TYPES,
                 bet_choice_string_rep: str):
        super().__init__(bet_type_name, min_bet, max_bet, stake, bet_choice,
                         win_criteria, payout, playing_wheel)
        self.bet_choice_string_rep = bet_choice_string_rep

    @abstractmethod
    def get_user_bet_choice(self):
        """
        Abstract method for getting the bet choice from the user.
        This is defined for each specific bet subclass of RouletteBetUser in bet_type_defns_user
        """
        raise NotImplemented("Call to get_user_bet_choice has referred abstract method in"
                             "RouletteBetUser super class")

    @abstractmethod
    def get_bet_choice_string_rep(self):
        """
        Abstract method for generating a string representation of the bet the user wants to place.
        This is defined for each specific bet subclass of RouletteBetUser in bet_type_defns_user
        """
        raise NotImplemented("Call to get_bet_choice_string_rep has referred abstract method in"
                             "RouletteBetUser super class")

    def choose_stake_amount(self, player_funds) -> int:
        """
        Returns:
        Stake amount, all_in_status, which by default is set to false
        """
        if player_funds < self.min_bet:
            raise ValueError("Player funds have been allowed to drop below min bet")
        while True:
            stake = input("How much would you like to stake?\n"
                          f"Minimum stake: £{self.min_bet}, Maximum stake: £{self.max_bet}, integer stakes only.\n"
                          f"You have £{player_funds} left to play with.\n--->")
            try:
                stake = int(stake.replace("£", ""))  # get rid of the £ sign if the user types one
                if stake > player_funds:
                    print(f"A £{stake} stake exceeds your current funds (£{player_funds}).")
                    continue
                elif self.min_bet <= stake <= self.max_bet:
                    return stake
                else:
                    print("Invalid stake - please try again and refer to bet criteria.")
            except ValueError:
                print('Invalid stake - please try again and refer to bet criteria.')

    def confirm_bet_choice(self) -> bool:
        """
        Method to allow the user to see the payout and stake of an individual bet before confirming their choice.
        Note that this method can only be called after all the attributes called within it have been set, note in
        particular that it's called after temporarily setting the bet_choice.
        Returns:
        bool - True if they have confirmed their bet choice, in which case necessary action is taken, otherwise False,
        in which case the bet is discarded.
        """
        confirmation = input(f"Confirm £{self.stake} stake on a {self.bet_choice_string_rep}?\n"
                             f"Winning this bet would return: "
                             f"£{self.payout}\n"
                             f"[Y]es or [N]o\n--->").upper()
        if confirmation != 'Y':
            return False  # maybe add here an extra loop before they discard their bet
        else:
            print(f"£{self.stake} placed on a {self.bet_choice_string_rep}!")
            return True

    ##########
    # Setter methods for added instance attributes
    ##########
    def set_bet_choice_string_rep(self, bet_choice_string: str):
        self.bet_choice_string_rep = bet_choice_string


##########
# Typevar to be used when referencing user bets in type hints throughout game
##########
USER_BET_TYPES = TypeVar(name="USER_BET_TYPES", bound=RouletteBetUser)
