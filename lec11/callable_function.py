from typing import Callable

def my_function() -> None:
    print('um hi')
    def __name__() -> str:
        return "Named"

def execute_multiple(func: Callable[[], None], times:int) -> None:
    """Executes the function func times number of times"""
    for _ in range(times):
        func()

execute_multiple(my_function, 3)
execute_multiple(lambda: print("sd"), 2)
