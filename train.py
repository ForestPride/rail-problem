"""Creates the train class"""

class Train:
    """
    Each train in the metro is an instance of the Train class.
    Methods:
    __init__: creates a new train in the station
    """

    def __init__(self):
        self.cars = None
        self.board_rate = 8
        self.pop = None
        self.travelers_exiting = None
        self.dwell_time = None
        self.car_capacity = 125

    @property
    def cap(self):
        return self.cars * self.car_capacity
