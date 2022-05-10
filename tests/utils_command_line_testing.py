import functools
from typing import TypeVar

T = TypeVar("T")

#  TODO move to its own module
def call_count(func):
    """
    Decorator for counting how many times a function has been called. This gets used to track how many times the
    input function has been called.
    """

    def call_count_wrapper(*args, **kwargs):
        call_count_wrapper.calls += 1
        return func(*args, **kwargs)

    call_count_wrapper.calls = 0
    return call_count_wrapper


@call_count
def access_nth_list_value_on_nth_call(user_input_list: list[T], *args, **kwargs) -> T:
    """
    Parameters: input_sequence: A list of the user input sequence we would like to simulate for testing.
    Returns: the nth item in the input_sequence on the nth call for a user input. The decorator allows us to
    know how many times we've called the new_input_func, and thus correctly selects the nth item
    """
    return user_input_list[access_nth_list_value_on_nth_call.calls - 1]


def custom_user_input_func(user_input_list: list[T]) -> functools.partial[T]:
    """
    Parameters: A list of the user input sequence we would like to simulate for testing.
    Returns: A curried version of the new_input_func function with the input_sequence bound as a parameter.
    This return function is then used to override the input function, with the affect that calls to input() in the
    original code are replaced by the nth input in the input_sequence.
    """
    return functools.partial(access_nth_list_value_on_nth_call, user_input_list)

def override_input_function_with_input_sequence(monkeypatch, input_sequence):
    monkeypatch.setattr("builtins.input", custom_user_input_func(user_input_list=input_sequence))
