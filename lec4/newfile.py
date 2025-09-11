from typing import List
def sum_with_bad_manners(in_list: List[int]) -> int:
    sum: int = 0
    while (len(in_list) > 0):
        sum += in_list.pop()
    return sum

my_list: List[int] = [1,2,3,4]
print(my_list)
print(f'Sum:{sum_with_bad_manners(my_list)}')
print(my_list)
#since list is mutable the function removes things from the list