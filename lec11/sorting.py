from typing import List
words: List[str] = 'never gonna give you up'.split()

#default sort: alphabetical for strings, ascending for numbers
#key parameter lets you pass a function to determine sort order

sorted_alphabetically: List[str] = sorted(words)
print(' '.join(sorted_alphabetically))

sorted_by_length: List[str] = sorted(words, key=lambda word: len(word))
print(' '.join(sorted_by_length))

sorted_by_reverse_length: List[str] = sorted(words, key=lambda word: -len(word))
print(' '.join(sorted_by_reverse_length))

print(sorted(words, key=lambda word: len([i for i in word if i in 'aeiou'])))
