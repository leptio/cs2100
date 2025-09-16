"""Creates a function that adds numbers from a list"""
from typing import List

def sum_with_bad_manners(in_list: List[int]) -> int:
    """Add numbers in a list"""
    new_sum: int = 0
    while len(in_list) > 0:
        new_sum += in_list.pop()
    return new_sum

my_list: List[int] = [1,2,3,4]
print(my_list)
print(f'Sum:{sum_with_bad_manners(my_list)}')
print(my_list)
#since list is mutable the function removes things from the list
