from typing import TypeVar, List
T = TypeVar('T')

def get_first(list: List[T]) -> T:

    if len(list) > 0:
        return list[0]
    else:
        raise ValueError