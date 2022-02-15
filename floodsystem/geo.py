# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine

"""Task 1B"""
def stations_by_distance(stations, p):
    #function which returns list of (station, distance) tuples sorted by their distance from p
    
    stations_list = []
    #list which will have (station, distance) tuples appended to it

    for station in stations:
        distance = haversine(station.coord, p)
        #calculates distance between station and p

        stations_list.append([station, distance])
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

"""Task 1E"""

def rivers_by_station_number(stations, N):
    """ function that returns an ordered list of rivers with highest number of monitoring stations.
    The length of the list is determined by N """

    rivers_and_num_stations = []
    # create an empty list to put information in

    for river in stations_by_river(stations):
    # iterate through dictionary created using the stations_by_river function (Task 1D)

        num_stations = len(stations_by_river(stations)[river])
        # calculates number of stations associated with a river by the length of the list

        rivers_and_num_stations.append( (river, num_stations) )
        # add tuples of the format (river name, number of stations)
    
    rivers_and_num_stations.sort(reverse=True, key=lambda tup: tup[1])
    # sort list by number of stations in order of highest to lowest

    min_num_stations = rivers_and_num_stations[N-1][1]
    # calculate number of stations for Nth river

    shortened_list = []
    # create an empty list to add the qualifying tuples into

    for tuple in rivers_and_num_stations:
    # iterate over tuples in the ordered list
        if tuple[1] >= min_num_stations:
        # if the number of stations is greater than or equal to the amount for the N'th river 

            shortened_list.append(tuple)
            # add the river to the shortened list
            # this should be ordered since the rivers_and_num_stations is ordered
    
    return shortened_list