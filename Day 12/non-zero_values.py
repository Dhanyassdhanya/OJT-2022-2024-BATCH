def count_non_zero_values(array):
    count = 0
    for value in array:
        if value != 0:
            count += 1
    return count

# Example usage:
array = [1, 0, 3, 0, 4, 5, 0, 6]
non_zero_count = count_non_zero_values(array)
print("The number of non-zero values in the array is: ", non_zero_count)
