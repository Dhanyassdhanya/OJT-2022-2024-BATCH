# Function: Add
def add(a, b): 
    print ("Adding : %d + %d" % (a, b)) 
    return a + b 
# Function: Subtract 
def subtract(a, b): 
    print ("Subtracting : %d - %d" % (a, b)) 
    return a - b 
# Function: Multiply 
def multiply(a, b): 
    print ("Multiplying : %d * %d" % (a, b))
    return a * b 
# Function: Divide 
def divide(a, b):
     print ("Dividing : %d / %d" % (a, b))
     return a / b 
print ("Let's use the functions created by us")
 # Calling Functions 
A = add(5, 5) 
B = subtract(5, 6)
C = multiply(6, 5) 
D = divide(5, 5) 
print ("A : %d | B : %d | C : %d | D : %d" % (A, B, C, D))