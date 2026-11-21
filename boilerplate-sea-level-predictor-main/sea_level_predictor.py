
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    result = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    years = range(1880, 2051)

    plt.plot(
        years,
        [result.slope * year + result.intercept for year in years],
        color="red"
    )

    # Create second line of best fit
    recent_data = df[df["Year"] >= 2000]

    recent_result = linregress(
        recent_data["Year"],
        recent_data["CSIRO Adjusted Sea Level"]
    )

    recent_years = range(2000, 2051)

    plt.plot(
        recent_years,
        [
            recent_result.slope * year + recent_result.intercept
            for year in recent_years
        ],
        color="green"
    )

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
