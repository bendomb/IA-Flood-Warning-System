# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.geo import rivers_by_station_number


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town
    assert s.typical_range_consistent() == True

def test_rivers_by_station_number():
    stations = build_station_list()

    list = rivers_by_station_number(stations, 2)

    # check that number of stations for the second station is lower than the first one
    assert list[0][1] > list[1][1]

def test_inconsistent_stations():
    # Build list of stations
    stations = build_station_list()

    # Checks that each value is a string
    for station in inconsistent_typical_range_stations(stations):
        assert type(station) == str 

test_rivers_by_station_number()