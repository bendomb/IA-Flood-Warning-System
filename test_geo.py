from floodsystem.geo import stations_by_distance, stations_within_radius, rivers_with_station, stations_by_river, rivers_by_station_number
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation


'''TEST STATIONS: to be used in test functions to see if functions work with any inputs'''

# creates attributes of test station 1
station_id1 = "test station id 1"
measure_id1 = "test measure id 1"
label1 = "TS1"
coord1 = (1.0, 4.0)
typical_range1 = (-2, 5)
river1 = "River Cam"
town1 = "Town 1"
# formats attributes as station under TestStation1
TestStation1 = MonitoringStation(station_id1, measure_id1, label1, coord1, typical_range1, river1, town1)

# creates attributes of test station 2
station_id2 = "test station id 2"
measure_id2 = "test measure id 2"
label2 = "TS2"
coord2 = (0.0, 1.0)
typical_range2 = (-2, 2)
river2 = "River Cam"
town2 = "Town 2"
# formats attributes as station under TestStation2
TestStation2 = MonitoringStation(station_id2, measure_id2, label2, coord2, typical_range2, river2, town2)

# creates attributes of test station 3
station_id3 = "test station id 3"
measure_id3 = "test measure id 3"
label3 = "TS3"
coord3 = (1.0, 1.0)
typical_range3 = (-2, 3)
river3 = "River Thames"
town3 = "Town 3"
# formats attributes as station under TestStation3
TestStation3 = MonitoringStation(station_id3, measure_id3, label3, coord3, typical_range3, river3, town3)

# list of TestStations
test_stations = [TestStation1, TestStation2, TestStation3]

'''----------------Task 1B Test-----------------'''
# test for stations_by_distance()
def test_stations_by_distance():

    # applying function to list
    TestResult1B = stations_by_distance(test_stations, (0, 0))

    # check: results should be in this order as TestStation 2 is the closest to (0,0), followed by TestStation 3 and then TestStation 1 
    assert (TestResult1B[0][0], TestResult1B[1][0], TestResult1B[2][0]) == (TestStation2, TestStation3, TestStation1)

test_stations_by_distance()

'''----------------Task 1C Test-----------------'''

# test for stations_within_radius()
def test_stations_within_radius():
    
    # applying function to list
    centre = (0,0)
    radius = 2.0
    TestResult1C = stations_within_radius(test_stations, centre, radius)
    print (TestResult1C)
'''NOT WORKING -.-'''
test_stations_within_radius()

'''----------------Task 1D Tests-----------------'''

# test for rivers_with_station()
def test_rivers_with_station():
    assert rivers_with_station(test_stations) == {'River Cam', 'River Thames'}

# test for stations_by_river()
def test_stations_by_river():
    assert sorted(stations_by_river(test_stations)['River Cam']) == [TestStation1.name, TestStation2.name]
