"""Creates the train class"""


from request_integer_in_range import *

class Train:
    """
    Each train in the metro is an instance of the Train class.
    Methods:
    __init__: creates a new train in the station
    """

    def __init__(self):
        self.cars = request_integer_in_range("Enter even number of train cars between 8-12: ", 8, 12)
        self.board_rate = 8
        self.population = population
        self.dwell_time = None
        self.car_capacity = 125
