import numpy as np
# Create an originial array
original_array = np.array([1,2,3,4,5,6])
print("original array :" ,original_array)

# Create a view for the array
view_array =original_array.view()
print("View of the original array is : " ,view_array)

view_array[2]= 30
print("Modified vies of the array : " , view_array)
print("Original array after modified th view : " , original_array)

#Create a copy of original array
copy_array = original_array.copy()
print("Copy Array :" ,copy_array)

# Modify element in copy array
copy_array[0]=10
print("Modified copy array : ",copy_array)
print("Original array after modified the copy array : ",copy_array)