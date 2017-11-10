"""Creates the station class"""


class Station:
    """
    Each train station is an instance of the Train class.
    Methods:
    __init__: creates a new stations
    total_station_pop: calculates total station population
    """

    def __init__(self, capacity, escalators, train_wait, travelors_arriving, travelors_departing):
        self.capacity = capacity
        self.escalators = escalators
        self.train_wait = train_wait
        #self.arrivalrate = arrivalrate
        #self.departurerate = departurerate
        self.travelors_arriving = travelors_arriving
        self.travelors_departing = travelors_departing
