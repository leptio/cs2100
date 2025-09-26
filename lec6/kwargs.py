"""Uses kwargs (keyword arguments) to print each argument of a function on a separate line"""

from typing import TypeVar

T = TypeVar('T')

def print_args(**kwargs: T) -> None:
    """Print each argument on a separate line"""
    for argument_name, argument_value in kwargs.items():
        print(f'{argument_name}: {argument_value}')

print_args(a=1,b=2,c=3)
