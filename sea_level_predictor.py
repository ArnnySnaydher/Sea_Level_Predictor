import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'],s=5)

    # Create first line of best fit

    line1 = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    x1 = np.arange(df['Year'].min(),2050,1)
    y1 = x1*line1.slope + line1.intercept
    plt.plot(x1,y1,color='darkred')

    # Create second line of best fit

    df2 = df[df['Year'] >= 2000]
    line2 = linregress(df2['Year'],df2['CSIRO Adjusted Sea Level'])
    x2 = np.arange(2000,2050,1)
    y2 = x2*line2.slope + line2.intercept
    plt.plot(x2,y2,color='navy')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()