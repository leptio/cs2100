from functools import reduce
from typing import List

def add(num1: int, num2: int) -> int:
    return num1 + num2

my_nums: List[int] = [9,4,2,3,1,2]
my_sum: int = reduce(add, my_nums)
print(my_sum)
