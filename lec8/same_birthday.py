"""Check if any two students have the same birthday"""
from typing import Set, Tuple
num_students: int = 10

def has_duplicate_birthday() -> bool:
    """Checks if any student has a duplicate birthday"""
    birthday_set: Set[tuple[int, int]] = set()
    for _ in range(num_students):
        month: int = int(input('Enter month: '))
        day: int = int(input('Enter day: '))
        date: Tuple[int, int] = (month, day)
        if date in birthday_set:
            return True
        else:
            birthday_set.add(date)
    return False

has_duplicate_birthday()