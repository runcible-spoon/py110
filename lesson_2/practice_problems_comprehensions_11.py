'''
The following dictionary has list values that contains strings. Write some code to create a list of 
every vowel (a, e, i, o, u) that appears in the contained strings, then print it.

Start by trying to write this using nested loops.

Extra Challenge: Once your nested loop code works, try to refactor the code so it uses a single list 
comprehension. (You can print the resulting list outside of the comprehension.)
'''

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

VOWELS = {'a', 'e', 'i', 'o', 'u'}

list_of_vowels = []

for list in dict1.values():
    for char in ''.join(list):
        if char in VOWELS:
            list_of_vowels.append(char)

expected = ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']

print(list_of_vowels == expected)

list_of_vowels = [
    char for list in dict1.values()
         for char in ''.join(list)
         if char in VOWELS
]

print(list_of_vowels == expected)
