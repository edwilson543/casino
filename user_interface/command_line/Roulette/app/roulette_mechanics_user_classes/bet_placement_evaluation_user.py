from Games.Roulette.app.roulette_wheel_base_class import RouletteWheel
from Games.Roulette.app.roulette_bet_base_class import RouletteBet
from Games.Roulette.app.roulette_mechanics_action_classes.bet_placement_evaluation import BetPlacementEvaluation

from Games.Roulette.definitions.game_parameters import pause_durations

from typing import Union
from time import sleep
import sys


# TODO sort out the type hint error where it's expecting a roulette bet, temporarily added get_user_bet_choice
#  to the roulette bet class
# TODO maybe write some parent methods for stake quantification in the parent class,
#  and use players rather than player funds?
class BetPlacementEvaluationUser(BetPlacementEvaluation):
    """Purpose of this subclass is to inherit the get_winning_slots and get_potential_winnings
    methods from the BetPlacement class, and
    to add the get_user_bet_choice method which is shown below"""

    def __init__(self,
                 bet_type: RouletteBet,
                 stake: int,
                 playing_wheel: RouletteWheel,
                 player_funds: int):
        super().__init__(bet_type, stake, playing_wheel)
        self.player_funds = player_funds

    def choose_stake_amount(self):
        """Returns: Stake amount, all_in_status"""
        min_bet = self.bet_type.min_bet
        if self.player_funds >= min_bet:
            all_in_stake, all_in_status = self.choose_stake_amount_funds_exceed_min_bet()
            return all_in_stake, all_in_status
        else:  # TODO Add some feature here to allow user to do a top up instead
            all_in_stake, all_in_status = self.all_in()
            return all_in_stake, all_in_status

    def get_user_bet_choice(self) -> Union[int, str, list]:
        """gets user to specify their bet (navigation unique to the bet type)
        then uses generic confirmation by displaying potential payout.
        If confirmation is no, they can place a new bet choice."""
        while True:
            bet_choice = self.bet_type.get_user_bet_choice(playing_wheel=self.playing_wheel)
            confirmation = input(f"Confirm £{self.stake} stake on {bet_choice}?\n"
                                 f"Winning this bet would return: £"
                                 f"{self.get_winnings(self.get_winning_slots(bet_choice))}\n"
                                 f"[Y]es or [N]o\n--->").upper()
            if confirmation != 'Y':
                continue
            else:
                print(f"£{self.stake} placed on {bet_choice}!")
                return bet_choice

    def evaluate_user_bet(self, bet_choice: Union[int, str, list]) -> int:
        """
        Method to give the user the outcome of their bet based on a spin of the wheel, using the evaluate_bet
        method from the parent class BetPlacementEvaluation
        """
        spin_outcome_num, spin_outcome_col, winnings = self.evaluate_bet(bet_choice=bet_choice)
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

    def choose_stake_amount_funds_exceed_min_bet(self):
        """
        Returns:
        Stake amount, all_in_status, which by default is set to false
        """
        min_bet = self.bet_type.min_bet
        max_bet = self.bet_type.max_bet
        all_in_status = False  # if this method is called, it's because the user isn't going all in
        while True:
            stake = input("How much would you like to stake?\n"
                          f"Minimum stake: £{min_bet}, Maximum stake: £{max_bet}, integer stakes only.\n"
                          f"You have £{self.player_funds} left to play with.\n--->")
            try:
                stake = int(stake.replace("£", ""))  # get rid of the £ sign if the user types one
                if stake > self.player_funds:
                    print(f"A £{stake} stake exceeds your current funds ({self.player_funds}).")
                    continue
                elif min_bet <= stake <= max_bet:
                    confirmation = input(f"Confirm your stake of £{stake}?\n"
                                         "[Y]es, [N]o \n--->").upper()
                    if confirmation != 'Y':
                        print(f"£{stake} stake placed, time to choose your bet!")
                    return stake, all_in_status
                else:
                    print('Invalid stake - please try again and refer to bet criteria.')
            except ValueError:
                print('Invalid stake - please try again and refer to bet criteria.')

    def all_in(self):
        all_in = input(f"The minimum bet exceeds your pot of £{self.player_funds}.\n"
                       f"Would you like to go all in, [Y]es or [N]o?\n--->").upper()
        while True:
            if all_in == 'Y':
                all_in_status = True
                return self.player_funds, all_in_status
            elif all_in == 'N':
                sys.exit(f"Game over, your final pot is {self.player_funds}")
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
