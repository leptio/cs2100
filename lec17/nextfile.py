from typing import Iterator
iterator: Iterator[int] = range(5).__iter__()
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
#print(iterator.__next__()) raises StopIteration