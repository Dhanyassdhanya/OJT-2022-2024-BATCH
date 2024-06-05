#   Create an array with data type 4 bytes integer
import numpy as np

# Create an array with 4-byte integers (int32)
int32_array = np.array([1, 2, 3, 4, 5], dtype=np.int32)

# Verify the data type of the array
print(int32_array)
print(f"Data type of int32_array: {int32_array.dtype}")
