# creating scalars in Numpy
import numpy as np
arr = np.array([10])
print(arr)
scalar = np.isscalar(arr)
print(scalar)

# creating vector in Numpy
import numpy as np
list1 =  [1,2,3]
list2 = [[10],[20],[30]]
vector1 = np.array(list1)
vector2 = np.array(list2)
print(vector1)
print(vector2)

# creating matrix in numpy
import numpy as np
a = np.matrix('1 2 ; 3 4')
print(a)

# matrix multiplication in numpy
import numpy as np
a = ([1,6,5],[3, 4 ,8] ,[2, 12,3])
b = ([1,2,3],[4,5,6],[7,8,9])
res = np.dot(a,b)
print(res)