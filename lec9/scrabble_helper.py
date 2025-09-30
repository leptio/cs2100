"""Helps with scrabble by finding words given letters."""
from typing import Dict, Set
import os

file_path = os.path.join(os.path.dirname(__file__), 'words_alpha.txt')

def scrabble_helper(input_letter: str) -> Dict[int, Set[str]]:
    """Helps find all amounts of a certain letter in all words in the English dictionary."""
    result: Dict[int, Set[str]] = dict()
    with open(file_path, 'r', encoding='utf-8') as english_dict:
        for word in english_dict.readlines():
            if input_letter in word:
                word = word.strip()
                letter_count = word.count(input_letter)
                if letter_count in result:
                    result[letter_count].add(word)
                else:
                    result[letter_count] = {word}
    return result

function_result: Dict[int, Set[str]] = scrabble_helper('r')

for key, value in function_result.items():
    if key > 2:
        print(f'{key}: {value}')
