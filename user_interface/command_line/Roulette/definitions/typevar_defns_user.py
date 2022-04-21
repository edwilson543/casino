"""
Typevars used to specify user bet/wheel types for type hints
e.g. return from the user Uwheel lookup is at most a RouletteWheelUser, or any subclass of RouletteWheel
"""
from typing import TypeVar
from user_interface.command_line.Roulette.app.roulette_bet_base_class_user import RouletteBetUser
from user_interface.command_line.Roulette.app.roulette_wheel_base_class_user import RouletteWheelUser

USER_WHEEL_TYPES = TypeVar(name="USER_WHEEL_TYPES", bound=RouletteWheelUser)
USER_BET_TYPES = TypeVar(name="USER_BET_TYPES", bound=RouletteBetUser)
