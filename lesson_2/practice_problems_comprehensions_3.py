'''
Given the following data structure, return a **new** list with the same structure, 
but with the values in each sublist ordered in ascending order **as strings** 
(that is, the numbers should be treated as strings). 

Use a comprehension if you can. (Try using a `for` loop first.)
'''

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# Expected result
expected = [['a', 'b', 'c'], [-3, 11, 2], ['black', 'blue', 'green']]

new_list = []
for sublist in lst:
    new_list.append(sorted(sublist, key=str))

print(new_list)
print(expected == new_list)

new_list = [ sorted(sublist, key=str) for sublist in lst ]

print(new_list)
print(expected == new_list)
