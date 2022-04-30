#  TODO change the look up methods to not be from a dictionary
from games.roulette.definitions.bet_type_defns import BET_TYPES
from games.roulette.app.roulette_wheel_base_class import WHEEL_TYPES
from games.roulette.constants.bet_constants import BetTypeIds
from games.roulette.app.roulette_wheel_base_class import RouletteWheel
from games.roulette.constants.wheel_constants import WheelParameters
from dataclasses import asdict
from enum import Enum


# TODO what type hint should be used for the look up? it's an enum of bet/wheel objects
class WheelAndBetTypeConstructor:
    """
    Class to look up wheel and bet parameters based on their names,
    and instantiate the relevant wheel/bet objects
    """

    def __init__(self,
                 wheel_parameters_look_up: Enum = WheelParameters,
                 construction_object=RouletteWheel):
        self.wheel_parameters_look_up = wheel_parameters_look_up
        self.construction_object = construction_object

    def get_wheel_from_wheel_name(self, wheel_name: str) -> WHEEL_TYPES:
        """
        Method to take the wheel_name, look_up the relevant parameters, and then instantiate the relevant live wheel
        object
        Parameters: wheel_name - the name of the desired playing wheel (parameters)
        Returns: an instance of the construction object (RouletteWheel/RouletteWheelUser),
        which has all the instance attributes defined (e.g. Euro_wheel()).
        """
        try:
            wheel_parameters = getattr(self.wheel_parameters_look_up, wheel_name).value
            wheel_parameters_dict = asdict(wheel_parameters)  # dict of parameters specific to the named wheel
            wheel = self.construction_object(**wheel_parameters_dict)
            return wheel
        except ValueError:
            raise ValueError(f"Inavlid wheel name: {wheel_name} passed to {self.wheel_parameters_look_up}, in method"
                             f"'get_wheel_from_wheel_name'")

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
        except ValueError:
            raise ValueError(f"User has been allowed to pass invalid bet type id:"
                             f" {bet_type_id} to {bet_type_look_up}.")
