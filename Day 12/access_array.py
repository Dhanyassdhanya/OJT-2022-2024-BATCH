import numpy as np

array_2D = np.array([[1,2,3],[4,5,6]])

# Accessing a single element
element = array_2D[1,2]
print("Element at the index of [1,2] " , element)

# # Access by row
row = array_2D[1:]
print("Second row :" ,row)

# #  : symbol refers to entire rows
row = array_2D[0,:]
print("Second row :" ,row)

# #  Access second row
row = array_2D[:,1]
print("Second row :" ,row)

#  Access second column
column = array_2D[:,1]
print("Second column :" ,column)

# Slicing
# Access the subarray with row of 0 and 1,coloumn of and 2
slicing_array = array_2D[0:2,1:3]
print ("subarray :" ,slicing_array)

