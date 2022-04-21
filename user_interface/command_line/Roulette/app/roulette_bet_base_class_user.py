from Games.Roulette.app.roulette_bet_base_class import RouletteBet
from user_interface.command_line.Roulette.definitions.wheel_defns_user import USER_WHEEL_TYPES

from Games.Roulette.definitions.game_parameters import pause_durations  # this should be moved to the UI

from typing import Union
from time import sleep
from sys import exit
from abc import abstractmethod


# Do we want player funds as an attribute or as a parameter?
class RouletteBetUser(RouletteBet):
    def __init__(self,
                 min_bet: int,
                 max_bet: int,
                 bet_type_id: str,
                 stake: int,
                 bet_choice: Union[int, str, list],
                 win_criteria: list[int],
                 payout: int,
                 playing_wheel: USER_WHEEL_TYPES):
        super().__init__(min_bet, max_bet, bet_type_id, stake, bet_choice,
                         win_criteria, payout, playing_wheel)

    @abstractmethod
    def get_user_bet_choice(self):
        """
        Abstract method for getting the bet choice from the user.
        This is defined for each specific bet subclass of RouletteBetUser in bet_type_defns_user
        """
        pass

    def choose_stake_amount(self, player_funds: int) -> (int, bool):
        """
        Parameters: player_funds - the amount of money the current player has in their pot
        Returns: stake_amount (integer within min/max bet), all_in_status (T/F depending on if user is all in"""
        min_bet = self.min_bet
        if player_funds >= min_bet:
            stake, all_in_status = self.choose_stake_amount_funds_exceed_min_bet(player_funds=player_funds)
            return stake, all_in_status
        else:  # TODO Add some feature here to allow user to do a top up instead
            all_in_stake, all_in_status = self.all_in(player_funds=player_funds)
            return all_in_stake, all_in_status

    def confirm_bet_choice(self) -> bool:
        """
        Method to allow the user to see the payout and stake of an individual bet before confirming their choice.
        Note that this method can only be called after all the attributes called within it have been set, note in
        particular that it's called after temporarily setting the bet_choice.
        Returns:
        bool - True if they have confirmed their bet choice, in which case necessary action is taken, otherwise False,
        in which case the bet is discarded.
        """
        confirmation = input(f"Confirm £{self.stake} stake on {self.bet_choice}?\n"
                             f"Winning this bet would return: "
                             f"£{self.payout}\n"
                             f"[Y]es or [N]o\n--->").upper()
        if confirmation != 'Y':
            return False  # maybe add here an extra loop before they discard their bet
        else:
            print(f"£{self.stake} placed on {self.bet_choice}!")
            return True

    def evaluate_user_bet(self) -> int:
        """
        Method to give the user the outcome of their bet based on a spin of the wheel, using the evaluate_bet
        method from the parent class BetPlacementEvaluation
        """
        spin_outcome_num, spin_outcome_col, winnings = self.evaluate_bet()
        self.get_user_to_spin_wheel()
        print("Wheel spinning...")
        sleep(pause_durations['medium'])
        print(f"Ball has landed on {spin_outcome_num}, ({spin_outcome_col.upper()})!")
        if winnings > 0:
            sleep(pause_durations['medium'])
            print(f"Congratulations! You have won £{winnings}!\n")
        elif winnings == 0:
            sleep(pause_durations['medium'])
            print("Better luck next time, your bet did not win.")
        else:
            raise ValueError("Invalid winnings amount encountered in evaluate_user_bet.")
        return winnings

    ##########
    # Lower level methods called in choose_stake_amount
    ##########

    def choose_stake_amount_funds_exceed_min_bet(self, player_funds) -> (int, bool):
        """
        Returns:
        Stake amount, all_in_status, which by default is set to false
        """
        all_in_status = False  # if this method is called, it's because the user isn't going all in
        while True:
            stake = input("How much would you like to stake?\n"
                          f"Minimum stake: £{self.min_bet}, Maximum stake: £{self.max_bet}, integer stakes only.\n"
                          f"You have £{player_funds} left to play with.\n--->")
            try:
                stake = int(stake.replace("£", ""))  # get rid of the £ sign if the user types one
                if stake > player_funds:
                    print(f"A £{stake} stake exceeds your current funds ({player_funds}).")
                    continue
                elif self.min_bet <= stake <= self.max_bet:
                    if self.stake_confirmation(stake=stake):
                        print(f"£{stake} bet placed, time to choose your bet!")
                        return stake, all_in_status
                    else:
                        continue
                else:
                    print('Invalid stake - please try again and refer to bet criteria.')
            except ValueError:
                print('Invalid stake - please try again and refer to bet criteria.')

    @staticmethod
    def all_in(player_funds) -> (int, bool):
        all_in = input(f"The minimum bet exceeds your pot of £{player_funds}.\n"
                       f"Would you like to go all in, [Y]es or [N]o?\n--->").upper()
        while True:
            if all_in == 'Y':
                all_in_status = True
                return player_funds, all_in_status
            elif all_in == 'N':
                exit(f"Game over, your final pot is {player_funds}")
            else:
                print("Invalid options, please try again.")

    ##########
    # Lower level methods called in evaluate_user_bet
    ##########
    @staticmethod
    def get_user_to_spin_wheel():
        """Low level method just to get the user to type spin in the game flow above"""
        while True:
            user_ready = input("Type 'SPIN' to spin the wheel!\n--->").upper()
            if user_ready != "SPIN":
                print("Please try spinning the wheel again.")
                continue
            else:
                break

    ##########
    # Lowest level method called in choose stake amount funds exceed min bet
    ##########

    @staticmethod
    def stake_confirmation(stake: int) -> bool:
        confirmation = input(f"Confirm your stake of £{stake}?\n"
                             "[Y]es, [N]o \n--->").upper()
        if confirmation != 'Y':
            return False
        else:
            return True
