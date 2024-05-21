# Write a python program to Delete a file

import os
filename = 'example.txt'
if os.path.exists(filename):
    os.remove(filename)
    print(f"File '{filename}' successfully deleted.")
else:
    print(f"File '{filename}' not found.")
