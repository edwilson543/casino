"""
Module for defining the utility function to be used throughout command line testing.
The override_input_function_with_input_sequence replaces call to input() in the program with a sequence of inputs.
"""

from typing import TypeVar, Generator

T = TypeVar("T")  # Generic type use in type hints below


def print_replacement_func(*args, **kwargs):
    """Function to replace print with when testing command line game - a function that does nothing."""
    pass


def override_input_function_with_input_sequence(monkeypatch, input_sequence: list[T]) -> None:
    """
    We replace the input function with a call to next on a generator that generates the desired input sequence.
    Here a generator expression is used because it's more succinct, however a generator function could equivalently be
    used, which yields the nth value in the input_sequence.

    Parameters:
    ----------
    monkeypatch: pytest tool used to override functions when testing
    list_of_values: The list of the user input sequence we would like to test a given method with

    Returns:
    ----------
    None

    Outcomes:
    ----------
    input() function calls are overriden by list_of_values
    print() function calls are nullified
    """

    generator: Generator[T] = (value for value in input_sequence)

    def next_nth_value(*args, **kwargs) -> T:
        return next(generator)

    monkeypatch.setattr("builtins.input", next_nth_value)
    monkeypatch.setattr("builtins.print", print_replacement_func)
