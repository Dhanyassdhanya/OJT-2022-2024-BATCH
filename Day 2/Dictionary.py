#  Iterate over keys and values in a dictionary. 

names={"fname:" : "Dhanya","age:":25}
for a,b in names.items():
    print(a,b)

#  Create a dictionary and access its elements
dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print("Name:", dict['name'])
print("Age:", dict['age'])
print("City:", dict['city'])

#  Add a key-value pair to an existing dictionary.
edict = {'name': 'Alice', 'age': 30}
edict['city'] = 'New York'
print("Updated dictionary:", edict)

#  Check if a key exists in a dictionary
kdict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
key_to_check = 'city'
if key_to_check in kdict:
    print(f"{key_to_check} exists in the dictionary.")
else:
    print(f"{key_to_check} does not exist in the dictionary.")
