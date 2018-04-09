import abc

class HashFunction(object):
    """Base class for hash functions."""
    def __init__(self):
        pass

    @abc.abstractmethod
    def hash(self, string):
        """Run the hash function on the string and return the output."""
        pass