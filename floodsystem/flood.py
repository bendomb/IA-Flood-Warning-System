from floodsystem.stationdata import build_station_list, update_water_levels
import floodsystem.station as station
from .utils import sorted_by_key

stations = build_station_list()
update_water_levels(stations)

def stations_level_over_threshold(stations, tol):
    listtuple=[]
    for station in stations:
        if stations[station].typical_range_consistent() == True:
            ratio = stations[station].relative_water_level()
            if ratio > tol:
                listtuple.append((stations[station].name, ratio))
    return sorted_by_key(listtuple, 1, reverse=True)