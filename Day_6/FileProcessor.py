# Create a class called FileProcessor with methods to read data from a file, write data to a file, and append data to an existing file.

class FileProcessor:
    @staticmethod
    def read_file(file_name):
        try:
            with open(file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return f"Error: File '{file_name}' not found."

    @staticmethod
    def write_file(file_name, data):
        try:
            with open(file_name, 'w') as file:
                file.write(data)
                return f"Data written to '{file_name}' successfully."
        except Exception as e:
            return f"Error occurred while writing to '{file_name}': {e}"

    @staticmethod
    def append_file(file_name, data):
        try:
            with open(file_name, 'a') as file:
                file.write(data)
                return f"Data appended to '{file_name}' successfully."
        except Exception as e:
            return f"Error occurred while appending to '{file_name}': {e}"

# Example usage:
file_name = "examples.txt"

# Writing data to file
print(FileProcessor.write_file(file_name, "Hello, World!"))

# Reading data from file
print("Data read from file:", FileProcessor.read_file(file_name))

# Appending data to file
print(FileProcessor.append_file(file_name, "\nAppending more data."))

# Reading data from file after appending
print("Data read from file after appending:", FileProcessor.read_file(file_name))
