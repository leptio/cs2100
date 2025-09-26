"""Initializes function to map any function to a list"""
from typing import TypeVar, List, Callable
T = TypeVar('T')
R = TypeVar('R')

def custom_map(original: List[T], mapper: Callable[[T], R]) -> List[R]:
    """Returns a copy of the list containing elements converted using the mapper
    
    Parameters
    ----------
    original : List[T]
        The original list
    mapper: Callable[[T], R]
        The function to convert elements from the original list to the new list

    Returns
    ----------
    List[R]
        A new list with the mapped elements
    """
    #List comprehension
    return [mapper(i) for i in original]


def sort_by_number(x:int) -> int:
    """Adds 4 to a number"""
    return x+4

if __name__ == "__main__":
    print(custom_map([1,2,3], lambda x: x+1))
    print(custom_map([1,2,3], lambda x: str(x)))
    print(custom_map([1,4,5], sort_by_number))
    print(custom_map(['1','2','3'], lambda x: int(x)+2))
