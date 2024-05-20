# Write a Python program to calculate the factorial of a number using a lambda function and reduce function.

from functools import reduce

# Define the factorial function using reduce and a lambda function
factorial = lambda n: reduce(lambda x, y: x * y, range(1, n + 1)) 
print(factorial(5))
