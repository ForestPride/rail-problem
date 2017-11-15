"""Creates the escalator class"""


class Escalator:
    """
    Each escalator is an instance of the escalator class.
    Methods:
    __init__: creates a new escalator
    rate: calculates the rate people leave the escalator
    """

    def __init__(self):
        self.stand_time = None
        self.stand_space = None
        self.walk_time = None
        self.walk_space = None

    
    @property
    def rate(self):
        return (self.stand_time * self.stand_space) + self.walk_time * (self.walk_space)
