'''
Given the following data structure, return a new list identical in structure to the original but, 
with each number incremented by 1. Do not modify the original data structure. Use a comprehension.
'''

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

expected = [{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}]

new_list = []

for dictionary in lst:
    new_dict = {}
    for key in dictionary:
        incremented_num = dictionary[key] + 1
        new_dict[key] = incremented_num
    new_list.append(new_dict)


print(lst != new_list)
print(new_list == expected)

new_list = [ { key: value + 1 for key, value in dictionary.items() } for dictionary in lst ]

print(lst != new_list)
print(new_list == expected)
