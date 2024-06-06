import numpy as np

# Create an original array
arr1 = np.array([1, 2, 3, 4, 5])
print("Original array:", arr1)
print("Array1 base:", arr1.base)  # Should print None

# Create a view array
arr2 = arr1.view()
print("View array:", arr2)
print("Array2 base:", arr2.base)  # Should print the original array

# Create a copied array
arr3 = arr1.copy()
print("Copied array:", arr3)
print("Array3 base:", arr3.base)  # Should print None