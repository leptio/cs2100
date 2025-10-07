from typing import Callable, Optional
divide: Callable[[int, int], Optional[float]] = lambda num, den: num/den if den!=0 else None
print(divide(9,0))
print(divide(9,3))
