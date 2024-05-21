# Write a Python program that reads a file and prints its content. Handle ‘FileNotFoundError’ and ‘PermissionError’ exceptions.

def read_and_print_file(filename):
    try:
        with open(filename, 'r') as file:
            print(file.read())
    except (FileNotFoundError, PermissionError) as e:
        print("Error: ",e)

# Example usage
filename = 'example.txt'
read_and_print_file(filename)
