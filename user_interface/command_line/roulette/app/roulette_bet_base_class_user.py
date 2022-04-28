from games.roulette.app.roulette_bet_base_class import RouletteBet
from user_interface.command_line.roulette.definitions.wheel_parameters_and_defns_user import USER_WHEEL_TYPES

from typing import Union
from abc import abstractmethod


# Do we want player funds as an attribute or as a parameter?
class RouletteBetUser(RouletteBet):
    def __init__(self,
                 bet_type: str,
                 min_bet: int,
                 max_bet: int,
                 stake: int,
                 bet_choice: Union[int, str, list],
                 win_criteria: list[int],
                 payout: int,
                 playing_wheel: USER_WHEEL_TYPES):
        super().__init__(bet_type, min_bet, max_bet, stake, bet_choice,
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
        else:  # TODO Add some feature here to allow user to do a top up instead, will also need top up method somehow
            all_in_stake, all_in_status = self.go_all_in(player_funds=player_funds)
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
                    print(f"A £{stake} stake exceeds your current funds (£{player_funds}).")
                    continue
                elif self.min_bet <= stake <= self.max_bet:
                    return stake, all_in_status
                else:
                    print("Invalid stake - please try again and refer to bet criteria.")
            except ValueError:
                print('Invalid stake - please try again and refer to bet criteria.')

    @staticmethod
    def go_all_in(player_funds) -> (int, bool):  # TODO sort out all in functionality...
        """
        If the player wants to go all in, returns the player's pot and True.
        If the player doesn't want to go all in, returns False
        """
        all_in = input(f"The minimum bet exceeds your pot of £{player_funds}.\n"
                       f"Would you like to go all in, [Y]es or [N]o?\n--->").upper()
        while True:
            if all_in == "Y":
                all_in_status = True
                return player_funds, all_in_status
            elif all_in == "N":
                exit("Game over.\nYou have insufficient funds to bet and have refused to go all in.")
                #  TODO find an alternative to directly calling sys.exit here - utilise Player method
            else:
                print("Invalid options, please try again.")
