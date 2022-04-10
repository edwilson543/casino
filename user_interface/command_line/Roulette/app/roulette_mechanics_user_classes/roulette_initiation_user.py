from Games.Roulette.definitions.wheel_defns import wheel_options, wheel_options_text

##########
# NOT UPDATED
##########
# Can almost definitely get rid of this, by moving the wheel choice into the bet selection module
class RouletteInitiatorUser:
    """
    Class to initiate the roulette game.
    Methods to get the user to initiate the game, set their initial deposit, and choose the wheel they want to play on
    """

    def __init__(self, min_deposit: int, deposit_multiples: int):
        self.min_deposit = min_deposit
        self.deposit_multiples = deposit_multiples

    def wheel_choice(self):
        """Method to allow the user to input what wheel they would like to play on"""
        while True:
            wheel_choice = input("What wheel would you like to play on?\n"
                                 f"{wheel_options_text}\n--->").upper()  # upper to allow for lower case
            if wheel_choice in list(wheel_options.keys()):
                return wheel_choice
            else:
                print("Invalid wheel choice, please try again")
