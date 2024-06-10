#  Convert the array into a 1D array
import numpy as np

# Step 1: Create a 3D array with shape (2, 2, 2)
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print("3D Array:")
print(array_3d)

# Step 2: Convert the 3D array to a 1D array
array_1d = array_3d.flatten()

print("\n1D Array:")
print(array_1d)
