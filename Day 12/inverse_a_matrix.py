import numpy as np

# Create a sample 3x3 matrix
matrix_3x3 = np.array([[1, 2, 3],
                       [0, 1, 4],
                       [5, 6, 0]])

# Calculate the inverse of the matrix
inverse_matrix_3x3 = np.linalg.inv(matrix_3x3)

print("The original 3x3 matrix is:")
print(matrix_3x3)

print("The inverse of the 3x3 matrix is:")
print(inverse_matrix_3x3)
