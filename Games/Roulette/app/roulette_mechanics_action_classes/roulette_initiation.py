from Games.Roulette.definitions.wheel_defns import wheel_options, wheel_options_text


class RouletteInitiator:
    """
    Class to initiate the roulette game.
    Methods to get the user to initiate the game, set their initial deposit, and choose the wheel they want to play on
    """

    def __init__(self, min_deposit: int, deposit_multiples: int):
        self.min_deposit = min_deposit
        self.deposit_multiples = deposit_multiples

    # Could maybe define a method here that does all 3 in one?

    def deposit_amount(self):
        """Method to get the user to specify how much they want to deposit."""
        while True:
            deposit_amount = input("How much would you like to deposit to play with?\n"
                                   f"Deposits are allowed as multiples of £{self.deposit_multiples},"
                                   f"the minimum deposit is £{self.min_deposit}. \n--->")
            try:
                user_pot = int(deposit_amount.replace("£", ""))  # in case someone types in e.g. £100 rather than 150
                if user_pot >= self.min_deposit and user_pot % self.deposit_multiples == 0:
                    confirmation = input(f"Are you sure you would like to deposit £{user_pot} to play with?\n"
                                         "[Y]es, [N]o \n--->").upper()
                    if confirmation != 'Y':
                        continue
                    print(f"You have deposited £{user_pot} to play with")
                    return user_pot
                else:
                    print('Invalid deposit amount - please try again and refer to deposit criteria.')
            except ValueError:
                print('Invalid deposit amount - please try again and refer to deposit criteria.')

    def wheel_choice(self):
        """Method to allow the user to input what wheel they would like to play on"""
        while True:
            wheel_choice = input("What wheel would you like to play on?\n"
                                 f"{wheel_options_text}\n--->").upper()  # upper to allow for lower case
            if wheel_choice in list(wheel_options.keys()):
                return wheel_choice
            else:
                print("Invalid wheel choice, please try again")
