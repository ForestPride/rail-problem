"""Creates the station class"""


from request_integer_in_range import request_integer_in_range

class Station:
    """
    Each train station is an instance of the Station class.
    Methods:
    __init__: creates a new stations
    request_integer_in_range : requests an integer in a range

    """

    def __init__(self):
        self.capacity = request_integer_in_range("Enter the station capacity between 10 and 10000: ", 10, 10000)
        self.escalators = request_integer_in_range("Enter an odd number of escalators between 1 and 7: ", 1, 7)
        self.train_wait = request_integer_in_range("Enter the wait time between trains in seconds between 60 and 1800 ", 60, 1800)
        self.travelers_arriving = request_integer_in_range("Enter the number of people that exited the train between 1 and 500: ", 1, 500)
        self.travelers_departing = request_integer_in_range("Enter the number of people waiting for the train between 1 and 500: ", 1, 500)

    @property
    def pop(self):
        """Computes the total population of the station."""
        return self.travelers_arriving + self.travelers_departing

    @property
    def escalators_entering(self):
        """compute the number of escalators leaving the station."""
        return (self.escalators // 2)

    @property
    def escalators_exiting(self):
        """compute the number of escalators exiting the station."""
        return (self.escalators // 2) + 1
