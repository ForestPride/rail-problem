def before_train_station_pop(station, escalator):
    # calculate the number of people waiting to depart on the train by the time the train arive.
    station.travelers_departing = station.travelers_departing +
                                    (escalator.rate * escalators.entering * station.train_wait)
    # number of people who have arived and want to leave.
    station.travelers_arriving = station.travelers_arriving -
                                   (escalator.rate * station.train_time
    # Get the total station population.
    population = station.pop
    return population
