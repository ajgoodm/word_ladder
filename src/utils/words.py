from copy import copy
from typing import Generator

LOWERCASE_Z_ORD = 122

def count_differences(word_1: str, word_2: str) -> int:
    if len(word_1) != len(word_2):
        raise ValueError("words in a ladder must be the same lenght. "
                         f"Received {word_1} and {word_2}")
    
    n_diffs = 0
    for char_1, char_2 in zip(word_1, word_2):
        if char_1 != char_2:
            n_diffs += 1
    
    return n_diffs


def later_neighbors(word: str) -> Generator[str, None, None]:
    assert word.islower()

    for idx, char in enumerate(word):
        char_ord = ord(char)
        while char_ord < LOWERCASE_Z_ORD:
            char_ord += 1
            next_word = word[:idx] + chr(char_ord) + word[idx + 1:]
            yield next_word