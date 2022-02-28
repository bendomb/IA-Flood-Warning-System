from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_level_with_fit
import matplotlib.pyplot as plt
import datetime
import numpy as np

from floodsystem.plot import plot_water_level_with_fit, plot_water_levels


def run():
    """Requirements for Task 2G"""

    # Build list of stations
    stations = build_station_list()

    # Ensure stations have up-to-date data
    update_water_levels(stations)

    # Create list of stations and their relative water levels
    levelstations = stations_highest_rel_level(stations, len(stations)) 

    # Create empty arrays for different risk categories
    low_risk, moderate_risk, high_risk, severe_risk = [], [], [], []

    # Iterate over stations
    for i in levelstations:
        # Separating into categories by relative water level
        if i[1]<-1:
            low_risk.append(i[0].name)
        elif i[1]<0:
            moderate_risk.append(i[0].name)
        elif i[1]<1:
            high_risk.append(i[0].name)
        else:
            severe_risk.append(i[0].name)

    print(severe_risk)

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()