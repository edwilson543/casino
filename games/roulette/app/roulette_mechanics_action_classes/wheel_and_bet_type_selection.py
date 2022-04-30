#  TODO change the look up methods to not be from a dictionary
from games.roulette.definitions.bet_type_defns import BET_TYPES
from games.roulette.app.roulette_wheel_base_class import RouletteWheel, WHEEL_TYPES, WHEEL_PARAMETER_TYPES
from games.roulette.app.roulette_bet_base_class import RouletteBetParameters
from games.roulette.constants.wheel_constants import WheelParameters
from games.roulette.constants.bet_constants import WheelBetParameters
from games.roulette.definitions.bet_type_defns import BetTypeOptions
from dataclasses import asdict
from enum import Enum


# TODO what type hint should be used for the look up? it's an enum of bet/wheel objects
class WheelBoardBetConstructor:
    """
    Class to look up wheel and bet parameters based on their names,
    and instantiate the relevant wheel/bet objects
    """

    def __init__(self,
                 wheel_parameters_look_up=WheelParameters,
                 construction_object=RouletteWheel,
                 bet_parameters_look_up=WheelBetParameters,
                 bet_object_look_up: Enum = BetTypeOptions):
        self.wheel_parameters_look_up = wheel_parameters_look_up
        self.construction_object = construction_object
        self.bet_parameters_look_up = bet_parameters_look_up
        self.bet_object_look_up = bet_object_look_up

    def get_wheel_from_wheel_name(self, wheel_name: str) -> WHEEL_TYPES:
        """
        Method to take the wheel_name, look_up the relevant parameters, and then instantiate the relevant live wheel
        object
        Parameters: wheel_name - the bet_type_name of the desired playing wheel (parameters)
        Returns: an instance of the construction object (RouletteWheel/RouletteWheelUser),
        which has all the instance attributes defined (e.g. Euro_wheel()).
        """
        try:
            wheel_parameters: WHEEL_PARAMETER_TYPES = getattr(self.wheel_parameters_look_up, wheel_name)
            wheel_parameters_dict = asdict(wheel_parameters)  # dict of parameters specific to the named wheel
            wheel = self.construction_object(**wheel_parameters_dict)
            return wheel  # TODO return wheel and board
        except ValueError:
            raise ValueError(f"Inavlid wheel bet_type_name: {wheel_name} passed to {self.wheel_parameters_look_up}, in method"
                             f"'get_wheel_from_wheel_name'")

    def get_bet_type_from_bet_type_name(self, wheel_name: str, bet_type_name: str) -> BET_TYPES:
        """
        Method to take the bet_type_id and return a live bet object (subclass).
        Note the purpose of this remains that the user enters a single letter, although it's not a UI facing method
        Parameters: bet_type_id - string, e.g. 'C' which represents ColoursBet subclass of Bet
        Returns: A subclass of Bet which is a fully defined bet class (i.e. includes bet placing).
        """
        try:
            bet_type_parameters: RouletteBetParameters = getattr(
                getattr(self.bet_parameters_look_up, wheel_name),  # get parameters specific to the given wheel
                bet_type_name)  # get parameters specific to the given bet
            bet_type_parameters_dict = asdict(bet_type_parameters)
            bet_type_object = getattr(self.bet_object_look_up, bet_type_name).value
            bet_type = bet_type_object(**bet_type_parameters_dict)  # sets bet_type_name, min bet and max bet
            return bet_type
        except ValueError:
            raise ValueError(f"Invalid bet type {bet_type_name} passed to {self.bet_object_look_up} "
                             f"in get_bet_type_from_bet_type_name")
