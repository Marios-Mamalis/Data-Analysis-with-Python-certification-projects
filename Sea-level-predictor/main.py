import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    years1 = list(range(1880, 2051))
    years2 = years1.copy()[(2000-1880):]

    # Create scatter plot
    fig, ax = plt.subplots()
    df.plot.scatter(x='Year', y='CSIRO Adjusted Sea Level', ax=ax)

    # Create first line of best fit
    slope1, intercept1, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(years1, [i * slope1 + intercept1 for i in years1])

    # Create second line of best fit
    slope2, intercept2, _, _, _ = linregress(df.loc[(2000-1880):,'Year'], df.loc[(2000-1880):,'CSIRO Adjusted Sea Level'])
    plt.plot(years2, [i * slope2 + intercept2 for i in years2])

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
