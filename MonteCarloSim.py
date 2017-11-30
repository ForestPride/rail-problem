
from StationPopWithoutTrain import *
from StationPopWithTrain import *

def simulation(station, train, escalator):
    overflows = 0
    for i in range(10):
        # Let time pass with no train in the station.
        population = before_train_station_pop(station, escalator_standing)
        # check to see if the sation overflows.
        if population >= station.capacity:
            overflows = overflows + 1

        # Calculate the station population second by second while the train is at the sation.
        # Starting a clock when the train arrives.
        dwell_time = 0
        while station.departing != 0 or Train.pop != train.cap:
            pupulation = population + durring_train_station_pop(station, train, escalator_standing)
            # Advance the clock one second.
            dwell_time = dwell_time + 1
            # Check to see if the station overflows.
            if population >= station.capacity:
                overflows = overflows + 1

    return overflows, dwell_time
