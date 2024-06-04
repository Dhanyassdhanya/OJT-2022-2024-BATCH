def get_third_and_fourth_and_add(array):
    if len(array) < 4:
        return "Array doesn't have enough elements"
    
    third_element = array[2]
    fourth_element = array[3]
    
    sum_of_third_and_fourth = third_element + fourth_element
    
    return sum_of_third_and_fourth

# Example usage:
my_array = [1, 2, 3, 4, 5]
result = get_third_and_fourth_and_add(my_array)
print("Sum of third and fourth elements:", result)
