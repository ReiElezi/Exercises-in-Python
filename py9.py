def element_exists_in_tuple(my_tuple, element):
    return element in my_tuple

# Test the function
my_tuple = (1, 2, 3, 4, 5)
element_to_check = 3
if element_exists_in_tuple(my_tuple, element_to_check):
    print(f"The element {element_to_check} exists in the tuple.")
else:
    print(f"The element {element_to_check} does not exist in the tuple.")

