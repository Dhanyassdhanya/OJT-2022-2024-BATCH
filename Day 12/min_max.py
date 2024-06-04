import numpy as np

# Create a sample matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Get the maximum and minimum values
max_value = np.max(matrix)
min_value = np.min(matrix)

print(f"The maximum value in the matrix is: {max_value}")
print(f"The minimum value in the matrix is: {min_value}")
