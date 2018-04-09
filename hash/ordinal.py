"""Hash functions based on the ordinals of the input string's characters."""

from . import base

class ProgressiveHash(base.HashFunction):
    """
    Hashes a string by progressively calculating over the ordinals of its
    characters.
    """
    def hash(self, string):
        hash_result = 0
        for char in string:
            hash_result = self._compute_next_hash_result(hash_result, char)
        return hash_result

    def _compute_next_hash_result(self, current_hash_result, char):
        hash_result = current_hash_result * ord(char) + 1
        hash_result = hash_result % 29
        return hash_result
