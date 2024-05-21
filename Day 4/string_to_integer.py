# Write a Python program with a function that converts a string to an integer.
#  Handle exceptions within the function and print appropriate error messages.\


def string_to_int(s):
    try:
        num = int(s)
        return num
    except ValueError:
        print("Error:" ,s," is not a valid integer.")
        return None

# Test the function
print(string_to_int("1234"))  # Output: 1234
print(string_to_int("abcd"))  # Output: Error: 'abcd' is not a valid integer.
