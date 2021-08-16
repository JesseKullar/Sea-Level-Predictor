import pandas as pd
import matplotlib.pyplot as plt
import scipy
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', sep=',')
    # Create scatter plot
    fig = plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    lin1 = scipy.stats.linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = range(1880, 2051)
    plt.plot(x1, lin1.intercept + lin1.slope*x1)
    # Create second line of best fit
    lin2 = scipy.stats.linregress(df['Year'][120::], df['CSIRO Adjusted Sea Level'][120::])
    x2 = range(2000, 2051)
    plt.plot(x2, lin2.intercept + lin2.slope*x2)
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()