import numpy as np

# Create a 2D array
arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

# Accessing single elements
print("Single Element:", arr[1, 2])  

# Slicing arrays
print("Slice 1:", arr[0:2, 1:3])           

# Boolean indexing
print("Boolean Indexing:", arr[arr > 50])  

# Fancy indexing
print("Fancy Indexing:", arr[[0, 2], [1, 2]])  

# Indexing with arrays
rows = np.array([0, 1, 2])
cols = np.array([2, 0, 1])
print("Indexing with Arrays:", arr[rows, cols])  
