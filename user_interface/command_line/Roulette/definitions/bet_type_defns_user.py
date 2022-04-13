from Games.Roulette.definitions.bet_type_defns import ColoursBet, StraightUpBet
from user_interface.command_line.Roulette.app.roulette_wheel_base_class_user import RouletteWheelUser

"""To define a new bet, first go to Roulette->definitions->bet_type_defns"""
##########
# Navigation parameters
##########
# Define the text strings to display the bet categories available on each wheel
bet_cat_options_text = {'E': "[I]nside, [O]utside", 'A': "[I]nside, [O]utside"}
# Define the dictionaries showing bet types available on each wheel, wihtin each category
bet_cats_and_types = {'E': {'O': ['C'], 'I': ['S']}, 'A': {'O': ['C'], 'I': ['S']}}
# Define the text strings to display for each wheel, once the bet category is selected
bet_type_options_text = {'E': {'O': "[C]olours", 'I': "[S]traight up"},
                         'A': {'O': "[C]olours", 'I': "[S]traight up"}}

##########
# Define 'get_user_bet_choice' method for each user bets
##########
class ColoursBetUser(ColoursBet):
    def __init__(self,
                 min_bet: int = 5,
                 max_bet: int = 50,
                 bet_type_id: str = 'C'):
        super().__init__(min_bet, max_bet, bet_type_id)

    @staticmethod
    def get_user_bet_choice(playing_wheel: RouletteWheelUser):
        """
        Method to define the user's bet choice - they are required to enter a valid colour on the given wheel.
        Returns: user colour choice (as a string, example: 'red').
        Note that bet confirmation is done in the bet_placement_user class, because:
        1) It's generic to all bets
        2) It ideally shows potential bet return, which is not defined here
        """
        while True:
            bet_choice = input(
                f"What colour would you like to bet on?\n{playing_wheel.colour_options}\n--->").upper()
            if bet_choice in playing_wheel.colour_ids:
                bet_choice_colour = playing_wheel.colour_ids[bet_choice]
                return bet_choice_colour
            else:
                print(f"{bet_choice} not a valid choice, please try again")


class StraightUpBetUser(StraightUpBet):
    """Class for defining win criteria and payout for a straight-up bet"""

    def __init__(self,
                 min_bet: int = 10,
                 max_bet: int = 20,
                 bet_type_id: str = 'S'):
        super().__init__(min_bet, max_bet, bet_type_id)

    @staticmethod
    def get_user_bet_choice(playing_wheel: RouletteWheelUser):
        number_options_text = playing_wheel.user_number_options_text()
        number_options_range = playing_wheel.user_number_options_range()
        while True:
            bet_choice = input(f"What number would you like to bet on?\nThe options are {number_options_text}.\n--->")
            try:
                bet_choice_int = int(bet_choice)
                if bet_choice_int in number_options_range:
                    return bet_choice_int
                else:
                    print(f"{bet_choice} is not a valid bet choice, please try again")
            except ValueError:
                print(f"{bet_choice} is not a valid bet choice, please try again")


##########
# Add the newly defined user bet class to the bet_type_options_user dictionary below
##########
bet_type_options_user = {'C': ColoursBetUser(), 'S': StraightUpBetUser()}
