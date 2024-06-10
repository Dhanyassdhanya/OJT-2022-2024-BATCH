#  Convert 1D array with 8 elements to 3D array with 2x2 elements
import numpy as np

# Step 1: Create a 1D array with 8 elements
array_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Step 2: Reshape the 1D array to a 3D array with shape (2, 2, 2)
array_3d = array_1d.reshape((2, 2, 2))

print("1D Array:")
print(array_1d)

print("\n3D Array:")
print(array_3d)
