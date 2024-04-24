def remove_duplicates(input_list):
    return list(set(input_list))

# Test the function
my_list = [1, 2, 3, 4, 3, 2, 1, 5, 6, 7, 6]
print("Original list:", my_list)
unique_list = remove_duplicates(my_list)
print("List after removing duplicates:", unique_list)
