"""Defines lists and performs operations on them"""
from typing import List

my_nums: List[int] = [6,7,8,9]
words: List[str] = ['never', 'gonna', 'give', 'you', 'up']

split_words: List[str] = 'never gonna give you up'.split()
# ['never', 'gonna', 'give', 'you', 'up']

chopped_words: List[str] = 'never gonna give you up'.split('e')
# ['n', 'v', 'r gonna giv', ' you up']

phrase: str = ' '.join(['never', 'gonna', 'give', 'you', 'up'])
# ['never', 'gonna', 'give', 'you', 'up']

last_word: str = words[-1]
#negative indices count from right

two_to_five: List[str] = words[2:5]
#a:b gets all members of list from a to b

letters: List[str] = list('abcdefghijklmnopqrstuvwxyz')
#makes a list with each letter of the alphabet as individual arguments

print(words)
print(split_words)
print(chopped_words)
print(phrase)
print(last_word)
print(two_to_five)
print(f'{letters[-len(letters)]} {''.join(letters[23:])} {letters[-1]}')
