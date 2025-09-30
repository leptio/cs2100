from typing import Set, Dict, List, Tuple
from random import random

#Array is not flexible because of the space it needs
#Python gives list [] (mutable)
#Python gives tuple () (immutable)
#Python gives set {} (immutable) (unordered), can only hold one item at most - no duplicates
#Python gives dict {} (mutable) (key:value), keys are unique (form a set)
#Curly brackets can mean either set or dict

numbers: Set[int] = set(range(5))

float_set: Set[float] = set()
for i in range(100):
    random_float = round(random(), 2)
    float_set.add(random_float)

print(len(float_set))

ages: Dict[str, int] = {'elephant':12, 'cat':10}
#get key "cat" through various methods:
print(ages['cat']) #10
print(ages.get('cat')) #10
print(ages.get('dog')) #None
print(ages.get('dog', 3)) #3 (default value)
#print(ages['dog']) #KeyError

#dict iteration
for key in ages:
    print(f"{key}'s age is {ages.get(key)}")

also_ages: List[Tuple[str, int]] = ([('elephant', 12), ('cat', 12)])

print(ages)
print(also_ages)
