from typing import Callable

add: Callable[[int, int], int] = lambda x,y: print(x+y)
print(add(4,5))
