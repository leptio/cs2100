# Union (A | B) -> Elements in either set
# Intersection (A & B) -> Elements in both sets
# Subset (A <= B) -> True of all a in b
# Strict subset (A < B) -> a<=b and not equal
# Subtraction (A - B) -> elements in a and not in b
from typing import Set

nums_a: Set[int] = set(range(1,5))
nums_b: Set[int] = set(range(3,9))

print(nums_a | nums_b)
print(nums_a & nums_b)
print (nums_a <= nums_b)
print(nums_a - nums_b)
