from floodsystem.stationdata import build_station_list, update_water_levels
import floodsystem.station as station
import floodsystem.flood as flood

stations = build_station_list()
update_water_levels(stations)

consistent_stations = []
for station in stations:
    if station.typical_range_consistent() == True:
        consistent_stations.append(station)
    

suitable_stations = flood.stations_level_over_threshold(consistent_stations, 0.8)
for i in range(len(suitable_stations)):
    print(suitable_stations[i][0], suitable_stations[i][1])