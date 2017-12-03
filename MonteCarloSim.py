
from StationPopWithoutTrain import before_train_station_pop
from StationPopWithTrain import train_unloading_station_pop, train_boarding_station_pop
from random import random

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
    print("the number of train cars is: ", train.cars)

    # The number of people on the train.
    train.pop = int(dice_roll * train.car_capacity * train.cars)
    print("the populatio of the train is: ", train.pop)

    """
    The number of people that want to get off the train.
    There is a new random number here so that the percentage of people leaving
    the train does not depend on the population
    """
    travelers_exiting_train = int(train.pop * random())
    print("the number of travelers exiting the train is: ", travelers_exiting_train)

    overflows = 0
    for i in range(10):
        # Let time pass with no train in the station.
        before_train_station_pop(station, escalator)
        print("the station population is: ", station.pop)
        # check to see if the sation overflows.
        if station.pop >= station.capacity:
            overflows = overflows + 1
            print(overflows)

        """
        Calculate the station population second by second while the train is at the sation.
        Starting a clock when the train arrives.
        """
        dwell_time = 0
        while travelers_exiting_train != 0:
            train_unloading_station_pop(station, train, escalator)
            print("the station population is: ", station.pop)
            # Advance the clock one second.
            dwell_time = dwell_time + 1
            # Check to see if the station overflows.
            if station.pop >= station.capacity:
                overflows = overflows + 1
                print(overflows)

        while station.travelers_departing != 0 or train.pop != train.capacity:
            train_boarding_station_pop(station, train, escalator)
        i = i
    return overflows, dwell_time
