# Generate word ladders!

A word ladder is a sequence of words that differ by one letter each.
This command line tool allows you to generate the shortest word ladder
between a start word and end word of a given length. It does this using
a collection of graphs (one per word length) where the nodes are words
and an edge between two words indicates that the words differ by one letter.
These graphs have been generated for words in the [Scrabble](https://en.m.wikipedia.org/wiki/Scrabble) dictionary. The CLI then uses the graph utility library [networkx](https://networkx.org)
to find a shortest path (a word ladder) between the start word and end word.

## Installation
`pip` installing the package locally (`pip install -e .`) will install the
necessary dependencies (`click` and `networkx`) and expose the CLI utility, which
can be invoked:

```bash
$ word-ladder --help

➜  word_ladder git:(master) ✗ word-ladder --help
Usage: word-ladder [OPTIONS] COMMAND [ARGS]...

  Entrypoint for word-ladder cli.

Options:
  --help  Show this message and exit.

Commands:
  get-ladder  calculate the shortest word ladder between two words
```

## Usage

To generate a ladder between two words, use the `word-ladder get-ladder`command:

```bash
$ word-ladder get-ladder --word-1 cat --word-2 dog
    The shortest ladder from cat to dog has length 4;
    an example ladder of such length is ['cat', 'cot', 'cog', 'dog']

$ word-ladder get-ladder --word-1 yellow --word-2 orange
    The shortest ladder from yellow to orange has length 20;
    an example ladder of such length is ['yellow', 'bellow', 'billow', 'billon', 'ballon', 'ballot', 'ballet', 'balled', 'bolled', 'bolted', 'boated', 'coated', 'crated', 'craned', 'cranes', 'cranks', 'pranks', 'prangs', 'orangs', 'orange']
```

## Underlying Corpus

By default, word-ladder uses the Scrabble dictionary as its source of all possible
words. The graphs have already been pre-computed and serialized for performance.

If you would like to provide a different corpus, you can do so as a newline-separated
list of words saved to disk. If you provide a path to such a corpus, word-ladder will generate
the necessary graphs on the fly before computing a word ladder.

```bash
$ cat /path/to/a/worse/corpus.txt
    dot
    dit
    kit
    kat
    cat
    dog

$ word-ladder get-ladder --word-1 cat --word-2 dog --corpus-file /path/to/a/worse/corpus.txt
    [ INFO - word_ladder.corpus - 2024-01-05 11:02:01,745 ]: splitting words by length
    [ INFO - word_ladder.corpus - 2024-01-05 11:02:01,745 ]: alphabetizing words
    [ INFO - word_ladder.corpus - 2024-01-05 11:02:01,745 ]: building nodes for words of length 3
    [ INFO - word_ladder.corpus - 2024-01-05 11:02:01,745 ]: building edges for words of length 3
    The shortest ladder from cat to dog has length 6;
    an example ladder of such length is ['cat', 'kat', 'kit', 'dit', 'dot', 'dog']
```
