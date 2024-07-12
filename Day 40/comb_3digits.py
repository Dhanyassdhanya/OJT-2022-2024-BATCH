
# Write a Python program to make combinations of 3 digits.

from itertools import combinations

def make_combinations(nums):
    return list(combinations(nums, 3))

nums = [1, 2, 3, 4]
print(make_combinations(nums))


