import numpy as np

# Create the original array
original_array = np.array([1, 2, 3, 4, 5])

# Make a view of the original array
view_array = original_array.view()

# Change the original array
original_array[0] = 99

# Display both arrays
print("Original array:", original_array)
print("View array:", view_array)
