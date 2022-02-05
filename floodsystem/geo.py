# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit

"""Task 1B"""
def stations_by_distance(stations, p):
    #function which returns list of (station, distance) tuples sorted by their distance from p
    
    stations_list = []
    #list which will have (station, distance) tuples appended to it

    for station in stations:
        distance = haversine(station.coord, p)
        #calculates distance between station and p

        stations_list.append((station.name, distance))
        #add stations data to stations_list

    sorted_stations_list = sorted_by_key(stations_list, 1)
    #sorts stations by distance from p

    return sorted_stations_list

"""Task 1C"""
def stations_within_radius(stations, centre, r):
    #function which returns list of all stations within radius r
    
    stations_list = []
    #list which will have stations within radius appended to it

    for station in stations:
        distance = haversine(station.coord, centre)
        #calculates distance between station and centre

        if distance < r:
            stations_list.append(station.name)
            #add stations data to stations_list if within radius

        
    return stations_list

"""Task 1D"""

def rivers_with_station(stations):
    #function which returns a container of rivers with a monitoring station

    river_set = set()
    #creates empty set to contain rivers - will contain no duplicates

    for station in stations: 
        river_set.add(station.river)
    return river_set
    #adds rivers with stations to river_set

def stations_by_river(stations):
    #function which returns a dictionary that maps river names to list of station objects on a given river
    
    river_stations_dict = {}
    #creates empty dictionary  
    
    for station in stations: 
    #iterates through list of MonitoringStation objects
        if station.river in river_stations_dict:
        # if dictionary already contains river associated with station

            river_stations_dict[station.river].append(station.name)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
            river_stations_dict[station.river].sort()
            # add the station to the river 'key' and alphabetically sort list of stations associated with the river
        
        else: 
            river_stations_dict[station.river] = [station.name]
            # if the river is not already in the dictionary, add it and assign the station name as a value 
              
    return river_stations_dict
