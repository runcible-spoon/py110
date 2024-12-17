'''Given the following data structure, return a **new** 
list with the same structure, but with the values in each sublist 
ordered in ascending order. Use a comprehension if you can. (Try using a
 `for` loop first.)
 
 The string values should be sorted as strings, while the numeric values should be sorted as numbers.
 '''

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# Expected result

expected = [['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]

# regular loop
new_list = []

for sublist in lst:
    new_list.append(sorted(sublist))

print(new_list == expected)

# comprehension

new_list = [sorted(sublist) for sublist in lst]
print(new_list == ex)
