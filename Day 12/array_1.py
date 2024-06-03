import numpy as np

# Create an with 1-D array
array_1D = np.array([1,2,3,4,5])
print ("1D Array : ",array_1D)

# Create a 2-D array

array_2D = np.array([[1,2,3],[4,5,6]])
print ("2D Array : ",array_2D)

# Create a 3-D array

array_3D = np.array([[[1,2,3],[4,5,6]]])
print ("3D Array : ",array_3D)

# Create an array with ones
 
array_ones =  np.ones ((2,4))
print("Array with ones :" ,array_ones)

# Create an array with zeors

array_zeors = np.zeros ((3,3))
print( "Array with zeros :" ,array_zeors )

#Create an array with a particular range

array_range = np.arange(10)
print ("Array with a range : " ,array_range)