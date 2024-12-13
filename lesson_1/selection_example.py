def multiply(numbers, factor):
    multiplied_nums = []

    for current_num in numbers:
        multiplied_nums.append(current_num * factor)

    return multiplied_nums
    
my_numbers = [1, 4, 3, 7, 2, 6]
print(multiply(my_numbers, 2)) # [2, 8, 6, 14, 4, 12]
print(my_numbers) # [1, 4, 3, 7, 2, 6]
