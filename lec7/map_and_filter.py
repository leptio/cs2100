"""Uses and tests map() and filter()"""

#map(function, collection) applies the function to each element and yields results one by one

#filter() iterates only over elements where the function returns True

phrase: str = 'tired of rick astley'

def is_long(word_var: str) -> bool:
    """checks if a word is at least 4 letters"""
    return len(word_var) >= 4

#map
for word in map(str.upper, phrase.split()):
    print(word)

#filter
for word in filter(is_long, phrase.split()):
    print(word)
