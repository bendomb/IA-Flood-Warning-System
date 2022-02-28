"""This module provides functionality for analysis tasks (2F)

"""

import matplotlib
import numpy as np

def polyfit(dates, levels, p):
    """ station computes a least-squares fit of a polynomial of degree p to water level data """

    # Converting the dates to floats
    x = matplotlib.dates.date2num(dates)

    # Using shifted x values, find coefficient of best-fit polynomial f(x) of degree p
    p_coeff = np.polyfit(x - x[0], levels, p)

    # Convert coefficient into a polynomial that can be evaluated
    poly = np.poly1d(p_coeff)

    return poly, x[0]
