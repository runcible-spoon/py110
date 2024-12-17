'''
Given the following data structure return a new list identical in structure to the original, 
but containing only the numbers that are multiples of 3.

Try to use a comprehension for this. However, we recommend first trying it without comprehensions.
'''

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

expected = [[], [3, 12], [9], [15, 18]]

new_list1 = []
for sublist in lst:
    new_sublist = []
    for element in sublist:
        if element % 3 == 0:
            new_sublist.append(element)
    new_list1.append(new_sublist)

print(new_list1)
print(new_list1 != lst, new_list1 == expected)
 
new_list2 = [ [ element for element in sublist if element % 3 == 0 ] for sublist in lst ]

print(new_list2 != lst, new_list2 == expected)
print(new_list2)
