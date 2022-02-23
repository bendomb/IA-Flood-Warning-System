from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
import floodsystem.flood as flood
import floodsystem.plot as plot
from datetime import datetime, timedelta
import datetime 

stations = build_station_list()
update_water_levels(stations)

# plots the water levels over the past 10 days for the 5 stations at which the current relative water level is greatest.

def run():
    """Requirements for Task 2E"""

    # makes a list of the 5 stations with the highest relative water level in descending order
    top_five = flood.stations_highest_rel_level(stations, 5)

    for i in range(5):

        station_name = top_five[i][0]
        
        station_check = None
        for station in stations:
            if station.name == station_name:
                station_check = station
                break
            
        if not station_check:
                print("Station {} could not be found".format(station_name))

        dt = 10
        dates, levels = fetch_measure_levels(station_check.measure_id, dt = datetime.timedelta(days=dt))

        plot.plot_water_levels(station, dates, levels)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
