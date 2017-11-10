

from random import *

#choose how many times we allow the simulation to run.

def sim_no_train(station_standing, station_walking, train, escalator_standing, escalator_walking):
    standing_overflows = 0
    # Let time pass with no train in the station.
    population = before_train_station_pop(station, escalator_standing)
    # check to see if the sation overflows.
    if population >= station.capacity:
        standing_overflows = standing_overflows + 1

    walking_overflows = 0
    # Let time pass with no train in the station.
    population = before_train_station_pop(station, escalator_walking)
    # check to see if the sation overflows.
    if population >= station.capacity:
        walking_overflows = overflows + 1

    return standing_overflows, walking_overflows, dwell_time_standing, dwell_time_walking

def sim_train(station_standing, station_walking, train, escalator_standing, escalator_walking):

    # Starting a clock when the train arrives.
    dwell_time_standing = 0
    # Calculate the station population second by second while the train is at the sation.
    while station.departing != 0 or Train.pop != train.cap:
        pupulation = population + durring_train_station_pop(station, train, escalator_standing)
        # Advance the clock one second.
        dwell_time_standing = dwell_time_standing + 1
        # Check to see if the station overflows.
        if population >= station.capacity:
            standing_overflows = standing_overflows + 1

    # Starting a clock when the train arrives.
    dwell_time_walking = 0
    # Calculate the station population second by second while the train is at the sation.
    while station.departing != 0 or Train_1.pop != train.cap:
        # Calculate the station population second by second while the train is at the sation.
        pupulation = population + durring_train_station_pop(station, train, escalator_walking)
        # Advance the clock one second.
        dwell_time_walking = dwell_time_walking + 1
        # Check to see if the station overflows.
        if population >= station.capacity:
            walking_overflows = overflows + 1

    return standing_overflows, walking_overflows, dwell_time_standing, dwell_time_walking
