# Write a Python function check_strong_number(num) that accepts a positive integer as argument and returns
#  True if the number is strong number else false. 
# Invoke the function and based on return value print the number is strong number or not.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def check_strong_number(num):
    digits = [int(digit) for digit in str(num)]
    sum_of_factorials = sum(factorial(digit) for digit in digits)
    return sum_of_factorials == num

num = 145

if check_strong_number(num):
    print(f"The number {num} is a strong number")
else:
    print(f"The number {num} is not a strong number")
