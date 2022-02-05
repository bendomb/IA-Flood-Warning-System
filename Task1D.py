from os import stat
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def run():
    """Requirements for Task 1D"""

    # Build list of stations
    stations = build_station_list()

    # Calls function to find rivers with a station and sorts list
    x = sorted(rivers_with_station(stations))

    # prints number of stations and first 10 stations
    print(len(x), " stations")
    print()
    print("First 10 - ", x[:10])
    print()

    station_aire = sorted(stations_by_river(stations)['River Aire'])
    station_cam = sorted(stations_by_river(stations)['River Cam'])
    station_thames = sorted(stations_by_river(stations)['River Thames'])

    print()
    print("River Aire: ", station_aire)
    print()
    print("River Cam: ", station_cam)
    print()
    print("River Thames: ", station_thames)

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    print()
    run()