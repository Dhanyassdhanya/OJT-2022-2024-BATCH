# Write a Python program to Read/Write to a File

# Writing to a file
with open('example.txt', 'w') as file:
    file.write("Hello, World!\nThis is a sample text.")

# Reading from a file
with open('example.txt', 'r') as file:
    data = file.read()
    print(data)

    