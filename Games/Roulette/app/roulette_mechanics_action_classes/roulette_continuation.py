from Games.Roulette.definitions.game_parameters import threshold_for_top_up_prompt
from Games.Roulette.definitions.navigation_defns import navigation_text, navigation_options
from Games.Roulette.definitions.navigation_defns import navigation_text_low_funds, navigation_options_low_funds
import sys


class RouletteContinuation:
    """
    Class to keep the game going until the user runs out of money or quits.
    We'll need to expand to include play on same wheel, new bet type.
    The purpose will be to map users to where they need to be within the existing mechanics.
    """

    def __init__(self, initial_user_pot: int, user_pot: int, min_top_up: int, top_up_multiples: int, stake: int):
        self.initial_user_pot = initial_user_pot
        self.user_pot = user_pot
        self.min_top_up = min_top_up
        self.top_up_multiples = top_up_multiples
        self.stake = stake

    def game_continuation_steps(self):
        self.keep_playing()
        top_up = self.check_top_up_prompt_worthwhile()
        next_step = self.choose_navigation()
        return top_up, next_step

    # lower level methods

    def keep_playing(self):
        while True:
            proceed = input(f"You are {self.up_or_down()} by £{abs(self.user_pot - self.initial_user_pot)}\n"
                            "Would you like to continue playing, [Y]es or [N]o\n--->").upper()
            if proceed == "N":
                sys.exit(f"Game over.\nYour final pot is £{self.user_pot}\n")
            elif proceed == 'Y':
                break
            else:
                print(f"{proceed} not a valid command, please try again")

    def check_top_up_prompt_worthwhile(self):
        if self.user_pot > threshold_for_top_up_prompt:
            return 0
        else:
            return self.top_up_prompt()

    def choose_navigation(self):
        if self.stake <= self.user_pot:
            nav_text = navigation_text
            nav_options = navigation_options
        else:
            nav_text = navigation_text_low_funds
            nav_options = navigation_options_low_funds
        while True:
            next_step = input(f"What would you like to do?\n{nav_text}\n--->").upper()
            if next_step in nav_options:
                return next_step
            else:
                print(f"{next_step} not a valid command, please try again")

    # lowest level methods

    def top_up_prompt(self):
        """Method to get the user to specify how much they want to top up"""
        while True:
            proceed = input(f"Your pot only contains £{self.user_pot} - "
                            f"would you like to top up?\n[Y]es or [N]o\n--->").upper()
            if proceed == 'Y':
                break
            elif proceed == 'N':
                return 0
            else:
                print("Invalid command, pleas try again")
        while True:
            deposit_amount = input("How much would you like to top up?\n"
                                   f"Top ups are allowed as multiples of £{self.top_up_multiples},"
                                   f"the minimum top up is £{self.min_top_up}. \n--->")
            try:
                top_up = int(deposit_amount.replace("£", ""))  # in case someone types in e.g. £100 rather than 150
                if top_up >= self.min_top_up and top_up % self.top_up_multiples == 0:
                    confirmation = input(f"Are you sure you would like to top up by £{top_up}?\n"
                                         "[Y]es, [N]o \n--->").upper()
                    if confirmation != 'Y':
                        continue
                    print(f"You have deposited £{top_up}.\n Your new pot is £{top_up + self.user_pot}")
                    return top_up
                else:
                    print('Invalid top up amount - please try again and refer to criteria.')
            except ValueError:
                print('Invalid top up amount - please try again and refer to criteria.')

    def up_or_down(self):
        """Method to specify whether the player is winning or losing in the text prompts"""
        if self.user_pot >= self.initial_user_pot:
            return "up"
        elif self.user_pot < self.initial_user_pot:
            return "down"

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
