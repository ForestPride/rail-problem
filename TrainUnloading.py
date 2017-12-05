def train_unloading_station_pop(station, train, escalator):
    """
    calculate the population of the platform while people are disembarking
    from the train. Each run reprisents the passing of one second in time.
    """
    """
    People exit the train, but first we need to calculate the train boarding,
    and exiting rate. if there are fewer spaces on the platform than the maximum
    boarding rate of the trains, then the rate at which people can exit the train
    in one second is equal to the number of empty spaces on the platform.
    """

    if (station.capacity - station.pop) < (train.board_rate * train.cars) and \
    (station.capacity - station.pop) > 0:

        exit_train_rate = (station.capacity - station.pop)

    elif (station.capacity - station.pop) <= 0:

        print("station is at capapcity!")
        exit_train_rate = 0

    elif train.travelers_exiting < train.board_rate:

        exit_train_rate = train.travelers_exiting

    else:
        exit_train_rate = (train.board_rate * train.cars)


    print("exit train rate:", exit_train_rate, "\n")

    if train.travelers_exiting - exit_train_rate >= 0:

        train.travelers_exiting = train.travelers_exiting - exit_train_rate
        train.pop = train.pop - exit_train_rate

    else:
        train.pop = train.pop - train.travelers_exiting
        train.travelers_exiting = 0

    station.travelers_arriving = station.travelers_arriving + \
    exit_train_rate - (station.escalators_exiting * escalator.rate)

    station.travelers_departing = station.travelers_departing + \
    (station.escalators_entering * escalator.rate)
