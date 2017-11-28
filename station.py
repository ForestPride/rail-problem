"""Creates the station class"""



#import ask_user from ask_user
#import int_check from int_check
#import reasonable_check from reasonable_check


class Station:
    """
    Each train station is an instance of the Station class.
    Methods:
    __init__: creates a new stations
    total_station_pop: calculates total station population
    ask_user(prompt, lower_range, upper_range): function to get input, maybe it should live
    somewhere else?
    """

    def __init__(self, capacity, escalators, train_wait, travelors_arriving, travelors_departing):
        self.capacity = user.says("Enter the max capacity of the station between" lower "and" upper)
        self.escalators = user.says("Enter the number of escalators in the station between" lower "and" upper)
        self.train_wait = user.says("Enter the wait time between trains in seconds between" lower "and" upper)
        self.travelors_arriving = user.says("How many people just exited the train? between" lower "and" upper)
        self.travelors_departing = user.says("How many people are waiting for the train? between" lower "and" upper)
