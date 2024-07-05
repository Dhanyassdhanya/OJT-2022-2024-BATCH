# palindrome
def is_palindrome(num):
    return str(num) == str(num)[::-1]

num1 = 12321
num2 = 12345

if is_palindrome(num1):
    print(f"Given number {num1} is a palindrome")
else:
    print(f"Given number {num1} is not a palindrome")

if is_palindrome(num2):
    print(f"Given number {num2} is a palindrome")
else:
    print(f"Given number {num2} is not a palindrome")
