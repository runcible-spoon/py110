# Consider the following nested dictionary:

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

'''Compute and display the total age of the family's male members. Try 
working out the answer two ways: first with an ordinary loop, then with a
 comprehension.

The result should be `444`.'''

total = 0
for member in munsters.values():
    if member['gender'] == 'male':
        total += member['age']

print(total)

total = sum([member['age'] for member in munsters.values() if member['gender'] == 'male'])
print(total)
