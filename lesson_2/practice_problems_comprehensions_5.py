'''Given the following data structure, sort the list so that the sub-lists are ordered based on the sum 
of the *odd* numbers that they contain. You shouldn't mutate the original list.'''

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

'''
Note that the first sublist has the odd numbers 1 and 7; the second sublist has odd numbers 1, 5, and 3; 
and the third sublist has 1 and 3. Since (1 + 3) < (1 + 7) < (1 + 5 + 3), the sorted list should look 
like this:
'''

# Expected result

expected = [[1, 8, 3], [1, 6, 7], [1, 5, 3]]

# Try to use a comprehension in your solution.

def odd_sum(num_list):
    sum = 0
    for num in num_list:
        if num % 2 == 1:
            sum += num
    return sum

new_list = sorted(lst, key=odd_sum)

print(new_list == expected)

new_list = [ sublist for sublist in sorted(lst, key=odd_sum) ]
print(new_list == expected)
