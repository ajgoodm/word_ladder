from collections import defaultdict
from typing import Iterable


class WordTree:
    def __init__(self, words: Iterable[str]):
        self.tree = self._tree()
        self._build_tree(words)

    def _tree(self):
        return defaultdict(self._tree)
    
    def _build_tree(self, words: Iterable[str]):
        for word in words:
            d = self.tree
            for char in word:
                d = d[char]
