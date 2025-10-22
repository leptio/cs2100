from collections.abc import Iterable, Iterator
from typing import List

class Calendar(Iterable[str]):
    def __init__(self, days: List[str]):
        self.days = days

    def __iter__(self) -> Iterator[str]:
        """Returns an iterator that returns every other day this week"""
        return AlternatingDayIterator(self.days)

class AlternatingDayIterator(Iterator[str]):
    def __init__(self, days: List[str]):
        self.days = days
        self.index: int = 0

    def __next__(self) -> str:
        if self.index >= len(self.days):
            raise StopIteration

        value = self.days[self.index]
        self.index += 2
        return value

days = Calendar(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])

for alternating_day in days:
    print(alternating_day)
