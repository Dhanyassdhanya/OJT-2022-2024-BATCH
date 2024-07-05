#  Write a Python function check_amicable_numbers(num1, num2) that accepts two numbers num1 
# and num2 as arguments and returns True if the given pair of numbers are amicable numbers else return false.
#  Invoke the function and based on return value print the numbers are amicable numbers or not.

def sum_of_proper_divisors(num):
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors)

def check_amicable_numbers(num1, num2):
    return (sum_of_proper_divisors(num1) == num2) and (sum_of_proper_divisors(num2) == num1)

num1 = 220
num2 = 284

if check_amicable_numbers(num1, num2):
    print(f"Given numbers {num1} and {num2} are amicable numbers")
else:
    print(f"Given numbers {num1} and {num2} are not amicable numbers")
