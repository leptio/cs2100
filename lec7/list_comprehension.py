"""Applies functions to lists using list comprehension"""
from typing import List, Set

my_nums: List[int] = [6,7,8,9]

#applies function to every value in list, creating new list
#Syntax: [(expression) for (item) in (list) if (condition)]
increased_nums: List[int] = [i+1 for i in my_nums]

def positive_copy(nums: List[int]) -> List[int]:
    """Returns a copy of the list with only positive numbers"""
    return [i for i in nums if i >=0]

print(positive_copy([1,-2,3,-4,5]))

phrase: str = 'never gonna give you up'
letters: Set[str] = {letter.lower() for letter in phrase}

#set does not allow repeated values
print(letters)
