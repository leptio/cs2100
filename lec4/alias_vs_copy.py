"""Alias vs. Copy demo"""
from typing import List

original: List[int] = [1,2,3]

alias: List[int] = original
copy: List[int] = original.copy()

original[2] = 90

print(alias)
#[1,2,90]
print(copy)
#[1,2,3]

print(id(original))
print(id(alias))
print(id(copy))
#original and alias have same address in memory
#copy has a different one

