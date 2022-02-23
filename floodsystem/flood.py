from floodsystem.stationdata import build_station_list, update_water_levels
import floodsystem.station as station
from .utils import sorted_by_key

stations = build_station_list()
update_water_levels(stations)

'''Task 2B''' 
def stations_level_over_threshold(stations, tol):
    listtuple=[]
    for station in stations:
        if station.relative_water_level() != None and station.typical_range_consistent() != False:
            ratio = station.relative_water_level()
            if ratio > tol and ratio < 20:
                listtuple.append([station.name, ratio])
    return sorted_by_key(listtuple, 1, reverse=True)