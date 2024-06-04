import numpy as np

# Create a sample matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Calculate the sum of each column
column_sums = np.sum(matrix, axis=0)
print("The sum of each column:" ,column_sums)

# Calculate the sum of each row
row_sums = np.sum(matrix, axis=1)
print("The sum of each row:", row_sums)
