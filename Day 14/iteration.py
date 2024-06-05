# iterations
import numpy as np
# for_in loop
#1D Array

arr_1D = np.array([1,2,3,4,5,6])
# Iterate the elements in the array
print("Array_id : ",arr_1D)
for elements in arr_1D:
    print(elements)

# Create a 2D array
arr_2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
# Iterate 2D array
print("Array_2D : ",arr_2D)
# for rows in arr_2D:
#     print(rows)

#     for elements in rows:
#         print(elements)
for elements in np.nditer(arr_2D):
    print(elements)

# Iterate the elements with index
for index ,elements in np.ndenumerate(arr_2D):
    print("Index : ",index ,"Elements",elements)
