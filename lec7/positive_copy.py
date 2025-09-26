from typing import List

def positive_copy (nums: List[int]) -> List[int]:
    result: List[int] = list()
    for i in nums:
        if i>=0:
            result.append(i)
        return result