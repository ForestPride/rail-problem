"""
Train station Optimizer!

This program optimizes the efficiency of a train station by simulating normal
operations and varying train schedules and escalator ediquette.
"""

from StationPopWithoutTrain import before_train_station_pop
from StationPopWithTrain import durring_train_station_pop
from MonteCarloSim import simulation
from station import Station
from train import Train
from escalator import Escalator

runs = eval(input("Enter the number of simulations you want to run: "))
failure_threshold = (eval(input("Enter acceptable system failure percentage: ")) //
                     100) * runs

def main():
    station_1 = Station()
    # Create a new station that is the same as station_1 before runnning the simulation.
    print(station_1.capacity, "is the station capacity")
    station_2 = station_1
    train_1 = Train()
    # Create a standing only escalator.
    escalator_1 = Escalator()
    # Create a standing and walking escalator.
    escalator_2 = Escalator()

    for i in range(runs):
        while station_1.train_wait != 3600:
            failures = simulation(train_1, station_1, escalator_1)[0]
            print(failures)
            if failures >= failure_threshold:
                station_1.train_wait = station_1.train_wait + 60
            else:
                pass

    for i in range(runs):
        while station_1.train_wait != 3600:
            failures = simulation(train_1, station_2, escalator_2)[0]
            print(failures)
            if failures >= failure_threshold:
                station_2.train_wait = station_2.train_wait + 60
            else:
                pass
main()
