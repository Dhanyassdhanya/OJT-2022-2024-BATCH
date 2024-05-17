# Write a Python program to print numbers from 1 to 10, but skip printing the number 5 using a for loop and the continue statement.

for i in range(1,11):
    if i==5:
        continue
    print(i)
    
    # As a result, when i equals 5, the continue statement skips the print(i) statement, so the number 5 is not printed. 
    # For all other values of i, the print(i) statement is executed, so numbers from 1 to 4 and from 6 to 10 are printed.