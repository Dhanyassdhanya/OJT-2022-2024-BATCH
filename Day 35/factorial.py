# Factorial
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

# Example usage:
print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1
