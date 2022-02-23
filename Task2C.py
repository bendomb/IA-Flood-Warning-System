from floodsystem.stationdata import build_station_list, update_water_levels
import floodsystem.station as station
import floodsystem.flood as flood

stations = build_station_list()
update_water_levels(stations)

def run():
    """Requirements for Task 2C"""

    high_list = flood.stations_highest_rel_level(stations, 10)
    for i in range(len(high_list)):
        print(high_list[i][0], high_list[i][1])

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    print()
    run()