from Games.Roulette.definitions.bet_type_defns import ColoursBet, StraightUpBet
from Games.Roulette.app.roulette_wheel_base_class import RouletteWheel

"""UI classes that inherit from the relevant class in bet_type_defns.
These classes are to add the UI that allows users to make their bet choice."""


# TODO these could instead just be inherited directly form the Roulette Bet base class?

class ColoursBetUser(ColoursBet):
    def __init__(self,
                 min_bet: int = 5,
                 max_bet: int = 50,
                 bet_type_id: str = 'C'):
        super().__init__(min_bet, max_bet, bet_type_id)

    @staticmethod
    def get_user_bet_choice(playing_wheel: RouletteWheel):
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
            if bet_choice in playing_wheel.colour_ids.keys():
                bet_choice_colour = playing_wheel.colour_ids[bet_choice]
                return bet_choice_colour
            else:
                print(f"{bet_choice} not a valid choice, please try again")


class StraightUpBetUser(StraightUpBet):
    """Class for defining win criteria and payout for a straight up bet"""

    def __init__(self,
                 min_bet: int = 10,
                 max_bet: int = 20,
                 bet_type_id: str = 'S'):
        super().__init__(min_bet, max_bet, bet_type_id)

    @staticmethod
    def get_user_bet_choice(playing_wheel: RouletteWheel):
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


###################
# Add the newly defined user bet class to the bet_type_options dictionary below
###################
bet_type_options_user = {'C': ColoursBetUser(), 'S': StraightUpBetUser()}
