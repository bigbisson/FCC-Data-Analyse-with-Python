import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y)

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x, y)

    x2 = list(range(1880, 2050))
    y2 = []

    for year in x2:
        y2.append(intercept + slope*year)

    plt.plot(x2, y2)

    # Create second line of best fit
    xx = df[df['Year'] >= 2000]['Year']

    yy = df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level']

    slope2 = linregress(xx, yy).slope
    intercept2 = linregress(xx, yy).intercept

    x3 = list(range(2000, 2050))
    y3 = []
    for year in x3:
        y3.append(intercept2 + slope2*year)

    plt.plot(x3, y3)

# Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

# Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
