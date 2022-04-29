from games.player_base_class import Player, PlayerType
from games.roulette.definitions.game_parameters import AllGameParameters
from datetime import datetime


class PlayerUser(Player):
    def __init__(self,
                 player_type: PlayerType,
                 name: str,
                 username: str,
                 password: str,
                 active_pot: int,
                 last_top_up_datetime: datetime,
                 active_session_initial_pot: int = None,
                 active_session_start_time: datetime = None,
                 active_session_top_ups: int = 0,
                 all_in_status: bool = False):
        super().__init__(player_type=player_type, name=name, username=username, password=password,
                         active_pot=active_pot,
                         last_top_up_datetime=last_top_up_datetime,
                         active_session_initial_pot=active_session_initial_pot,
                         active_session_start_time=active_session_start_time,
                         active_session_top_ups=active_session_top_ups,
                         all_in_status=all_in_status)

    def get_active_session_report(self):
        print(f"Your current pot is £{self.active_pot}.\n"
              f"You have been playing for {self.calculate_active_session_duration_minutes()} minute(s), "
              f"during which time you have {self.won_or_lost()}: "
              f"£{abs(self.calculate_active_session_winnings())}.")

    def end_session(self):
        print(f"Thanks for playing {self.name}!\n"
              f"Your final pot is £{self.active_pot}.")
        exit()

        ##########
        # lower level methods called in the initial_deposit_or_top_up method above
        ##########

    @staticmethod
    def get_initial_deposit_amount() -> int:
        """
        Method to get users to specify how much they want to initially deposit.
        Returns: An integer, which is the specified desired top up amount.
        """
        min_deposit = AllGameParameters.deposit_parameters.min_deposit
        deposit_multiples = AllGameParameters.deposit_parameters.deposit_multiples
        while True:
            amount = input(
                f"How much would you like to deposit?\nDeposits are allowed as multiples of £"
                f"{deposit_multiples}, the minimum deposit is £{min_deposit}.\n--->")
            try:
                amount_int = int(amount.replace("£", ""))  # e.g. replace '£100' with '100'
                if amount_int >= min_deposit and amount_int % deposit_multiples == 0:
                    confirmation = input(
                        f"Are you sure you would like to deposit £{amount_int} to play with?\n"
                        "[Y]es, [N]o \n--->").upper()
                    if confirmation != 'Y':
                        continue
                    print(f"You have made a deposit of £{amount_int} to play with!")
                    return amount_int
                else:
                    print(f"Invalid deposit amount - please try again and refer to deposit criteria.")
            except ValueError:
                print(f"Invalid deposit amount - please try again and refer to deposit criteria.")

    def check_top_up_scenario(self) -> int:
        """
        Method to check whether the user pot is below the threshold for a top up prompt to be worthwhile,
        and then make a top_up if it is worthwhile/ they have to to keep playing.
        Note that user will be forced to top up by see_if_user_wants_to_top_up in order to continue
        playing, if their pot is below a pre-determined threshold.
        Returns:
        int - the top up amount specified by the user (by default 0)
        """
        low_pot_forced_top_up = AllGameParameters.top_up_parameters.low_pot_forced_top_up
        threshold_for_top_up_prompt = AllGameParameters.top_up_parameters.threshold_for_top_up_prompt
        if self.active_pot > threshold_for_top_up_prompt:
            return 0
        elif threshold_for_top_up_prompt >= self.active_pot > low_pot_forced_top_up:
            if self.see_if_user_wants_optional_top_up():
                return self.get_top_up_amount()
            else:
                return 0
        elif 0 < self.active_pot <= low_pot_forced_top_up:
            if self.see_if_user_wants_forced_top_up():
                return self.get_top_up_amount()
            else:
                self.end_session()

    ##########
    # Method called during check top up worthwhile
    ##########
    @staticmethod
    def get_top_up_amount() -> int:
        """
        Method to get users to specify how much they want to top up by.
        Note if this method is called, it's because the user has said they want to top up.
        Returns: An integer, which is the specified desired top up amount.
        """
        min_top_up = AllGameParameters.top_up_parameters.min_top_up
        top_up_multiples = AllGameParameters.top_up_parameters.top_up_multiples
        while True:
            amount = input(
                f"How much would you like to top up by?\nTop ups are allowed as multiples of £"
                f"{top_up_multiples}, the minimum deposit is £{min_top_up}.\n--->")
            try:
                amount_int = int(amount.replace("£", ""))  # e.g. replace '£100' with '100'
                if amount_int >= min_top_up and amount_int % top_up_multiples == 0:
                    confirmation = input(
                        f"Are you sure you would like to top up by £{amount_int}?\n"
                        "[Y]es, [N]o \n--->").upper()
                    if confirmation != 'Y':
                        continue
                    print(f"You have made a top up of £{amount_int}!")
                    return amount_int
                else:
                    print(f"Invalid top up amount - please try again and refer to top up criteria.")
            except ValueError:
                print(f"Invalid top up amount - please try again and refer to top up criteria.")

    def see_if_user_wants_optional_top_up(self) -> bool:
        """
        Method to get the user to specify if they want to top up, HAVING BEEN GIVEN the top up prompt
        If they have £0 in their pot, they don't have a choice and must top up to continue playing.
        """
        low_pot_forced_top_up = AllGameParameters.top_up_parameters.low_pot_forced_top_up
        threshold_for_top_up_prompt = AllGameParameters.top_up_parameters.threshold_for_top_up_prompt
        while True:
            if low_pot_forced_top_up < self.active_pot <= threshold_for_top_up_prompt:
                print(f"Your pot only contains £{self.active_pot}.")
                proceed = input("Would you like to top up?\n[Y]es, [N]o\n--->").upper()
                if proceed == "Y":
                    return True
                elif proceed == "N":
                    return False
                else:
                    print("Invalid command, please try again.")
            else:
                raise ValueError("Top up prompt attempted to see if user wants to top up,"
                                 "despite pot exceeding threshold for top up prompt.")

    def see_if_user_wants_forced_top_up(self):
        """
        Method to force the user to top up - note it still only returns T/F.
        If it returns F and the user has no active bets, the game will end.
        If it returns F and the user has active bets, they just won't be allowed to add any more bets to current spin.
        """
        while True:
            if 0 < self.active_pot <= AllGameParameters.top_up_parameters.low_pot_forced_top_up:
                proceed = input(f"You only have £{self.active_pot} left in your pot, "
                                "to continue playing you must top up.\nWould you like to top up?\n"
                                "[Y]es, [N]o, (game session will end if you have no active bets)\n--->").upper()
                if proceed == "Y":
                    return True
                elif proceed == "N":
                    return False
                else:
                    print("Invalid command, please try again.")
            else:
                raise ValueError(f"Invalid call of the forced top_up method")

    ##########
    # lower level UI methods
    ##########
    def won_or_lost(self):  # called in get_active_session_report
        if self.calculate_active_session_winnings() > 0:
            return "won"
        else:
            return "lost"
