"""Creates the escalator class"""


class Escalator:
    """
    Each escalator is an instance of the escalator class.
    Methods:
    __init__: creates a new escalator
    """

    def __init__(self, stand_time, stand_space, walk_time, walk_space):
        self.stand_time = stand_time
        self.stand_space = stand_space
        self.walk_time = walk_time
        self.walk_space = walk_space
