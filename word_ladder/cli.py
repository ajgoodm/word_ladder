import logging
from pathlib import Path

import click

from word_ladder.corpus import Corpus
from word_ladder.settings import Config, PKG_DIR
from word_ladder.utils.words import is_only_lowercase_az, parse_words

logging.basicConfig(**Config.LOGGING_CONFIG)
logger = logging.getLogger(__name__)

SCRABBLE_CORPUS = PKG_DIR / "data" / "corpora" / "scrabble_corpus"


@click.group()
def cli():
    """Entrypoint for word-ladder cli."""


@cli.command(help="calculate the shortest word ladder between two words")
@click.option(
    "--word-1",
    type=str,
    required=True,
    help="first word composed of lowercase characters from a-z",
)
@click.option(
    "--word-2",
    type=str,
    required=True,
    help="second word composed of lowercase characters from a-z",
)
@click.option(
    "--corpus-file",
    type=click.Path(dir_okay=False, readable=True),
    default=None,
    show_default=True,
    help="Path to a newline-separated list of words from which "
    "to construct a word ladder. If none is provided, word "
    "ladders are constructed from words in the "
    "Scrabble dictionary.",
)
def get_ladder(word_1: str, word_2: str, corpus_file: str):
    for word in [word_1, word_2]:
        if not is_only_lowercase_az(word):
            raise ValueError(
                f"words must match regex `^[a-z]*$`; received {word_1} and {word_2}"
            )

    if corpus_file is not None:
        corpus = Corpus(parse_words(Path(corpus_file)))
    else:
        corpus = Corpus.load_graphs(SCRABBLE_CORPUS)

    print(
        f"The shortest ladder from {word_1} to {word_2} is {corpus.get_ladder(word_1, word_2)}"
    )
