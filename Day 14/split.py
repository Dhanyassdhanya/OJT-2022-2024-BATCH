import numpy as np
# Split will work in numpy

array = np.array([1,2,3,4,5,6,7,8,9])
print("Split array : ",np.split(array, 3)) 
# Split the array into 3 equal parts

# multi dimentional
# horizontally and vertically

array_2D = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
vsplit_array = np.vsplit(array_2D,2)
print("Vertical Split : ",vsplit_array)

# Horizonatal
hsplit_array = np.hsplit(array_2D,3)
print("Horizontal Split : ",hsplit_array)