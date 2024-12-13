'''
- Define vowel set
- Initialize empty dictionary
- For element in original list, append element.join to dictionary as keys, with 0 as values 
- For element, element + 1 in dict.keys: 
- If both characters not in vowel set, increment value +1
- Initialize return list
- Sort dict by values
- Turn dict keys into list
- Return list
'''

def sort_by_consonant_count(strings):
    strings.sort(key=count_max_adjacent_consonants, reverse=True)
    return strings

def count_max_adjacent_consonants(string):
    vowels = {'a', 'e', 'i', 'o', 'u'}

    string = ''.join(string.split(' '))
    max_consonants = 0
    adjacent_consonants = ''

    for letter in string:
        if letter not in vowels: 
            adjacent_consonants += letter
            if len(adjacent_consonants) > max_consonants:
                if len(adjacent_consonants) > 1:                
                    max_consonants = len(adjacent_consonants)
        else:
            if len(adjacent_consonants) > max_consonants:
                if len(adjacent_consonants) > 1:                
                    max_consonants = len(adjacent_consonants)

            adjacent_consonants = ''
    
    return max_consonants


my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list) == ['dddaa', 'ccaa', 'aa', 'baa'])

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list) == ['salt pan', 'can can', 'batman', 'toucan'])

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list) == ['bar', 'car', 'far', 'jar'])

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list) == ['month', 'day', 'week', 'year'])

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list) == ['xxxx', 'xxxb', 'xxxa'])
