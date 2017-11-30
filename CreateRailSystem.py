from RailSystem import *

def create_rail_system(station, train, escalator_standing, escalator_walking):
    #Create the station, train, and escalator objects.

    print()"Create an initial station.\n")
    # The number of escalators in the station.
    station.capacity = eval(input("Enter the max capacity of the station:\n"))
    # The number of escalators in the station.
    station.escalators = eval(input("Enter the number of escalators in the station:\n"))
    # The time between trains.
    station.train_wait = eval(input("Enter the wait time between trains:\n"))
    # Number of people waiting for the train.
    station.travelers_departing = eval(input("How many people departing?\n"))
    # Number of people lined up at the escalators to leave the station.
    station.travelers_arriving = eval(input("How many people just exited the train?\n"))


    print("Create an initial train.\n")
    # The rate, in people per second, of people boarding, or exiting a train car.
    train.board_rate = eval(input("Board Rate:\n"))
    # Maximum number of people that can fit in one train car.
    train.car_capacity = eval(input("Car Capacity:\n"))


    print("Create a standing only escalator.")
    # The escalator transit time for standing passengers.
    escalator_standing.stand_time = eval(input("Enter a standing escalator transit time:\n"))
    # The space (stairs between people) for standing passengers.
    escalator_standing.stand_space = eval(input("Enter the number of stairs between standing people:\n"))


    print("Create a standing and walking escalator.")
    # The escalator transit time for walking passengers.
    escalator_walking.walk_time = eval(input("Enter a walking escalator transit time:\n"))
    # The space (stairs between people) for walking passengers.
    escalator_walking.walking_space = eval(input("Enter the number of stairs between people walking:\n"))
