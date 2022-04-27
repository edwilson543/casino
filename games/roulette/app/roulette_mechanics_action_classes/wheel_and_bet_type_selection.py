#  TODO change the look up methods to not be from a dictionary
from games.roulette.definitions.bet_type_defns import BET_TYPES
from games.roulette.definitions.wheel_parameters_and_defns import WHEEL_TYPES
from games.roulette.definitions.wheel_parameters_and_defns import WheelIds
from games.roulette.definitions.bet_parameters import BetTypeIds

# TODO what type hint should be used for the look up? it's an enum of bet/wheel objects
class WheelAndBetTypeSelector:
    """Class to look up wheel and bet objects based on their ids, and also to determine all in status"""

    @staticmethod
    def get_wheel_from_wheel_id(wheel_id: str, wheel_look_up) -> WHEEL_TYPES:
        """
        Method to take the wheel_id and return a live wheel object (subclass).
        Note the purpose of this remains that the user enters a single letter, although it's not a UI facing method
        Parameters: wheel_id - this is a string, e.g. 'E' in the case of the european wheel.
        Returns: a subclass of RouletteWheel, which has all the instance attributes defined (e.g. Euro_wheel()).
        """
        try:
            wheel_name = WheelIds(wheel_id).name
            wheel = getattr(wheel_look_up, wheel_name).value
            return wheel
        except AttributeError:
            raise AttributeError(f"User has been allowed to pass invalid wheel id:"
                                 f" {wheel_id} to {wheel_look_up}.")
    @staticmethod
    def get_bet_type_from_bet_type_id(bet_type_id: str, bet_type_look_up) -> BET_TYPES:
        """
        Method to take the bet_type_id and return a live bet object (subclass).
        Note the purpose of this remains that the user enters a single letter, although it's not a UI facing method
        Parameters: bet_type_id - string, e.g. 'C' which represents ColoursBet subclass of Bet
        Returns: A subclass of Bet which is a fully defined bet class (i.e. includes bet placing).
        """
        try:
            bet_type_name = BetTypeIds(bet_type_id).name
            bet_type = getattr(bet_type_look_up, bet_type_name).value
            return bet_type
        except AttributeError:
            raise AttributeError(f"User has been allowed to pass invalid bet type id:"
                                 f" {bet_type_id} to {bet_type_look_up}.")
