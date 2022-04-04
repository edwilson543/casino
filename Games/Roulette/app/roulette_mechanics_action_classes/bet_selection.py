from Games.Roulette.definitions.bet_type_defns import bet_cats_and_types, bet_cat_options_text
from Games.Roulette.definitions.bet_type_defns import bet_type_options_text, bet_type_min_max_bet
import sys


class BetSelector:
    """class to allow users to select the type of bet to place
    note note yet to place the bet"""

    def __init__(self, wheel_id: str, player_funds: int):
        self.wheel_id = wheel_id
        self.player_funds = player_funds

    def choose_bet_category(self):
        while True:
            bet_cat = input("What category of bet would you like to place?"
                            f"\n{bet_cat_options_text[self.wheel_id]}\n--->").upper()
            if bet_cat in list(bet_cats_and_types[self.wheel_id].keys()):
                return bet_cat
            else:
                print("Not a valid bet category, try again")

    def choose_bet_type(self, bet_cat):
        while True:
            bet_type = input("What category of bet would you like to place?"
                             f"\n{bet_type_options_text[self.wheel_id][bet_cat]}\n--->").upper()
            if bet_type in bet_cats_and_types[self.wheel_id][bet_cat]:
                return bet_type
            else:
                print("Not a valid bet type, try again")

    def choose_stake_amount(self, bet_type):
        """Returns: Stake amount, all_in_status"""
        min_stake = bet_type_min_max_bet[self.wheel_id][bet_type]['min']
        if self.player_funds < min_stake:  # TODO Add some feature here to allow user to do a top up instead
            all_in_stake, all_in_status = self.all_in()
            return all_in_stake, all_in_status
        else:
            all_in_stake, all_in_status = self.choose_stake_amount_funds_exceed_min_bet(bet_type=bet_type)
            return all_in_stake, all_in_status

    def choose_stake_amount_funds_exceed_min_bet(self, bet_type):
        """
        Returns:
        Stake amount, all_in_status, which by default is set to false
        """
        min_stake = bet_type_min_max_bet[self.wheel_id][bet_type]['min']
        max_stake = bet_type_min_max_bet[self.wheel_id][bet_type]['max']
        all_in_status = False
        while True:
            stake = input("How much would you like to stake?\n"
                          f"Minimum stake: £{min_stake}, Maximum stake: £{max_stake}, integer stakes only.\n"
                          f"You have £{self.player_funds} left to play with.\n--->")
            try:
                stake = int(stake.replace("£", ""))  # get rid of the £ sign if the user types one
                if stake > self.player_funds:
                    print(f"A £{stake} stake exceeds your current funds ({self.player_funds}).")
                    continue
                elif min_stake <= stake <= max_stake:
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

    # def top_up(self):
    #     """Method to get the user to specify how much they want to top up"""
    #     while True:
    #         deposit_amount = input("How much would you like to top up?\n"
    #                                f"Top ups are allowed as multiples of £{self.top_up_multiples},"
    #                                f"the minimum top up is £{self.min_top_up}. \n--->")
    #         try:
    #             top_up = int(deposit_amount.replace("£", ""))  # in case someone types in e.g. £100 rather than 150
    #             if top_up >= self.min_top_up and top_up % self.top_up_multiples == 0:
    #                 confirmation = input(f"Are you sure you would like to top up by £{top_up}?\n"
    #                                      "[Y]es, [N]o \n--->").upper()
    #                 if confirmation != 'Y':
    #                     continue
    #                 print(f"You have deposited £{top_up}.\nYour pot now contains £{self.user_pot + top_up}")
    #                 return top_up
    #             else:
    #                 print('Invalid top up amount - please try again and refer to criteria.')
    #         except ValueError:
    #             print('Invalid top up amount - please try again and refer to criteria.')
