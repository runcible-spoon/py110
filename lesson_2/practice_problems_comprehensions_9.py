'''
Given the following data structure, write some code to return a list that
contains only the dictionaries where all the numbers are even.
'''



lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

expected = [{'e': [8], 'f': [6, 10]}]

# first attempt
import copy

new_list = []

def are_odd(num_list):
    return [ num % 2 == 1 for num in num_list ]

for dictionary in lst:
    for sublist in dictionary.values():
        if any(are_odd(sublist)):
            print(dictionary)


print(new_list)


new_list = [ dictionary for dictionary in lst
                        for sublist in dictionary.values()
                        if all(are_even(sublist)) ]

print(new_list)


# second attempt
new_lst = [
    dict for dict in lst
    if all(
        [ num % 2 == 0 for sblst in dict.values() for num in sblst ]
     )
 ]

print(new_lst == expected)
