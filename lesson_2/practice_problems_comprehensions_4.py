'''Given the following data structure, write some code that defines a dictionary where the key is the
first item in each sublist, and the value is the second.'''

lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

# Expected result, Pretty printed for clarity

expected = {
    'a': 1,
    'b': 'two',
    'sea': {'c': 3},
    'D': ['a', 'b', 'c']
}

dictionary = { lst[index][0]: lst[index][1] for index, _ in enumerate(lst) }

print(dictionary == expected)
