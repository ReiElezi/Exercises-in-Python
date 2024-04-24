def find_repeated_items(my_tuple):
    item_count = {}
    repeated_items = []

    for item in my_tuple:
        if item in item_count:
            item_count[item] += 1
        else:
            item_count[item] = 1
    
    for item, count in item_count.items():
        if count > 1:
            repeated_items.append(item)
    
    return repeated_items

# Test the function
my_tuple = (1, 2, 3, 4, 1, 2, 5, 6, 3, 7, 8, 2)
repeated_items = find_repeated_items(my_tuple)
print("Repeated items in the tuple:", repeated_items)
