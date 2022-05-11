"""
Module for defining the utility function to be used throughout command line testing.
The override_input_function_with_input_sequence replaces call to input() in the program with a sequence of inputs.
"""
import functools
from typing import TypeVar

T = TypeVar("T")  # Generic type use in type hints below


def call_count(func):
    """
    Decorator for counting how many times a function has been called. This gets used to track how many times the
    input function has been called, and return a different value base don this count.
    """

    def call_count_wrapper(*args, **kwargs):
        call_count_wrapper.calls += 1
        return func(*args, **kwargs)

    call_count_wrapper.calls = 0
    return call_count_wrapper

def print_replacement_func(*args, **kwargs):
    """Function to replace print with when testing command line game"""
    pass

def override_input_function_with_input_sequence(monkeypatch, input_sequence: list[T]) -> None:
    """
    access_nth_list_value_on_nth_call is curried with the list_of_values, and is then used to override the input
    function. The affect is that calls to input() in the original code are replaced by the nth input in the
    list_of_values.

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

    @call_count
    def access_nth_list_value_on_nth_call(list_of_values: list[T], *args, **kwargs) -> T:
        """
        Inner function is used (rather than a separate function) so that the call_count of the modified input function
        always gets reset to 0 each time input() is modified.

        Parameters:
        list_of_values: As above.

        Returns:
        the nth item in the list_of_values on the nth call for a user input. The decorator allows us to
        know how many times we've called the new_input_func, and thus correctly selects the nth item
        """
        return list_of_values[access_nth_list_value_on_nth_call.calls - 1]

    input_replacement_func = functools.partial(access_nth_list_value_on_nth_call, input_sequence)
    monkeypatch.setattr("builtins.input", input_replacement_func)
    monkeypatch.setattr("builtins.print", print_replacement_func)
