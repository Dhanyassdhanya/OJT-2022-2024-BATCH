# Use the scatter() method to draw a scatter plot diagram

import matplotlib.pyplot as plt

# Sample data for the scatter plot
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [2, 3, 4, 5, 6, 7, 8, 9]

# Create the scatter plot
plt.scatter(x, y, color='blue', marker='o')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sample Scatter Plot')

# Display the plot
plt.show()
