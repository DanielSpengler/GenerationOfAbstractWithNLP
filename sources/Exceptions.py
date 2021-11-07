
"""
Collection of all possible Exception types coming from this module
"""

class TransformerNotInitializedException(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg


class InvalidModelException(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg