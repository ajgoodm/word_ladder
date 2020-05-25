from collections import defaultdict
from copy import deepcopy
import logging
from typing import Iterable

import networkx as nx
from tqdm import tqdm

from src.utils import words

logger = logging.getLogger(__name__)


class Corpus:
    def __init__(self, words: Iterable[str]):
        self.words = defaultdict(list)
        self.graphs = {}

        self._sort_words(words)
        self._build_graphs()

    def _sort_words(self, words: Iterable[str]):
        logger.info('splitting words by length')
        for word in tqdm(words):
            self.words[len(word)].append(word)
        
        logger.info('alphabetizing words')
        for word_list in self.words.values():
            word_list.sort()
    
    def _build_graphs(self):
        for word_len, word_list in self.words.items():
            g = nx.Graph()
            logger.info('building nodes')
            for word in word_list:
                g.add_node(word)
            
            logger.info('building edges')
            for word_1 in tqdm(g.nodes):
                for word_2 in words.later_neighbors(word_1):
                    if word_2 in g.nodes:
                        g.add_edge(word_1, word_2)

            self.graphs[word_len] = deepcopy(g)

    def get_ladder(self, word_1: str, word_2: str):
        if len(word_1) != len(word_2):
            raise ValueError(f"Words must be the same length to make a word ladder. Got {word_1} and {word_2}")
        for word in [word_1, word_2]:
            if word not in self.words[len(word)]:
                raise ValueError(f"Word {word} not in corpus")

        return nx.shortest_path(self.graphs[len(word_1)], word_1, word_2)
        