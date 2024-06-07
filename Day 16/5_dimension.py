import numpy as np

# Create a 5-dimensional array using ndmin
array_5d = np.array([1, 2, 3, 4], ndmin=5)

# Print the array and its shape
print("Array:\n", array_5d)
print("Shape of the array:", array_5d.shape)

# Verify that the last dimension has the value 4
if array_5d.shape[-1] == 4:
    print("The last dimension has the value 4.")
else:
    print("The last dimension does not have the value 4.")
