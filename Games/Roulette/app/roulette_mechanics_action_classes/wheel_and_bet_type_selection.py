#  TODO change the look up methods to not be from a dictionary
from Games.Roulette.definitions.bet_type_defns import BET_TYPES
from Games.Roulette.definitions.wheel_defns import WHEEL_TYPES


class WheelAndBetTypeSelector:
    """Class to look up wheel and bet objects based on their ids, and also to determine all in status"""

    def __init__(self,
                 wheel_look_up: dict,
                 bet_type_look_up: dict):
        self.wheel_look_up = wheel_look_up
        self.bet_type_look_up = bet_type_look_up

    def get_wheel_from_wheel_id(self, wheel_id: str) -> WHEEL_TYPES:
        """
        Method to take the wheel_id and return a live wheel object (subclass).
        Parameters: wheel_id - this is a string, e.g. 'E' in the case of the european wheel.
        Returns: a subclass of RouletteWheel, which has all the instance attributes defined (e.g. Euro_wheel().
        """
        if wheel_id in self.wheel_look_up:
            wheel = self.wheel_look_up[wheel_id]
            return wheel
        else:
            raise NameError(f"No wheel with id {wheel_id} found.")

    def get_bet_type_from_bet_type_id(self, bet_type_id: str) -> BET_TYPES:
        """
        Method to take the bet_type_id and return a live bet object (subclass).
        Parameters: bet_type_id - string, e.g. 'C' which represents ColoursBet subclass of Bet
        Returns: A subclass of Bet which is a fully defined bet class (i.e. includes bet placing).
        """
        if bet_type_id in self.bet_type_look_up:
            bet_type = self.bet_type_look_up[bet_type_id]
            return bet_type
        else:
            raise NameError(f"No bet type with id {bet_type_id} found.")
