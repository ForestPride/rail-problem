"""Creates the station class"""


class Station:
    """
    Each train station is an instance of the Station class.
    Methods:
    __init__: creates a new stations
    total_station_pop: calculates total station population
    """

    def __init__(self):
        self.capacity = int(eval(input("Enter the max capacity of the station: ")))
        #testfuntion()
        self.escalators = int(eval(input("Enter the number of escalators in the station: ")))
        #testfuntion()
        self.train_wait = int(eval(input("Enter the wait time between trains in seconds: ")))
        #testfuntion()
        self.travelors_arriving = int(eval(input("How many people just exited the train? ")))
        #testfuntion()
        self.travelors_departing = int(eval(input("How many people are waiting for the train? ")))
        #testfuntion()
