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

    # Crates empty lists for closest and furthest stations
    closest = []
    furthest = []

    # prints list of tuples (station name, town and distance) for 10 closest and furthest stations
    for i in x[:10]:
        closest.append((i[0].name, i[0].town, i[1]))
    for i in x[-10:]:
        furthest.append((i[0].name, i[0].town, i[1]))
    print ("closest:", closest)
    print()
    print ("furthest:", furthest)

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    print()
    run()