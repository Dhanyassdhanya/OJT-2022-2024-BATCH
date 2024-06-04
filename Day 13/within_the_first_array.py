import numpy as np

# Example array
arr = np.array([[[1, 2, 3],[4, 5, 6],[7, 8, 9]],[[10, 11, 12],[13, 14, 15],[16, 17, 18]],[[19, 20, 21],[22, 23, 24],[25, 26, 27]]])

# Access the element directly
element = arr[0, 1, 2]

# Print the element
print("Element at 0th array, 1st row, 2nd column:", element)