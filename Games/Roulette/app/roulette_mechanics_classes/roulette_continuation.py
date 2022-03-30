from Games.Roulette.definitions.game_parameters import threshold_for_top_up_prompt


#TODO write this class so that it does the leg work for looping the game, navigating user to relevant stage
#ideally all in one method?
class RouletteContinuation:
    """
    Class to keep the game going until the user runs out of money or quits.
    We'll need to expand to include play on same wheel, new bet type.
    The purpose will be to map users to where they need to be within the existing mechanics.
    """

    def __init__(self, user_pot: int, min_top_up: int, top_up_multiples: int):
        self.min_top_up = min_top_up
        self.top_up_multiples = top_up_multiples
        self.user_pot = user_pot

    def keep_playing(self):
        """input = Y/N keep play"""
        pass

    def choose_next_steps(self):
        while True:
            next_step = input("")
        pass

    def top_up(self):
        """Method to get the user to specify how much they want to top up"""
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
                    print(f"You have deposited £{top_up}.\nYour pot now contains £{self.user_pot + top_up}")
                    return top_up
                else:
                    print('Invalid top up amount - please try again and refer to criteria.')
            except ValueError:
                print('Invalid top up amount - please try again and refer to criteria.')

    def check_top_up_prompt_worthwhile(self):
        if self.user_pot > threshold_for_top_up_prompt:
            return False
        else:
            return True

    def top_up_prompt(self):
        """Method to get the user to specify how much they want to top up"""
        while True:
            proceed = input(f"Your pot only contains £{self.user_pot}\n"
                            f"Would you like to top up?\n [Y]es or [N]o\n--->").upper()
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
                    print(f"You have deposited £{top_up}.")
                    return top_up
                else:
                    print('Invalid top up amount - please try again and refer to criteria.')
            except ValueError:
                print('Invalid top up amount - please try again and refer to criteria.')
