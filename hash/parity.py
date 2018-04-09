from . import base

class Parity(base.HashFunction):
    """
    Hash function that returns 0 if the word has an even number of
    characters and 1 if it has an odd number of characters.
    """

    def hash(self, string):
        is_even = len(string) % 2 == 0
        if is_even:
            return 0
        else:
            return 1