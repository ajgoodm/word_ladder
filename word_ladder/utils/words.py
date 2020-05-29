from pathlib import Path
import re
from typing import Generator

LOWERCASE_Z_ORD = 122


def count_differences(word_1: str, word_2: str) -> int:
    """Count the number of character positions
    that differ between word_1 and word_2

    Args:
        word_1 (str)
        word_2 (str):

    Returns:
        the number of character positions
        at which word_1 and word_2 differ.
    """
    if len(word_1) != len(word_2):
        raise ValueError(
            "words in a ladder must be the same lenght. "
            f"Received {word_1} and {word_2}"
        )

    n_diffs = 0
    for char_1, char_2 in zip(word_1, word_2):
        if char_1 != char_2:
            n_diffs += 1

    return n_diffs


def is_only_lowercase_az(word: str):
    if re.match("^[a-z]*$", word):
        return True
    return False


def later_neighbors(word: str) -> Generator[str, None, None]:
    """Return the words that differ by a single
    character from `word`. Only checks words that
    alphabetically follow word. Does this by cycling
    through lower case characters at each character
    position.

    Args:
        word (str): lowercase string of characters a-z

    Returns:
        A Generator of all words that alphabetically
        follow `word` and differ by exactly one character.
    """
    assert is_only_lowercase_az(word)

    for idx, char in enumerate(word):
        char_ord = ord(char)
        while char_ord < LOWERCASE_Z_ORD:
            char_ord += 1
            next_word = word[:idx] + chr(char_ord) + word[idx + 1 :]
            yield next_word


def parse_words(corpus_file: Path):
    with open(corpus_file, "r") as file_handle:
        words = file_handle.read().splitlines()
    valid_words = [word for word in words if is_only_lowercase_az(word)]
    return valid_words
