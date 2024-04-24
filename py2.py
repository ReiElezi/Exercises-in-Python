def find_max_min(numbers):

    max_num = min_num = numbers[0]  
    for num in numbers:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num
    return max_num, min_num


my_list = [10, 5, 8, 2, 15, 3]
max_num, min_num = find_max_min(my_list)
print("The largest number in the list is:", max_num)
print("The smallest number in the list is:", min_num)