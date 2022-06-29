"""
Module containing:
The WheelAndBetConstructor class, which is used to:
- instantiate a RouletteWheel using the data in storage (for a European/American etc.);
- instantiate specific subclasses of the RouletteBet (ColoursBet, StraightUpBet etc.) using the data in storage.
"""

# Standard library imports
from enum import Enum
import logging

# Local application imports
from games.roulette.app.roulette_wheel_base_class import RouletteWheelParameters, RouletteWheel, WHEEL_TYPES
from games.roulette.app.roulette_bet_base_class import RouletteBetParameters, BET_TYPES
from games.roulette.constants.wheel_constants import WheelParameters
from games.roulette.constants.bet_constants import WheelBetParameters
from games.roulette.definitions.bet_type_defns import BetTypeOptions


class WheelAndBetConstructor:
    """
    Class to look up wheel and bet parameters based on their names,
    and instantiate the relevant wheel/bet objects
    """

    def __init__(self,
                 wheel_parameters_look_up=WheelParameters,
                 wheel_construction_object=RouletteWheel,
                 bet_parameters_look_up=WheelBetParameters,
                 bet_object_look_up: Enum = BetTypeOptions):
        self.wheel_parameters_look_up = wheel_parameters_look_up
        self.wheel_construction_object = wheel_construction_object
        self.bet_parameters_look_up = bet_parameters_look_up
        self.bet_object_look_up = bet_object_look_up

    def get_wheel_from_wheel_name(self, wheel_name: str) -> WHEEL_TYPES:
        """
        Method to take the wheel_name, look_up the relevant parameters, and then instantiate the relevant live wheel
        object
        Parameters: wheel_name - the name of the desired playing wheel (parameters)
        Returns: an instance of the construction object (RouletteWheel/RouletteWheelUser),
        which then has the instance attribute "parameters" defined, using the RouletteWheelParameters dataclass
        """
        try:
            wheel_parameters: RouletteWheelParameters = getattr(self.wheel_parameters_look_up, wheel_name)
            wheel = self.wheel_construction_object(parameters=wheel_parameters)
            logging.info(f"{wheel_name} {self.wheel_construction_object.__name__} instantiated from its parameters.")
            return wheel
        except AttributeError:
            logging.exception(
                f"Exception occurred when instantiating {wheel_name} {self.wheel_construction_object.__name__}.")
            raise AttributeError(
                f"Invalid wheel bet_type_name: {wheel_name} passed to {self.wheel_parameters_look_up}, in method"
                f"'get_wheel_from_wheel_name'")

    def get_bet_type_from_bet_type_name(self, wheel_name: str, bet_type_name: str) -> BET_TYPES:
        """
        Method to take the wheel and bet name and return a live bet object (subclass).


        Parameters: wheel_name - the name of the playing wheel (that has already been selected). The wheel name is
        needed because the min/max bet parameters can be specific to each wheel.
        bet_type_name - the name of the bet that is being looked up and instantiated

        Returns: A subclass of Bet which is a fully defined bet class (i.e. includes bet placing), and is defined in
        bet_type_defns or bet_type_defns_user depending on the look_up Enum

        Note the purpose of this remains that the user enters a single letter, although it's not a UI facing method
        """
        try:
            bet_type_parameters: RouletteBetParameters = getattr(
                getattr(self.bet_parameters_look_up, wheel_name),  # get parameters specific to the given wheel
                bet_type_name)  # get parameters specific to the given bet
            bet_type_object = getattr(self.bet_object_look_up, bet_type_name).value
            bet_type = bet_type_object(fixed_parameters=bet_type_parameters)  # sets bet_type_name, min bet and max bet
            logging.info(f"{bet_type_name} instantiated from its parameters.")
            return bet_type
        except AttributeError:
            logging.exception(f"Exception occurred when instantiating {bet_type_name}.")
            raise AttributeError(f"Invalid bet type {bet_type_name} passed to {self.bet_object_look_up} "
                                 f"in get_bet_type_from_bet_type_name")
