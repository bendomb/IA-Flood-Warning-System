from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
import datetime

from floodsystem.plot import plot_water_level_with_fit, plot_water_levels


def run():
    """Requirements for Task 2F"""

    # Build list of stations
    stations = build_station_list()

    # Updating current water levels
    update_water_levels(stations)

    # Creating a list of the top 5 stations at which the current relative water level is greatest
    top_five = stations_highest_rel_level(stations, 5)
    
    # Setting the time period to extend back 2 days
    time_period_days = 2

    # print(top_five)
    for station in top_five:
    
        dates, levels = fetch_measure_levels(station[0].measure_id, dt=datetime.timedelta(days=time_period_days))
        plot_water_level_with_fit(station[0], dates, levels, 4)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()