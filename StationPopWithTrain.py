"""
This module allows one second of time to pass with a train in the station.
It uses the rates of people leaving and enering the station from escalators and
train to calculate the total population of the station every second.
"""

def train_unloading_station_pop(station, train, escalator):
    """
    calculate the population of the platform while people are disembarking
    from the train. Each run reprisents the passing of one second in time.
    """
    """
    People exit the train, but first we need to calculate the train boarding,
    and exiting rate. if there are fewer spaces on the platform than the maximum
    boarding rate of the trains, then the rate at which people can exit the train
    in one second is equal to the number of empty spaces on the platform.
    """

    if (station.capacity % station.pop) < train.board_rate * train.cars:
        exit_train_rate = (station.capacity % station.pop)
    else:
        exit_train_rate = train.board_rate

    station.travelers_arriving = station.travelers_arriving + exit_train_rate
    station.travelers_departing = station.travelers_departing + (station.escalators_entering * escalator.rate)

def train_boarding_station_pop(station, train, escalator):
    """
    calculate the population of the station while people are boarding the train.
    each run reprisents the passing of one second in time.
    """
    train.pop = train.pop + train.board_rate
    station.travelers_departing = station.travelers_departing - train.board_rate + (station.escalators_entering * escalator.rate)
    station.travelers_arriving = station.travelers_arriving - (station.escalators_exiting * escalator.rate)
