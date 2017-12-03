"""This module calculates the number of people in the station by the time the next train arives"""

def before_train_station_pop(station, escalator):
    """This function calculates the total number of people as a sume of people
    waiting to board the next train, and the number of people waiting to leave
    the station by the elebvators."""

    station.travelers_departing = station.travelers_departing + (escalator.rate * station.escalators_entering * station.train_wait)
    # number of people who have arived and want to leave.
    station.travelers_arriving = station.travelers_arriving - (escalator.rate * station.escalators_exiting * station.train_wait)
