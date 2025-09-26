"""Defines a class that prints args"""
from typing import TypeVar
T = TypeVar("T")

def print_args(*args: T) -> None:
    """Print each argument on a separate line"""
    for i in range(len(args)):
        print(f"args[{i}] = {args[i]}")
        for item in args:
            print(item)

if __name__ == "__main__":
    print_args(1, 9, 4, 9, 2, 6, 3)