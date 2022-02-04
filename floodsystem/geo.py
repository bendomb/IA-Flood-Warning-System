# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

from haversine import haversine, Unit

def stations_by_distance(stations, p):
    #function which returns list of (station, distance) tuples sorted by their distance from p
    
    stations_list = []
    #list which will have (station, distance) tuples appended to it

    for station in stations:
        distance = haversine(station.coord, p)
        #calculates distance between station and p
        #station coordinate from stationdata

        stations_list.append((station, distance))
        #add stations data to stations_list

    sorted_stations_list = sorted_by_key(stations_list, 1)
    return sorted_stations_list

    

