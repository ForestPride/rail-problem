"""Creates the escalator class"""


class Escalator:
    """
    Each escalator is an instance of the escalator class.
    Methods:
    __init__: creates a new escalator
    rate: calculates the rate people leave the escalator
    """

    def __init__(self):
        self.stand_time = request_integer_in_range("Enter a standing escalator transit time in seconds between 10 and 120:", 10, 120)
        self.stand_space = request_integer_in_range("Enter the number of stairs between standing people between 0 and 5:", 0, 5)
        self.walk_time = request_integer_in_range("Enter a walking escalator transit time in seconds between 20 and 60:", 20, 60)
        self.walk_space = request_integer_in_range("Enter the number of stairs between walking people between 0 and 5:", 0, 5)


    @property
    def rate(self):
        return (self.stand_time * self.stand_space) + (self.walk_time * self.walk_space)
