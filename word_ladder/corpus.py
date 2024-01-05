from collections import defaultdict
from copy import deepcopy
import logging
from pathlib import Path
from typing import Iterable

import networkx as nx

from word_ladder.execeptions import WordNotFound
from word_ladder.utils.words import later_neighbors

logger = logging.getLogger(__name__)


class Corpus:
    def __init__(self, words: Iterable[str]):
        self._words = defaultdict(list)
        self.graphs = {}

        if words:
            self._sort_words(words)
        self._build_graphs()

    def _sort_words(self, words: Iterable[str]):
        logger.info("splitting words by length")
        for word in words:
            self._words[len(word)].append(word)

        logger.info("alphabetizing words")
        for word_list in self._words.values():
            word_list.sort()

    def _build_graphs(self):
        for word_len, word_list in self._words.items():
            g = nx.Graph()
            logger.info(f"building nodes for words of length {word_len}")
            for word in word_list:
                g.add_node(word)

            logger.info(f"building edges for words of length {word_len}")
            for word_1 in g.nodes:
                for word_2 in later_neighbors(word_1):
                    if word_2 in g.nodes:
                        g.add_edge(word_1, word_2)

            self.graphs[word_len] = deepcopy(g)

    def write_graphs(self, output_dir: Path):
        output_dir.mkdir(parents=True)
        for word_length, graph in self.graphs.items():
            nx.readwrite.gpickle.write_gpickle(graph, output_dir / str(word_length))

    @classmethod
    def load_graphs(cls, output_dir: Path):
        corpus = cls([])
        for path in output_dir.iterdir():
            corpus.graphs[int(path.name)] = nx.readwrite.gpickle.read_gpickle(path)
        return corpus

    def get_ladder(self, word_1: str, word_2: str):
        if len(word_1) != len(word_2):
            raise ValueError(
                f"Words must be the same length to make a word ladder. Got {word_1} and {word_2}"
            )
        if len(word_1) not in self.graphs.keys():
            raise WordNotFound(f"Words {word_1} and {word_2} not in corpus")
        for word in [word_1, word_2]:
            if word not in self.graphs[len(word)].nodes:
                raise WordNotFound(f"Word {word} not in corpus")

        return nx.shortest_path(self.graphs[len(word_1)], word_1, word_2)
