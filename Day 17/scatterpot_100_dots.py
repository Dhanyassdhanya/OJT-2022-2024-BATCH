# A scatter plot with 1000 dots
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Generate random data for 1000 points
np.random.seed(0)  # For reproducibility
x = np.random.rand(1000)
y = np.random.rand(1000)

# Step 2: Create the scatter plot
plt.scatter(x, y, color='blue', marker='o')

# Step 3: Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with 1000 Dots')

# Step 4: Display the plot
plt.show()
