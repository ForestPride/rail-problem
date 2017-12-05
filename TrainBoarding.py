def train_boarding_station_pop(station, train, escalator):
    """
    calculate the population of the station while people are boarding the train.
    each run reprisents the passing of one second in time.
    """
    # We need to make sure that the next calculation wont't return a negative
    # number of people. If it does, set this population = 0.
    if station.travelers_departing - (train.board_rate * train.cars) + \
    (station.escalators_entering * escalator.rate) >= 0 and \
    train.pop + (train.board_rate * train.cars) <= train.cap:

        train.pop = train.pop + (train.board_rate * train.cars)
        station.travelers_departing = station.travelers_departing - \
        (train.board_rate * train.cars) + \
        (station.escalators_entering * escalator.rate)

    elif station.travelers_departing - (train.board_rate * train.cars) + \
    (station.escalators_entering * escalator.rate) < 0 and \
    train.pop + station.travelers_departing <= train.cap:

        station.travelers_departing = 0
        train.pop = train.pop + station.travelers_departing

    elif station.travelers_departing - (train.cap - train.pop) + \
    (station.escalators_entering * escalator.rate) >= 0 and \
    train.pop + (train.board_rate * train.cars) > train.cap:

        station.travelers_departing = station.travelers_departing - \
        (train.cap - train.pop)
        train.pop = train.cap

    # We need to make sure that the next calculation wont't return a negative
    # number of people. If it does, set this population = 0.
    if station.travelers_arriving - (station.escalators_exiting * escalator.rate) >= 0:

        station.travelers_arriving = station.travelers_arriving - \
        (station.escalators_exiting * escalator.rate)

    else:
        station.travelers_arriving = 0
    return train.pop
