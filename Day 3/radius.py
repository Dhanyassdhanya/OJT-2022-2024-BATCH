# Write a Python function to calculate the area of a circle given its radius.

radius = int(input("Enter the no"))

def area(radius):
    return 3.14159 * radius ** 2

print("The area of the circle with radius ",radius ,"is",area(radius))
