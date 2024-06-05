#  Change data type from float to integer by using 'i' as parameter value
import numpy as np

# Create a float array
float_array = np.array([1.5, 2.7, 3.1, 4.9, 5.2])

# Convert the float array to an integer array
int_array = float_array.astype('i')

# Print the resulting integer array and its data type
print(int_array)
print(f"Data type of int_array: {int_array.dtype}")
