from typing import Iterable, Iterator

class Range(Iterable[int]):
    def __init__(self, start: int, stop: int, step: int = 1):
        self.start = start
        self.stop = stop
        self.step = step
    
    def __iter__(self) -> Iterator[int]:
        if self.start < self.stop:
            return iter(range(self.start, self.stop, self.step))
        else:
            return BackwardsIter(self.start, self.stop, self.step)

class BackwardsIter(Iterator[int]):
    def __init__(self, start: int, stop: int, step: int = 1):
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start
    
    def __next__(self) -> int:
        if self.current <= self.stop:
            raise StopIteration
        value = self.current
        self.current -= self.step
        return value


for i in Range(10, -6, 3):
    print(i)