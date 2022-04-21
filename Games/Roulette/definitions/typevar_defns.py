"""
Typevars used to specify bet/wheel types for type hints
e.g. return from the wheel lookup is at most a RouletteWheel, or any subclass of RouletteWheel
"""
from typing import TypeVar
from Games.Roulette.app.roulette_bet_base_class import RouletteBet
from Games.Roulette.app.roulette_bet_base_class import RouletteWheel

WHEEL_TYPES = TypeVar(name="WHEEL_TYPES", bound=RouletteWheel)
BET_TYPES = TypeVar(name="BET_TYPES", bound=RouletteBet)
