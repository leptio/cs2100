from typing import Set, List
from random import random
#Array is not flexible because of the space it needs
#Python gives list [] (mutable)
#Python gives tuple () (immutable)
#Python gives set {} (unordered), can only hold one item at most - no duplicates

numbers: Set[int] = set(range(5))

float_set: Set[float] = set()
for i in range(100):
    random_float = round(random(), 2)
    float_set.add(random_float)

print(len(float_set))


