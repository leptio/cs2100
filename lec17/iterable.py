#list, dict, set, tuple, string are all iterable
#integers are NOT iterable
#custom iterator can be defined for custom iteration behavior

#all iterables (iterable protocol) require an __iter__() method returning an iterator
#iterator is like a bookmarker that maintains position, uses __next__
from typing import List, Iterator
from collections.abc import Iterable

class Calendar(Iterable[str]):
    def __init__(self, days: List[str]):
        self.days = days
    
    def __iter__(self) -> Iterator[str]:
        """Returns an iterator over the lecture days this week"""
        return iter(self.days)

lecture_days = Calendar(['Monday', 'Wednesday', 'Thursday'])

for lecture in lecture_days:
    print(lecture)

