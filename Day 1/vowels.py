# Write a Python program to count the number of vowels in a string.

vow=input("Enter the words: ")
count=0
for i in vow:

    if i in 'aeiouAEIOU':
        count +=1
print(count)
        