# Converting 1D into 2D 
# reshape() is the method which is used for reshaping the arrays.

import numpy as np
# Create a 1D array

arr_1D = np.array([1, 2, 3, 4, 5, 6])
print("Array 1D : ",arr_1D)
print("Shape of array 1D :", arr_1D.shape)

# Reshape the 1D array to 2D ARRAY
arr_2D = arr_1D.reshape(2,3)
print("Array 2D : ",arr_2D)
print("Shap of array 2D :",arr_2D.shape)

# Reshape 1D array into 3D array
arr_3D = arr_1D.reshape(3,2)
print("Array 3D : ",arr_3D)
print("Shap of array 3D :",arr_3D.shape)

# Reshape 2D array into 1D array
arr_1D_again = arr_2D.reshape(-1)
print("Array 1D again : ",arr_1D_again)

