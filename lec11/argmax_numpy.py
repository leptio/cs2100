import numpy as np
from typing import List
words: List[str] = 'never gonna give you up'.split()

#default sort: alphabetical for strings, ascending for numbers
#key parameter lets you pass a function to determine sort order

sorted_alphabetically: List[str] = sorted(words)
print(' '.join(sorted_alphabetically))
indices_of_sorted_words = np.argsort(sorted_alphabetically)
print(indices_of_sorted_words)