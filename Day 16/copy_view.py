import numpy as np

# Create a 1-D array with 12 elements
array_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Reshape the array to a 2-D array with 4 arrays, each containing 3 elements
array_2d = array_1d.reshape(4, 3)

# Check if array_2d is a view or a copy
is_view = np.may_share_memory(array_1d, array_2d)

print("Does array_2d share memory with array_1d?:", is_view)

# Alternatively, modify the reshaped array and check if the original array is affected
array_2d[0, 0] = 99

print("Modified reshaped 2-D array:\n", array_2d)
print("Original 1-D array after modification:\n", array_1d)

# Using np.may_share_memory:
# This function will return True if the two arrays share memory, indicating that one is a view of the other.
# It will return False if they do not share memory, indicating that the second array is a copy.
