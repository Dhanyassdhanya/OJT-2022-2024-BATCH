import numpy as np 
arr = np.array([1,2,3,4,5,])
print(arr)
print(type(arr))

# min , max
# import numpy library
import numpy as np
# create an array
arr = np.array([1, 2, 3, 4, 5])
# find the minimum value in the array
print(np.min(arr))

# find the maximum value in the array
print(np.max(arr))

from numpy import random
x = random.randint(100)
print(x)

from numpy import random
x = random.randint(100)
print(x)

from numpy import random
x = random.rand()
print(x)

from numpy import random
x = random.randint(100,size=(5))
print(x)

from numpy import random
x = random.randint(100 , size=(3,5))
print(x)

# creating scalars in Numpy
import numpy as np
arr = np.array([10])
print(arr)
scalar = np.asscalar(arr)
print(scalar)