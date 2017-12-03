"""Creates the escalator class"""
from request_integer_in_range import request_integer_in_range

class Escalator:
    """
    Each escalator is an instance of the escalator class.
    Methods:
    __init__: creates a new escalator
    rate: calculates the rate people leave the escalator
    """

    def __init__(self):
        self.standing_transit_time = request_integer_in_range("Enter the transit time when standing on the escalator in seconds between 0 and 120:", 0, 120)
        self.people_standing = request_integer_in_range("Enter the number of people standing between 0 and 500:", 0, 500)
        self.walking_transit_time = request_integer_in_range("Enter the transit time when walking on the escalator in seconds between 0 and 60:", 0, 60)
        self.people_walking = request_integer_in_range("Enter the number of people walking between 0 and 500:", 0, 500)


    @property
    def rate(self):
        return (self.people_standing / self.standing_transit_time) + (self.people_walking / self.walking_transit_time)
