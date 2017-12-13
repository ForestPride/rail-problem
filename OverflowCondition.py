def overflow_condition(station):
    if station.travelers_departing < station.capacity:
        station.travelers_arriving = 0
    else:
        station.travelers_arriving = 0
        station.travelers_departing /= 2
