from floodsystem.stationdata import build_station_list, update_water_levels
import floodsystem.station as station
import floodsystem.flood as flood

stations = build_station_list()
update_water_levels(stations)

# creates a list of consistent stations
consistent_stations = []
for station in stations:
    if station.typical_range_consistent() == True:
        consistent_stations.append(station)
    
def run():
    """Requirements for Task 2B"""

    suitable_stations = flood.stations_level_over_threshold(consistent_stations, 0.8)
    for i in range(len(suitable_stations)):
        print(suitable_stations[i][0], suitable_stations[i][1])

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    print()
    run()