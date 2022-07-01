"""
Module contents:
- The UI class of each of the bets defined in bet_type_defns - these are the classes that allow users to interact with
each bet type object. Each class uses multiple inheritance from the non-UI definition of that bet object (e.g.
ColoursBet) and from RouletteBetUser. This is so that it has both the bet type specific logic and user interaction
logic already implemented, meaning minimal logic needs to be added for each bet.
The bet type definitions here just implement the abstract methods of the RouletteBetUser class.
- Enum of all users bet types available - these are then imported into the UI application

To define a new bet, first go to roulette->strategies->bet_type_defns
"""

# Standard library imports
from enum import Enum

# Local application imports
from games.roulette.app.roulette_bet_base_class import RouletteBetParameters
from games.roulette.definitions.bet_type_defns import ColoursBet, StraightUpBet, SplitBet, HighLowBet, OddsEvensBet, \
    CornersBet
from games.roulette.app.roulette_wheel_base_class import WHEEL_TYPES
from games.roulette.constants.game_constants import Colour, ColourPrompts
from games.roulette.constants.bet_constants import HighLowBetOptions, OddsEvensBetOptions

# Local application UI imports
from user_interface.games.roulette.app.roulette_bet_base_class_user import RouletteBetUser


##########
# Outside Bets
##########
class ColoursBetUser(ColoursBet, RouletteBetUser):
    """Class for navigating the user to place a colours bet"""

    def __init__(self,
                 fixed_parameters: RouletteBetParameters,
                 stake: int = None,
                 bet_choice: Colour = None,
                 win_criteria: list[int] = None,
                 payout: int = None,
                 playing_wheel: WHEEL_TYPES = None,
                 bet_choice_string_rep: str = None):
        super(RouletteBetUser, self).__init__(fixed_parameters, stake, bet_choice, win_criteria, payout, playing_wheel)
        self.bet_choice_string_rep = bet_choice_string_rep

    def determine_valid_bet_choices_text(self):
        """"Returns: a string of all the valid colours bet options (i.e. excluding bias colour)"""
        colour_list = [colour.name for colour in super().determine_valid_bet_choices()]
        colour_options_text = ", ".join([getattr(ColourPrompts, colour).value for colour in colour_list])
        return colour_options_text

    def get_user_bet_choice(self) -> Colour:
        """
        Method to define the user's bet choice - they are required to enter a valid colour_id on the given wheel.
        Returns: user colour choice (as a member of the Colour Enum, e.g. Colour.RED
        """
        colour_options: set[Colour] = super().determine_valid_bet_choices()
        colour_options_text: str = self.determine_valid_bet_choices_text()
        while True:
            colour_choice = input(f"What colour would you like to bet on?\n{colour_options_text}\n--->").upper()
            try:
                colour_choice = Colour(colour_choice)
                if colour_choice in colour_options:
                    return colour_choice
                else:
                    print(f"{colour_choice} not a valid choice, please try again")
                    continue
            except (ValueError, AttributeError):
                print(f"{colour_choice} not a valid choice, please try again!")

    def get_bet_choice_string_rep(self) -> str:
        """String representation of the bet choice that has been made for feeding back to the user"""
        colour: str = getattr(self.bet_choice, "name").lower()
        return colour + " colours bet"  # on a ...


class HighLowBetUser(HighLowBet, RouletteBetUser):
    """Class for navigating the user to place a high low bet"""

    def __init__(self,
                 fixed_parameters: RouletteBetParameters,
                 stake: int = None,
                 bet_choice: HighLowBetOptions = None,
                 win_criteria: list[int] = None,
                 payout: int = None,
                 playing_wheel: WHEEL_TYPES = None,
                 bet_choice_string_rep: str = None):
        super(RouletteBetUser, self).__init__(fixed_parameters, stake, bet_choice, win_criteria, payout, playing_wheel)
        self.bet_choice_string_rep = bet_choice_string_rep

    def determine_valid_bet_choices_text(self):
        """This method is superfluous for a split bet"""
        raise NotImplementedError("HighLowBetUser's determine_valid_bet_choices_text method called unintentionally")

    def get_user_bet_choice(self) -> (int, int):
        """
        Method to define the user's bet choice.
        """
        while True:
            choice = input(f"What type of bet would you like to place?\n"
                           f"{HighLowBetOptions.PROMPT.value}\n--->").upper()
            try:
                bet_choice = HighLowBetOptions(choice)
                if bet_choice in self.determine_valid_bet_choices():
                    return bet_choice
                else:
                    continue
            except (ValueError, AttributeError):
                print(f"({choice} is not a valid choice for a high or low bet, please try again")

    def get_bet_choice_string_rep(self) -> str:
        """String representation of the bet choice that has been made for feeding back to the user"""
        high_low = self.bet_choice.name.lower()
        return f"{high_low} bet"  # On a...


class OddsEvensBetUser(OddsEvensBet, RouletteBetUser):
    """Class for navigating the user to place a high low bet"""

    def __init__(self,
                 fixed_parameters: RouletteBetParameters,
                 stake: int = None,
                 bet_choice: OddsEvensBetOptions = None,
                 win_criteria: list[int] = None,
                 payout: int = None,
                 playing_wheel: WHEEL_TYPES = None,
                 bet_choice_string_rep: str = None):
        super(RouletteBetUser, self).__init__(fixed_parameters, stake, bet_choice, win_criteria, payout, playing_wheel)
        self.bet_choice_string_rep = bet_choice_string_rep

    def determine_valid_bet_choices_text(self):
        """This method is superfluous for a split bet"""
        raise NotImplementedError("OddsEvensBetUser's determine_valid_bet_choices_text method called unintentionally")

    def get_user_bet_choice(self) -> (int, int):
        """
        Method to define the user's bet choice.
        """
        while True:
            choice = input(f"What type of bet would you like to place?\n"
                           f"{OddsEvensBetOptions.PROMPT.value}\n--->").upper()
            try:
                bet_choice = OddsEvensBetOptions(choice)
                if bet_choice in self.determine_valid_bet_choices():
                    return bet_choice
                else:
                    continue
            except (ValueError, AttributeError):
                print(f"({choice} is not a valid choice for a odds or evens bet, please try again")

    def get_bet_choice_string_rep(self) -> str:
        """String representation of the bet choice that has been made for feeding back to the user"""
        odd_even = self.bet_choice.name.lower()
        return f"{odd_even} bet"  # On a...


##########
# Inside Bets
##########

class StraightUpBetUser(StraightUpBet, RouletteBetUser):
    """Class for navigating the user to place a straight up bet"""

    def __init__(self,
                 fixed_parameters: RouletteBetParameters,
                 stake: int = None,
                 bet_choice: Colour = None,
                 win_criteria: list[int] = None,
                 payout: int = None,
                 playing_wheel: WHEEL_TYPES = None,
                 bet_choice_string_rep: str = None):
        super(RouletteBetUser, self).__init__(fixed_parameters, stake, bet_choice, win_criteria, payout, playing_wheel)
        self.bet_choice_string_rep = bet_choice_string_rep

    def determine_valid_bet_choices_text(self):
        """
        Returns: text string describing the numbers of the roulette wheel
        Example output form: '0 to 36 (inclusive)'
        Note this would need to change if defining a roulette wheel which skips numbers
        """
        options_range: range = self.determine_valid_bet_choices()
        min_number = min(options_range)
        max_number = max(options_range)
        return f"{min_number} to {max_number} (inclusive)"

    def get_user_bet_choice(self) -> int:
        """
        Method to define the user's bet choice - they must enter an adjacent pair of numbers on the given board.
        Returns: user slots choice (as an int, example: 15).
        """
        number_options_range = super().determine_valid_bet_choices()
        number_options_text = self.determine_valid_bet_choices_text()
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

    def get_bet_choice_string_rep(self) -> str:
        """String representation of the bet choice that has been made for feeding back to the user"""
        return "straight up bet on " + str(self.bet_choice)  # on a ...


class SplitBetUser(SplitBet, RouletteBetUser):
    """Class for navigating the user to place a split bet"""

    def __init__(self,
                 fixed_parameters: RouletteBetParameters,
                 stake: int = None,
                 bet_choice: (int, int) = None,
                 win_criteria: list[int] = None,
                 payout: int = None,
                 playing_wheel: WHEEL_TYPES = None,
                 bet_choice_string_rep: str = None):
        super(RouletteBetUser, self).__init__(fixed_parameters, stake, bet_choice, win_criteria, payout, playing_wheel)
        self.bet_choice_string_rep = bet_choice_string_rep

    def determine_valid_bet_choices_text(self):
        """This method is superfluous for a split bet"""
        raise NotImplementedError("SplitBetUser's determine_valid_bet_choices_text method called unintentionally")

    def get_user_bet_choice(self) -> (int, int):
        """
        Method to define the user's bet choice - they are required to enter a valid slot number on the given wheel.
        Returns: user slots choice (as an int, example: 15).
        """
        while True:
            print(self.playing_wheel.generate_board_string_rep())
            int_one_str = input("Please enter the first number for the split bet\n--->")
            int_two_str = input("Please enter the second number for the split bet\n--->")
            try:
                int_one = int(int_one_str)
                int_two = int(int_two_str)
                if super().determine_valid_bet_choices(int_one=int_one, int_two=int_two):
                    return int_one, int_two
                else:
                    print(f"({int_one_str}, {int_two_str}) is not a valid split bet, please try again.\n"
                          f"Split bets must be placed on neighbouring tiles on the board")
            except (ValueError, TypeError):
                print(f"({int_one_str}, {int_two_str}) is not a valid split bet, please try again"
                      f"Split bets must be placed on neighbouring tiles on the board")

    def get_bet_choice_string_rep(self) -> str:
        """String representation of the bet choice that has been made for feeding back to the user"""
        int_one = self.bet_choice[0]  # bet_choice is of type (int, int)
        int_two = self.bet_choice[1]
        return f"split bet on the edge between: {int_one} and {int_two}"  # on a ...


class CornersBetUser(CornersBet, RouletteBetUser):
    """Class for navigating the user to place a corners bet"""

    def __init__(self,
                 fixed_parameters: RouletteBetParameters,
                 stake: int = None,
                 bet_choice: list[int] = None,
                 win_criteria: list[int] = None,
                 payout: int = None,
                 playing_wheel: WHEEL_TYPES = None,
                 bet_choice_string_rep: str = None):
        super(RouletteBetUser, self).__init__(fixed_parameters, stake, bet_choice, win_criteria, payout, playing_wheel)
        self.bet_choice_string_rep = bet_choice_string_rep

    def determine_valid_bet_choices_text(self):
        """This method is superfluous for a corner bet"""
        raise NotImplementedError("Corner bet's determine_valid_bet_choices_text method called unintentionally")

    def get_user_bet_choice(self) -> (int, int):
        """
        Method to define the user's bet choice - they are required to enter a valid slot number on the given wheel.
        Returns: user slots choice (as an int, example: 15).
        """
        while True:
            print(self.playing_wheel.generate_board_string_rep())
            int_one = self.get_individual_entry(input_number="first")
            int_two = self.get_individual_entry(input_number="second")
            int_three = self.get_individual_entry(input_number="third")
            int_four = self.get_individual_entry(input_number="fourth")
            if super().determine_valid_bet_choices(int_list=[int_one, int_two, int_three, int_four]):
                return [int_one, int_two, int_three, int_four]
            else:
                print(f"({int_one}, {int_two}, {int_three}, {int_four}) "
                      f"is not a valid split bet, please try again.\n"
                      f"Split bets must be placed on neighbouring tiles on the board")
                continue

    @staticmethod
    def get_individual_entry(input_number: str) -> int:
        while True:
            int_input_str = input(f"Please enter the {input_number} number for the corners bet\n--->")
            try:
                int_input = int(int_input_str)
                return int_input
            except (ValueError, TypeError):
                print(f"({int_input_str}) is not a valid tile on the playing board, please try again.")

    def get_bet_choice_string_rep(self) -> str:
        """String representation of the bet choice that has been made for feeding back to the user"""
        int_list: list[int, int, int, int] = self.bet_choice
        return f"corners bet on the corner between: {int_list[0], int_list[1], int_list[2], int_list[3]}"  # on a ...


##########
# Enum for storing all the user bet classes
# Parameters imported live into game so don't instantiate
##########
class BetTypeOptionsUser(Enum):
    COLOURS_BET = ColoursBetUser
    STRAIGHTUP_BET = StraightUpBetUser
    SPLIT_BET = SplitBetUser
    HIGH_LOW_BET = HighLowBetUser
    ODDS_EVENS_BET = OddsEvensBetUser
    CORNERS_BET = CornersBetUser
