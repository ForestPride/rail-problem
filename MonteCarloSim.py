from random import random
from SansTrain import before_train_station_pop
from TrainUnloading import train_unloading_station_pop
from TrainBoarding import train_boarding_station_pop
from OverflowCondition import overflow_condition

def simulation(station, train, escalator):
    # Generate a random number to set the size of the train.
    dice_roll = random()
    # The number of cars the train has.
    if  dice_roll <= 0.30:
        train.cars = 8
    elif 0.30 < dice_roll <= 0.60:
        train.cars = 10
    else:
        train.cars = 12
    print("the number of train cars is:", train.cars)
    print("the train capacity is:", train.cap)

    # The number of people on the train.
    train.pop = int(dice_roll * train.car_capacity * train.cars)
    print("the populatio of the train is:", train.pop)

    """
    The number of people that want to get off the train.
    There is a new random number here so that the percentage of people leaving
    the train does not depend on the population
    """
    train.travelers_exiting = int(train.pop * random())
    print("the number of travelers exiting the train is:", train.travelers_exiting, "\n")

    overflows = 0
    # Let time pass with no train in the station.
    before_train_station_pop(station, escalator)
    print("there is no train in the station.\ntraverlers departing = ", \
    station.travelers_departing, "\ntravelers_arriving = ", \
    station.travelers_arriving, "\n")
    # check to see if the sation overflows.
    if station.pop >= station.capacity:
        overflows = overflows + 1
        overflow_condition(station)
        print(overflows)

    """
    Calculate the station population second by second while the train is at the sation.
    Starting a clock when the train arrives.
    """
    dwell_time = 0
    while train.travelers_exiting > 0:
        train_unloading_station_pop(station, train, escalator)
        print("the train is unloading.\ntraverlers departing =", \
        station.travelers_departing, "\ntravelers_arriving =", \
        station.travelers_arriving)

        print("people exiting train =", train.travelers_exiting)
        print("train population = ", train.pop, "\n")
        # Advance the clock one second.
        dwell_time = dwell_time + 1
        # Check to see if the station overflows.
        if station.pop >= (station.capacity - 1):
            overflows = overflows + 1
            overflow_condition(station)
            print("the station has overflowed while the train is unloading", overflows, "times")


    while station.travelers_departing > 0:
        train_boarding_station_pop(station, train, escalator)
        print("the train is boarding.\ntraverlers departing = ", \
        station.travelers_departing, "\ntravelers_arriving = ", \
        station.travelers_arriving)

        print("train population =", train.pop, "\n")
        if station.pop >= (station.capacity - 1):
            overflows = overflows + 1
            overflow_condition(station)
            print("the station has overflowed while the train is boarding", overflows, "times")
        if train.pop >= (train.cap):
            break

    return overflows, dwell_time
