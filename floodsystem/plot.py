"""This module provides functionality for plotting tasks (2E, 2F)

"""

import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np


'''Task 2E'''
def plot_water_levels(station, dates, levels):

    plt.plot(dates, levels, label = station.name)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level / m')
    plt.xticks(rotation = 45)
    plt.title(station.name)
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.legend()
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    y = levels

    # Code below adapted from hints for 2F
    # Using shifted x values, find coefficient of best-fit polynomial f(x) of degree p
    p_coeff = np.polyfit(x - x[0], y, p)

    # Convert coefficient into a polynomial that can be evaluated
    poly = np.poly1d(p_coeff)

    # Plot original data points
    plt.plot(x, y, '.')

    # Plot polynomial fit at 30 points along interval (note that polynomial is evaluated using the shift x)
    x1 = np.linspace(x[0], x[-1], 30)
    plt.plot(x1, poly(x1 - x[0]))
    plt.xlabel('date (as a float)')
    plt.ylabel('water level (m)')

    # Display plot
    plt.show()