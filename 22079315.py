# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 01:02:23 2024

@author: USER
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import os

# Get the current directory of the script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Assuming your data file is named 'data5-1.csv'
data_file_name = 'data5-1.csv'

# Combine the current directory and file name to create the full file path
full_file_path = os.path.join(current_directory, data_file_name)

# Read the data from the CSV file into a DataFrame
try:
    data = pd.read_csv(full_file_path, header=None, names=['Annual Salary'])
except FileNotFoundError:
    print(f"Error: The file {data_file_name} does not exist in the specified directory.")
    exit()
except pd.errors.EmptyDataError:
    print(f"Error: The file {data_file_name} is empty.")
    exit()
except pd.errors.ParserError:
    print(f"Error: Unable to parse data from the file {data_file_name}. Check the file format.")
    exit()

# Create a probability density function and plot as a histogram
plt.hist(data['Annual Salary'], bins=10, density=True, alpha=0.6, color='r', label='Histogram (Data)')

# Calculate mean annual salary (W~)
mean_salary = np.mean(data['Annual Salary'])

# Calculate the standard deviation
std_dev = np.std(data['Annual Salary'])

# Create a range of values for the probability density function
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mean_salary, std_dev)

# Plot the probability density function
plt.plot(x, p, 'k', linewidth=2, label=f'Probability Density Function (PDF) - W~: {mean_salary:.2f}')

# Determine the required value X based on your specific criteria (mentioned in the assignment)
# For example, let's say it's the 25th percentile
x_percentile = 10
x_value = np.percentile(data['Annual Salary'], x_percentile)

# Plot a vertical line at the calculated X value
plt.axvline(x_value, color='r', linestyle='--', label=f'X Value ({x_percentile}%): {x_value:.2f}')

# Set axis labels, title, and legend for the final graph
plt.xlabel('Annual Salary')
plt.ylabel('Probability Density')
plt.title('Histogram with PDF and X Value Marked')

# Display the legend
plt.legend()

# Display the final graph
plt.show()

# Print mean salary (W~) and X values
print(f"Mean Salary (W~): {mean_salary:.2f}")
print(f"X Value ({x_percentile}%): {x_value:.2f}")
