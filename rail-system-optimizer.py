"""
Train station Optimizer!

This program optimizes the efficiency of a train station by simulating normal
operations and varying train schedules and escalator ediquette.
"""

from MonteCarloSim import simulation
from station import Station
from train import Train
from escalator import Escalator

RUNS = int(input("Enter the number of simulations you want to run: "))
FAILURE_TRESHOLD = (int(input("Enter acceptable system failure percentage: ")) // 100) * RUNS

def main():
    print("create a train station: enter the appropriate values for your station.")
    station_1 = Station()
    # Create a new station that is the same as station_1 before runnning the simulation.
    station_2 = station_1
    print("Create a train: enter the appropriate values for your trains.")
    train_1 = Train()
    # Create a standing only escalator.
    print("Create a standing only escalator: enter the data for the behavior you have observed.")
    escalator_1 = Escalator()
    # Create a standing and walking escalator.
    print("Create a standing and walking escalator: enter the data for the behavio you have observed.")
    escalator_2 = Escalator()

    for i in range(RUNS):
        print(station_1.pop)
        while station_1.train_wait != 3600:
            failures = simulation(station_1, train_1, escalator_1)[0]
            print(failures)
            if failures >= FAILURE_TRESHOLD:
                station_1.train_wait = station_1.train_wait + 60
            else:
                pass
        i = i

    for i in range(RUNS):
        while station_1.train_wait != 3600:
            failures = simulation(station_2, train_1, escalator_2)[0]
            print(failures)
            if failures >= FAILURE_TRESHOLD:
                station_2.train_wait = station_2.train_wait + 60
            else:
                pass
        i = i

    print("the time between trains for the station with standing only escalators is: ", station_1.train_wait)
    print("The time between trains for the station with standing and walking escalators is: ", station_2.train_wait)
main()
