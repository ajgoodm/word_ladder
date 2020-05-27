class WordNotFound(Exception):
    """A word wasn't in the corpus."""

    def __init__(self, error_message: str) -> None:
        self.error_message = error_message
        super().__init__(self, self.error_message)
