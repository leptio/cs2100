from typing import Dict

def word_counter(text: str) -> Dict[str, int]:
    word_counts: Dict[str, int] = dict()
    for word in text.split():
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

print(word_counter('hello hi hi hello howdy hi'))