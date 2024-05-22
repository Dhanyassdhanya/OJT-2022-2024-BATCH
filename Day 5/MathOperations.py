# Create a class called MathOperations with class methods for basic mathematical operations like addition, subtraction, multiplication, 
# and a static method to find the factorial of a number.

class MathOperations:
    @classmethod
    def add(cls, a, b):
        return a + b

    @classmethod
    def subtract(cls, a, b):
        return a - b

    @classmethod
    def multiply(cls, a, b):
        return a * b

    @staticmethod
    def factorial(n):
        if n == 0:
            return 1
        elif n < 0:
            return "Factorial not defined for negative numbers"
        else:
            result = 1
            for i in range(1, n + 1):
                result *= i
            return result

# Example usage:
print("Addition (5 + 3):", MathOperations.add(5, 3))
print("Subtraction (5 - 3):", MathOperations.subtract(5, 3))
print("Multiplication (5 * 3):", MathOperations.multiply(5, 3))
print("Factorial (5!):", MathOperations.factorial(5))
print("Factorial (-5):", MathOperations.factorial(-5))
