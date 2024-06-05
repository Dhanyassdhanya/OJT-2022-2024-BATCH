import numpy as np
# array1 = np.array([1,2,3])
# array2 = np.array([4,5,6])

# print(np.concatenate((array1,array2)))

# Create a 2D array
array2d = np.array([[1,2,3],[4,5,6]])
array2d_1 = np.array([[7,8,9],[10,11,12]])


# Verticaly and Horizontal
# vstack - for vertical 
# hstack - for horizontal
print(np.vstack((array2d,array2d_1)))

print(np.hstack((array2d,array2d_1)))

