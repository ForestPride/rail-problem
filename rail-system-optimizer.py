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
FAILURE_TRESHOLD = (int(input("Enter acceptable system failure percentage: ")) / 100) * RUNS

def main():
    print("create a standing train station: enter the appropriate values for your station.")
    station_1 = Station()
    # Create a new station that is the same as station_1 before runnning the simulation.
    print("create a walking and standing train station: enter the appropriate values for your station.")
    station_2 = Station()
    train_1 = Train()
    # Create a standing only escalator.
    print("Create a standing only escalator: enter the data for the behavior you have observed.")
    escalator_1 = Escalator()
    # Create a standing and walking escalator.
    print("Create a standing and walking escalator: enter the data for the behavio you have observed.")
    escalator_2 = Escalator()

    print("failure threshold", FAILURE_TRESHOLD)

    for i in range(RUNS):
        print("station population", station_1.pop, "\n")
        failures = simulation(station_1, train_1, escalator_1)[0]
        print(failures, "failures")
        if failures >= FAILURE_TRESHOLD:
            station_1.train_wait += 60
            print("failure threshold reached.")
        else:
            pass

    print("End standing station test.\nStart standing and walking station test.\n")

    for i in range(RUNS):
        print("station population", station_1.pop, "\n")
        failures = simulation(station_2, train_1, escalator_2)[0]
        print(failures, "failures")
        if failures >= FAILURE_TRESHOLD:
            station_2.train_wait += 60
            print("failure threshold reached.")
        else:
            pass
    print("the time between trains for the station with standing only escalators is: ", station_1.train_wait / 60)
    print("The time between trains for the station with standing and walking escalators is: ", station_2.train_wait / 60)
main()
