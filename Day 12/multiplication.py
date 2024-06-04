import numpy as np

# Create two 3x3 matrices
matrix_c = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

matrix_d = np.array([[9, 8, 7],
                     [6, 5, 4],
                     [3, 2, 1]])

# Perform matrix multiplication using np.dot()
result_3x3_dot = np.dot(matrix_c, matrix_d)

# Perform matrix multiplication using the @ operator
result_3x3_at = matrix_c @ matrix_d

print("Matrix C:")
print(matrix_c)

print("Matrix D:")
print(matrix_d)

print("Result of 3x3 matrix multiplication using np.dot():")
print(result_3x3_dot)

print("Result of 3x3 matrix multiplication using the @ operator:")
print(result_3x3_at)
