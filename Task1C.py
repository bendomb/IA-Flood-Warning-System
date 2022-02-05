from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    """Requirements for Task 1C"""

    # Build list of stations
    stations = build_station_list()

    # Defines centre (city centre)
    centre = (52.2053, 0.1218)

    # Defines radius
    r = 10

    # Calls function
    x = stations_within_radius(stations, centre, r)

    print (x[:10])
    print (x[-10:])
