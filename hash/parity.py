from . import base

class Parity(base.HashFunction):
    def hash(self, string):
        is_even = len(string) % 2 == 0
        if is_even:
            return 0
        else:
            return 1