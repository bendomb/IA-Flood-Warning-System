from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.geo import rivers_by_station_number
import floodsystem.flood as flood
stations = build_station_list()
update_water_levels(stations)

'''----------------Task 2B Test-----------------'''
def test_stations_level_over_threshold():
    list = flood.stations_level_over_threshold(stations, 0.8)
    # check that all the water levels returned are above the required bound
    for station in range(len(list)):
        assert list[station][1] > 0.8

test_stations_level_over_threshold()

'''----------------Task 2C Test-----------------'''

def test_stations_highest_rel_level():
    list = flood.stations_highest_rel_level(stations, 10)    
    # check that water level for the second station is lower than the first one
    assert list[0][1] > list[1][1]
    # check that length of list is 10
    assert len(list) == 10
test_stations_highest_rel_level()