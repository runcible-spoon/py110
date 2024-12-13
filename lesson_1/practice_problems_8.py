# Given the following string, create a dictionary that represents the 
# frequency with which each letter occurs. 
# The frequency count should be case-sensitive:

statement = "The Flintstones Rock"

# The output should resemble the following:

# Pretty printed for clarity
test_dict = {
    'T': 1,
    'h': 1,
    'e': 2,
    'F': 1,
    'l': 1,
    'i': 1,
    'n': 2,
    't': 2,
    's': 2,
    'o': 2,
    'R': 1,
    'c': 1,
    'k': 1
}

def occurences(string):
    letter_occurences = dict.fromkeys(set(''.join(string.split())), 1)

    for letter in letter_occurences:
        if string.count(letter) > 1:
            letter_occurences[letter] = string.count(letter)
    
    return letter_occurences

print(occurences(statement))
