from random import *

def durring_train_station_pop(station, train, escalator):
    """
    calculate the population of the platform with train in station by looping
    through a second by second time step and calculate the platform population
    for each second.
    """
    # Generate a random number to set the size of the train.
    dice_roll = random()
    # The number of cars the train has.
    if  dice_roll < 0.30:
        train.cars(8)

    elif dice_roll > 0.30 < 0.60:
        train.cars(10)

    else:
        train.cars(12)
    # The number of people on the train.
    train.pop = int(dice_roll * train.car_capacity * train.cars))
    # Train max capacity
    train.cap = int(train.car_capacity * train.cars))
    """
    The number of people that want to get off the train.
    There is a new random number here so that the percentage of people leaving
    the train does not depend on the population
    """
    Leaving_train = train_pop * random()
        # People exit the train,  but first we need to calculate the train boarding,
        # and exiting rate.
        if (Station.capacity % Station_1.pop) < train.board_rate * train.cars:
            train.board_rate = station.capacity // (station.pop * train.cars)
        else:
            train.board_rate = escalator.rate

        population = station.pop +
                        # People getting off the train.
                        train.board_rate -
                        # People leave by escalator.
                        (station.escalators_exitying * escalator.rate) +
                        # People enter by escalator.
                        (station.escalators_entering * escalator.rate)
        return population
