import numpy as np

# Create a 1-D array with 12 elements
array_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Reshape the array to a 2-D array with 4 arrays, each containing 3 elements
array_2d = array_1d.reshape(4, 3)

# Print the reshaped array
print("Reshaped 2-D array:\n", array_2d)
