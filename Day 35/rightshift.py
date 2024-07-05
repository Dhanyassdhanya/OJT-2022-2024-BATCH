# Write a Python function right_shift(num, n) that takes two numbers num and n as  
# arguments and returns value of the integer num rotated to the right by n positions. 
# Assume both the numbers are unsigned. Invoke the function and print the return value.
def right_shift(num, n):
    return num >> n


num = 60
n = 2
result = right_shift(num, n)
print(f"The result of right shifting {num} by {n} positions is {result}")
