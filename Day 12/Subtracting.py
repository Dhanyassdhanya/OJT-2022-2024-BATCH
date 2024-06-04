import numpy as np

# Create two sample matrices
matrix_c = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

matrix_d = np.array([[9, 8, 7],
                     [6, 5, 4],
                     [3, 2, 1]])

# Subtract the matrices
result_subtraction = matrix_c - matrix_d

print("Matrix C:")
print(matrix_c)

print("Matrix D:")
print(matrix_d)

print("Result of matrix subtraction:")
print(result_subtraction)
