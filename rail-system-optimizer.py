"""
Train station Optimizer!

This program optimizes the efficiency of a train station by simulating normal
operations and varying train schedules and escalator ediquette.
"""


from CreateRailSystem import *
from StationPopWithoutTrain import *
from StationPopWithTrain import *
from MonteCarloSim import *

runs = eval(input("Enter the number of simulations you want to run: "))
failure_threshold = (eval(input("Enter acceptable system failure percentage: ")) //
                    100) * runs

def main():
    station_1 = station()
    station_2 = station_1
    train_1 = train()
    escalator_1 = escalator()
    escalator_2 = escalator()
    system_state = log(0,0,0,0)
    rail_system(station_1, train_1, escalator_1, escalator_2)

    failures = 0
    for i in range(runs):
        old_wait_time = station_1.train_wait

        failures = failures + im_no_train(station_1, train_1, escalator_1)[0]
        if failures > failure_threshold:
            failures = 0
            station_1.train_wait = station_1.train_wait - (old_wait_time / 2)
            sans_train_overflow = True
        else:
            failures = failures + sim_with_train(station_1, train_1, escalator_1)
            if failures > failure_threshold:
                station_1.train_wait = 2 * station_1.train_wait

        if sans_train_overflow:
            time_dfference = old_wait_time - station_1.train_wait
            for j in range(time_difference):
                failure = sim_with_train(station_1, train_1, escalator_1)[0]
                if failures > failure_threshold:
                    station_1.train_wait = station_1.train_wait + j
