from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()

    # Defines co-ordinate p (city centre)
    p = (52.2053, 0.1218)

    # Calls function
    x = stations_by_distance(stations, p)
    print (x[:10])
    print (x[-10:])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()