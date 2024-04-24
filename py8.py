def tuple_to_string(my_tuple):
    return ''.join(map(str, my_tuple))

# Test the function
my_tuple = (1, 2, 3, 4, 5)
result_string = tuple_to_string(my_tuple)
print("Tuple converted to string:", result_string)
