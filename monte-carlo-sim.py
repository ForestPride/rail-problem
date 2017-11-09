"""
Train station Optimizer!

This program optimizes the efficiency of a train station by simulating normal
operations and varying train schedules and escalator ediquette.
"""

from random import *

#choose how many times we allow the simulation to run.
runs = eval(input("Enter the number of simulations you want to run: "))

#Create the station, train, and escalator objects.

station_1 = station()
print()"Create an initial station.\n")
# The number of escalators in the station.
station_1.capacity = eval(input("Enter the max capacity of the station:\n"))
# The number of escalators in the station.
station_1.escalators = eval(input("Enter the number of escalators in the station:\n"))
# The time between trains.
station_1.train_wait = eval(input("Enter the wait time between trains:\n"))
# Number of people waiting for the train.
station_1.travelers_departing = eval(input("How many people departing?\n"))
# Number of people lined up at the escalators to leave the station.
station_1.travelers_arriving = eval(input("How many people just exited the train?\n"))


train_1 = train()
print("Create an initial train.\n")
# The rate, in people per second, of people boarding, or exiting a train car.
train_1.board_rate = eval(input("Board Rate:\n"))
# Maximum number of people that can fit in one train car.
train_1.car_capacity = eval(input("Car Capacity:\n"))

escalator_1 = escalator()
print("Create a standing only escalator.")
# The escalator transit time for standing passengers.
escalator_1.stand_time = eval(input("Enter a standing escalator transit time:\n"))
# The space (stairs between people) for standing passengers.
escalator_1.stand_space = eval(input("Enter the number of stairs between standing people:\n"))

escalator_2 = escalator()
print("Create a standing and walking escalator.")
# The escalator transit time for walking passengers.
escalator_1.walk_time = eval(input("Enter a walking escalator transit time:\n"))
# The space (stairs between people) for walking passengers.
escalator_1.walking_space = eval(input("Enter the number of stairs between people walking:\n"))

"""
Calculate the initial population of the platform before a train arives.
This should be two values, one for the people who are waiting for the train,
and one for the lined up at the escalators to leave the station.
"""
# the number of elscalators entering the station.
escalators_in = station_1.escalators // 2
# the number of escalators leaving the sation.
escalators_out = (station_1.escalators // 2) + 1

stading_overflows = 0
walking_overflows =
def before_train_station_pop(station, escalator):
    # calculate the number of people waiting to depart on the train by the time the train arive.
    station.travelers_departing = station.travelers_departing +
                                    (escalator.rate * escalators_in * station.train_wait)
    # number of people who have arived and want to leave.
    station.travelers_arriving = station.travelers_arriving -
                                   (escalator.rate * station.train_time
    # Get the total station population.
    population = station.pop
    return population

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
                        train.board_rate -
                        (escalators_out * escalator.rate) +
                        (escalators_in * escalator.rate)
        return population

for i in range(runs):   
    # Let time pass with no train in the station.
    population = before_train_station_pop(station_1, escalator_1)
    # check to see if the sation overflows.
    if population >= station_1.capacity:
        standing_overflows = overflows + 1

    # Starting a clock when the train arrives.
    dwell_time_standing = 0

    # Calculate the station population second by second while the train is at the sation.
    while station_1.departing != 0 or Train_1.pop != TrainCap:
        pupulation = population + durring_train_station_pop(station_1, train_1, escalator_1)
        # Advance the clock one second.
        dwell_time_standing = dwell_time_standing + 1
        # Check to see if the station overflows.
        if population >= station_1.capacity:
            standing_overflows = overflows + 1
    i = i + 1

    for i in range(runs):
        # Let time pass with no train in the station.
        population = before_train_station_pop(station_1, escalator_2)
        # check to see if the sation overflows.
        if population >= station_1.capacity:
            walking_overflows = overflows + 1

        # Starting a clock when the train arrives.
        dwell_time_walking = 0

        while station_1.departing != 0 or Train_1.pop != TrainCap:
            # Calculate the station population second by second while the train is at the sation.
            pupulation = population + durring_train_station_pop(station_1, train_1, escalator_2)
            # Advance the clock one second.
            dwell_time_walking = dwell_time_walking + 1
            # Check to see if the station overflows.
            if population >= station_1.capacity:
                walking_overflows = overflows + 1
        i = i + 1
