# Load the data into a pandas DataFrame.
# Perform data cleaning and preprocessing:
# Check for and handle missing values.
# Convert the Date column to a datetime type.
# Use NumPy to calculate the following statistics for the temperature:
# Mean
# Standard deviation
# Maximum
# Minimum
# Generate a time series plot using Matplotlib to show the temperature trend over time.
# Create a bar chart to show the average monthly precipitation.
# Plot a scatter plot to examine the relationship between wind speed and temperature.



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data into a pandas DataFrame
data = pd.read_csv('weather_data.csv')

# Perform data cleaning and preprocessing
# Check for and handle missing values
data.dropna(inplace=True)  # remove rows with missing values

# Convert the Date column to a datetime type
data['Date'] = pd.to_datetime(data['Date'])

# Calculate statistics for the temperature
temp_mean = np.mean(data['Temperature'])
temp_std = np.std(data['Temperature'])
temp_max = np.max(data['Temperature'])
temp_min = np.min(data['Temperature'])

print("Temperature Statistics:")
print(f"Mean: {temp_mean:.2f}")
print(f"Standard Deviation: {temp_std:.2f}")
print(f"Maximum: {temp_max:.2f}")
print(f"Minimum: {temp_min:.2f}")

# Generate a time series plot using Matplotlib to show the temperature trend over time
plt.plot(data['Date'], data['Temperature'])
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.title('Temperature Trend Over Time')
plt.show()

# Create a bar chart to show the average monthly precipitation
data.groupby(data['Date'].dt.month)['Precipitation'].mean().plot(kind='bar')
plt.xlabel('Month')
plt.ylabel('Average Precipitation')
plt.title('Average Monthly Precipitation')
plt.show()

# Plot a scatter plot to examine the relationship between wind speed and temperature
plt.scatter(data['Wind Speed'], data['Temperature'])
plt.xlabel('Wind Speed')
plt.ylabel('Temperature')
plt.title('Relationship between Wind Speed and Temperature')
plt.show()